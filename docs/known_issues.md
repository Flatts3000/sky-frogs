# Known Issues

Living tracker of Sky Frogs playtest bugs, limitations, and accepted-for-now quirks. Open *design questions* and deferred features live in [backlog.md](./backlog.md); this doc is for things observed in-game.

## Status legend

| Symbol | Meaning |
|---|---|
| 🔴 | Open. Fix pending. |
| 🟡 | Open. Workaround available. |
| 🟣 | Fix shipped. Awaiting in-game verification. |
| 🔵 | Accepted for now. Low priority; may revisit. |
| 🟢 | Resolved. |

Entries are kept after they are fixed: the diagnosis is the valuable part, and several of these bugs have near-misses that would otherwise be re-derived from scratch.

---

## Open

Three, all root-caused and all owned by another mod. New bugs are filed as [GitHub issues](https://github.com/Flatts3000/sky-frogs/issues) first (see [`github_issues_best_practices.md`](./github_issues_best_practices.md)); they earn an entry here once the root cause is understood, so the ledger records the diagnosis rather than duplicating issue state.

### 🟡 A scooped Slime in a Bucket cannot complete the six Slime-in-a-Bucket quests

Six quests take a Slime in a Bucket with `match_components: "strict"` against exactly `{Category, Variant}`. A **crafted** bucket carries exactly those two keys. A **scooped** one carries more: PF calls `Bucketable.saveDefaultDataToBucketTag` first, which writes `Health` unconditionally (plus `NoAI` / `Silent` / `NoGravity` / `Invulnerable` when set), and only then appends `Category` + `Variant`. Strict matching is exact map equality, so the scooped bucket never matches.

No pack-side setting fixes it: `fuzzy` compares whole components too and fails identically, and `none` would let any slime bucket satisfy the iron quest. The quest text for **A Bucket of Ender Pearl Slime** documents the by-hand scoop route, so the pack currently tells players to do the thing that cannot complete the quest.

**Workaround:** craft the bucket rather than scooping one. **Tracked as [#247](https://github.com/Flatts3000/sky-frogs/issues/247), upstream [productive-frogs#357](https://github.com/Flatts3000/productive-frogs/issues/357).** Reported on Discord by Sam Gomez.

### 🔵 The Copy-Paste Gadget pastes Froglights with no variant

Copying a build containing Froglights and pasting it produces variant-less Configurable Froglights. A placed Froglight keeps its variant in a **block entity** (`ConfigurableFroglightBlockEntity`), and Building Gadgets 2 copies block states, not block-entity data, so the variant is dropped on paste.

Worth knowing because a variant-less Froglight is not a harmless cosmetic loss: it is the item that used to poison Iron Furnaces' smeltability cache and lock out every other Froglight for the session (see the first Resolved entry below, fixed in PF 1.25.4). The paste itself is still lossy.

**Tracked as [#249](https://github.com/Flatts3000/sky-frogs/issues/249).** No upstream issue is filed yet.

### 🔵 Six Supplementaries cutting-board recipes fail to parse

Every world load logs a `RecipeManager` error per broken recipe. All six live under `supplementaries:integration/` and all six write their `farmersdelight:cutting` result in the pre-1.21 shape (`{"item": ...}`) where MC 1.21.1's ItemStack codec wants `{"id": ...}` - and the same jar uses the correct shape in its other Farmer's Delight recipes, so it is a slip rather than a version mismatch. Nothing accepts these; Farmer's Delight is pinned at 1.3.4 and its codec is vanilla's.

| recipe | salvage route lost |
|---|---|
| `lapis_bricks_salvaging_fd` | lapis bricks -> 4 lapis lazuli |
| `ash_bricks_salvaging_fd` | ash bricks -> 4 ash brick |
| `quiver_salvaging_fd` | quiver -> 2 leather |
| `cannon_boat_oak_salvaging_fd` | cannon boat -> oak boat + cannon |
| `cannon_raft_bamboo_salvaging_fd` | cannon raft -> bamboo raft + cannon |
| `dispenser_minecart_salvaging_fd` | dispenser minecart -> minecart + dispenser |

Nothing in the pack references any of them, so the only effect is the missing salvage routes and the red ERROR lines. **Supplementaries 3.8.8 shipped one broken in v1.6.2**, 3.8.10 added two more, and **3.9.6 added three more again** (the cannon boat, cannon raft and dispenser minecart rows) - so the count went three -> six on the v1.8.0 mod update, reversing part of the ERROR-line reduction the v1.7.0 notes tracked. The gating flags for the new three (`functional.cannon.cannon_boat`, `redstone.dispenser_minecart`) all default to `enabled = true`, so the conditions pass and the recipes are parsed and fail rather than being skipped.

Not caught by the update's dedicated-server boot test: that reads KubeJS's own "0 failed recipes" counter, which does not cover vanilla `RecipeManager` parse failures.

**Tracked as [#278](https://github.com/Flatts3000/sky-frogs/issues/278).** Found by the v1.7.0 launch test.

---

## Resolved

### 🟣 Iron Furnaces refused to accept Froglights at all until a restart (upstream bug, patched in PF)
**Symptom.** No Froglight would go into any Iron Furnaces furnace, by hand or by pipe, while a vanilla furnace took them fine. Restarting the game fixed it, until it came back. The pack's single most-reported problem: three CurseForge reporters in July 2026 alone (user_qqgd4audept0i3qy, Larronos, user_w647p447peuez0hl) on top of 28 Discord messages from 17 people over the pack's first two months, every one of whom was told to restart.

**Root cause.** `BlockIronFurnaceTileBase.hasRecipe` memoises smeltability in `ModSetup.HAS_RECIPE`, a **static `Map<Item, Boolean>`** that lives for the whole process:

```java
Item item = stack.getItem();
return ModSetup.HAS_RECIPE.computeIfAbsent(item, value -> ...isPresent());
```

`computeIfAbsent` means the first stack of an item ever tested decides the answer for every later stack of that item. Froglight smelting recipes match on the `slime_variant` **component**, so smeltability is a property of the component, not the item. A **variant-less** Froglight genuinely has no recipe, caches `false` against the Froglight item, and from that moment locks every variant out of every Iron Furnace until the process ends.

**Where the variant-less Froglights came from.** Mostly [#249](https://github.com/Flatts3000/sky-frogs/issues/249): Building Gadgets' Copy-Paste Gadget does not copy block-entity data, so pasted Froglights lose their variant. That issue was quietly the trigger for this one. The creative tab is the other source.

That explains every part of the report that made it look unfalsifiable - only Iron Furnaces furnaces affected, restarting fixes it, and it seems random because it depends entirely on which Froglight that session's furnace saw first.

**Fix.** **Productive Frogs 1.25.4**: component-carrying stacks bypass the cache and ask the recipe manager directly; everything else keeps Iron Furnaces' original cached path, so the optimisation survives and plain items are untouched. `compat.ironFurnacesRecipeCacheFix`. Pinned in pack v1.6.2. Same root cause as the entry below - item identity treated as item id - both documented in PF's [ironfurnaces_component_fixes.md](https://github.com/Flatts3000/productive-frogs/blob/mc-1.21.1/docs/ironfurnaces_component_fixes.md).

**Standing obligation.** Same as below: the patch fails open by design, so re-verify on any Iron Furnaces bump.

### 🟣 Iron Furnaces auto-split converted one Froglight variant into another (upstream bug, patched in PF)
**Symptom.** With **auto-split** on in a factory Iron Furnace, Froglights fed in from a drawer or network came out as a different variant. Reported by **abyssquidd** (#225, v1.4.3, Functional Storage drawer -> factory furnace) and, as "infinite froglight", by **millllehzh** (#220).

**Root cause.** `BlockIronFurnaceTileBase.split` levels the factory input slots by pooling every slot holding "the same item" and averaging the counts, and it decides "the same item" with `stackA.getItem() != stackB.getItem()` - item id only, never components. Every Froglight variant is the single id `productivefrogs:configurable_froglight` carrying its variant in a `slime_variant` component, so the furnace pooled variants that are not the same thing and wrote the averaged counts back into slots that each kept their own variant. 64 of one variant beside 1 of another became 32 and 33.

**The total count is conserved**, which is the whole reason it went unnoticed for months: it is not duplication, it is a silent 1:1 converter running unattended, from the cheapest Froglight a player can farm to the most expensive. Every other path in that class (auto-input, auto-output, internal insert) uses `isSameItemSameComponents` correctly; `split` is the outlier, and it is a regression of Iron Furnaces' own #147, which fixed the same behaviour for 1.19.2 NBT in 2023 before 1.21 replaced NBT with data components.

**Why it could not be fixed pack-side.** The corruption happens inside a block-entity tick. Iron Furnaces exposes no auto-split config, and the only lever a pack has is deleting the Factory augment (`ironfurnaces:augment_factory`), since `split` is only ever called inside the `isFactory()` branch - that removes the feature rather than the bug.

**Fix.** Upstream [Qelifern/IronFurnaces#229](https://github.com/Qelifern/IronFurnaces/issues/229) is open and unanswered with their last commit predating the report, so **Productive Frogs 1.25.3** ships a mixin that changes the one comparison and reproduces the rest of the algorithm exactly, so a furnace holding a single item type is unchanged. Applied only when `ironfurnaces` is loaded, non-fatal on failure, switchable via `compat.ironFurnacesAutoSplitFix`. Pinned in pack v1.6.2.

**Standing obligation.** The patch **fails open on purpose** - if a future Iron Furnaces reshapes `split`, it stops applying rather than crashing, which means a broken patch is silent. On any Iron Furnaces bump, check the log for `Applied the data-component fix to Iron Furnaces factory auto-split`. Its absence means unpatched. (PF `docs/ironfurnaces_component_fixes.md`.)

**Still open: #220's duplication face.** `split` conserves count, so it cannot produce "endless stacks with the drawer at 0". Either that report is this same conversion read as a dupe, or it is a separate defect in the storage layer's extraction of component items. Needs a repro before it can be closed.


### 🟢 "There is no skyblock/void world type to select" (it is already selected, since v1.6.0)

Reported on Discord by **Stay Sleep, Always Woke** (2026-09-01): "i went in and looked for the void/skyblock option when creating a world and its not there", after being told in-channel to select it. [#287](https://github.com/Flatts3000/sky-frogs/issues/287).

**There is nothing to select because it is already selected.** #251 (commit `1b351ef`, shipped in v1.6.0) remapped all five vanilla overworld presets to `skyblockbuilder:skyblock` via `pack/kubejs/data/minecraft/worldgen/world_preset/*.json`, and replaced the `minecraft:normal` world-preset tag so the picker holds a single entry. It was done because `level-type` in `server.properties` was a single point of failure that hosting panels rewrite. The client-side consequence, never spelled out at the time, is that the **World** tab's button already reads **`World Type: Skyblock`** and cycling it does nothing, because there is only the one entry.

So the standing support answer - "make sure you select sky block or void" - has been wrong since v1.6.0. It describes a choice that no longer exists, and a player who reads it as "find and click the skyblock option" finds a button they cannot change and concludes the install is broken.

**That button is the diagnostic**, and it is better than asking for a version. Screenshot the World tab:

- Reads **Skyblock** -> the worldgen override is loading correctly. Nothing is wrong with the install.
- Reads anything else (Default, Large Biomes, ...) -> the pack's `world_preset` overrides are not being applied at all, which narrows straight to cause 1 or 3 below and skips 2.

Verified on v1.8.0 (2026-09-01): the button reads `World Type: Skyblock` with `Customize` greyed out, and a fresh single-player world generates the skyblock.

**When terrain really does generate**, three causes, in this order:

1. **Pack older than v1.6.0.** The override does not exist there, so the button shows the vanilla list.
2. **A world created before updating.** Dimension generators are baked at world creation, so the override cannot repair an existing save. Needs a new world. Same caveat `worldgen.md` already carries for the End.
3. **Partial extraction** - the zero-byte-override case immediately below. Ask for `latest.log` and read the `Caused by:`.

A screenshot of the World tab plus whether the world is new separates all three in one answer: a non-Skyblock button rules out 2, and a Skyblock button rules out 1 and 3.

### 🟢 World creation crashes on the KubeJS biome modifiers (empty override files on the player's disk, not a pack defect)
R1shy reported (v1.5.3, Prism Launcher on Arch Linux, fresh install) that creating a world crashed with `Registry loading errors` on `productivefrogs:add_bog_slime_spawn`. [#242](https://github.com/Flatts3000/sky-frogs/issues/242). Kept here because the log signature is distinctive and this will be asked again.

**The tell.** All seven biome modifiers fail with the same `Caused by:` line:

```
java.lang.IllegalStateException: Not a JSON object: null
```

`null` is what Gson returns for an **empty stream**. So the file is being read as zero bytes. That is a different failure from a syntax error (which names a line and column), from an unknown registry key, and from a stale `kubejs/data` left by an in-place update - all three of which were plausible before the log arrived, and all three of which are wrong. KubeJS counted the files as present (`Validated 11 files in kubejs/assets/`, `Validated 19 files in kubejs/data/`, both matching the shipped pack exactly); they simply read back with nothing in them.

**Why it is not a KubeJS problem.** Three more places in the same log carry the identical signature, and the last one is outside `kubejs/` entirely:

1. All five Patchouli guide pages - `java.io.EOFException: End of input at line 1 column 1`, Gson's message for a literally empty file.
2. KubeJS `ClientAssetPacks.inject0` - `NullPointerException: Cannot invoke "com.google.gson.JsonObject.entrySet()" because "json" is null`, the same empty read, earlier in startup.
3. `SkyblockBuilder: Template with name default.nbt is incorrect.` from `config/skyblockbuilder/templates/islands/default.nbt`. A healthy instance logs `Loaded template "default" from "default.nbt"` instead - worth checking a known-good log to confirm the contrast, since that message is easy to mistake for noise.

Files across two separate override trees came out empty. That is interrupted or partial extraction at install time, and a full disk during install is the usual way it happens.

**Verifying the artifact, which is the step that actually settles it.** "Not reproducible on the dev instance" proves nothing here: that instance is junction-linked to the repo (see [`repo_layout.md`](./repo_layout.md)) and so **never exercises the exported zip**. Check the shipped file instead. For v1.5.3 the GitHub release asset and the CurseForge-hosted file were byte-identical (sha256 `8e9ebc57cb7f6d004f0521d90f29757365a33091a4f55f079113d6428a8338b8`; CurseForge is the copy Prism downloads), 194 entries, **zero** zero-byte files, all 25 JSONs parsed, and `default.nbt` was a valid gzipped NBT compound. The zip left clean and arrived with holes in it.

**Triage recipe.** Ask for the full `latest.log` and read the `Caused by:` - the pasted trace usually stops above it, and it is the only line that separates these four causes. If it says `Not a JSON object: null` or `End of input at line 1 column 1`, have the player run:

```sh
find <instance>/minecraft -type f -size 0
```

Zero-byte override files confirm it; the fix is deleting and reinstalling the instance rather than updating in place. If that command prints **nothing**, the files are intact on disk and something is serving them empty at runtime, which would be a real bug worth reopening for.

### 🟣 The Experience Singularity demanded books instead of the experience bottles the frog makes
Hunyol reported on Discord (v1.5.3) that the `experience` singularity takes books, "rather than bottles of enchanting as the name would suggest." [#245](https://github.com/Flatts3000/sky-frogs/issues/245).

**Ground truth.** The Experience Froglight smelts to `minecraft:experience_bottle` (`configurable_froglight_experience_to_experience_bottle.json` in `productivefrogs-1.25.2.jar`). The shipped singularity asked for `minecraft:book`.

**Root cause: two PF fields that agree everywhere except here.** `tools/gen_singularities.py` built every singularity's ingredient from the variant's `primer_item` - what you feed a slime to *make* that variant - on the assumption, stated in its own docstring, that the primer equals what the Froglight smelts to. Sweeping the pinned roster, that holds for all 58 vanilla variants but one:

| variant | `primer_item` | Froglight smelts to |
|---|---|---|
| experience | `minecraft:book` | `minecraft:experience_bottle` |

This is the **second** time the two fields have diverged. The first was chorus (see below): PF 1.8.1's Chorus Froglight smelted to *popped* chorus while the primer was raw, which broke the echo-shard chain and the chorus singularity, and PF fixed it upstream in 1.9.2. The entry for it called chorus "the **only** variant of all 70 where the froglight output differs from the `primer_item`" - true when written, and exactly the assumption that let this one through. `experience` arrived with PF 1.23.0 and the generator has been quietly wrong about it since.

**Why nothing else caught it.** `Q-SINGULARITY-INGREDIENT` was written to assert the same `primer_item` equality the generator produced, so it validated the generator against itself and could only ever agree. The quest copy was innocent: **Your First Singularity** already says "feed it the smelted ingots, not the Froglights," which is the correct law - the data was what disagreed with it.

**Player impact was mild.** Books are obtainable here (paper from sugar cane, leather from the Bog frog), so nobody was hard-blocked - it just made the Experience frog's own output useless toward its own singularity and quietly demanded a second production line.

**Fix shipped.** The generator and the validator both read the ingredient from PF's Froglight **smelting recipes** now, so the check has an independent source of truth instead of mirroring the generator. Both hard-error if a vanilla variant ever has zero or multiple smelt results rather than guessing. Regenerating moved exactly one file; the other 57 came out byte-identical, which is the proof the refactor is behavior-neutral.

**Verify in-game:** JEI the Experience Singularity - it should ask for 1,000 Bottles o' Enchanting.

### 🟣 Quest book contradicted itself on whether the Quantum Compressor consumes the Ultimate Catalyst
Hunyol reported on Discord (v1.5.3) that **The Ultimate Catalyst** and **The Long Compression** say opposite things about the catalyst, and that the former is the correct one. [#241](https://github.com/Flatts3000/sky-frogs/issues/241).

**Ground truth.** The catalyst is **not** consumed. Read from the pinned jar (`ExtendedCrafting-1.21.1-7.0.8`): `CompressorTileEntity.consumeInputs(int)` walks only the `inputs` list of `MaterialInput` records and decrements their counts; `process()` handles energy alone; nothing in `tick()` shrinks or clears the catalyst slot. `CompressorRecipe` holds the catalyst as a plain `Ingredient` used for matching. One catalyst per compressor, forever.

**Why the wrong claim spread.** It was asserted in four places at once, three of them player-facing: the two quest descriptions, the pack's Patchouli entry ("The catalyst is consumed each time"), and the singularities README. The [2026-06-11 editorial audit](./audits/quest_editorial_2026_06_11/the_ultimate_table.md) then marked it **MATCHES** on circular evidence - it cited a `defaultCatalyst` key in `extendedcrafting-common.toml` that **does not exist** in that file, and cited the pack README, which was itself the unverified claim. The same audit's `master_pond.md` recorded the *correct* fact ("reusable, not consumed - EC guide: 'does not get used up'") two files away, and the contradiction went unnoticed because the two chapters were audited separately.

**The lesson.** A "verified against the config" claim is only verified if the key is actually in the file - grep for it. And when a mechanic is described in more than one chapter, the audit has to reconcile the chapters against each other, not just each chapter against the jar. This one shipped for six weeks telling players to plan roughly 58 catalysts where one suffices.

**Fix shipped.** Corrected in all four places, and the stale audit row carries a dated correction rather than being rewritten.

**Verify in-game:** open the quest book at The Long Compression and Your First Singularity, and the Patchouli entry "The Singularity Endgame"; all three should describe a catalyst that stays in its slot.

### 🟣 Pack config overrides were not durable (tadpole growth back at PF's 20 min)
Sam Gomez reported on Discord (v1.5.2) that **Tadpole Growth Ticks read 24000** - Productive Frogs' own default, a 20 minute wait - where v1.4.4 had given him 3 minutes.

**What was NOT wrong.** The pack has always intended 3 minutes: `pack/config/productivefrogs-common.toml` sets `tadpoleGrowthTicks = 3600`, the fix for [#63](https://github.com/Flatts3000/sky-frogs/issues/63) ("first frogs take ~35 min"). Checked the shipped artifacts rather than the source: **v1.4.4, v1.5.0, v1.5.2 and v1.5.3 client zips all carry 3600**, and so does the v1.5.3 **server pack**. No release ever shipped 24000, and the value could not be reproduced on the dev instance running the same PF 1.25.2 jar. So this was never "every world is broken" - Sam's specific instance had lost the override, and the exact event that did it on his machine is still unknown.

**The real defect, which is structural.** Every pack config override lived only in `pack/config/`. That directory is **live per-instance state, written once at install**. NeoForge backs a config up to `<name>-N.toml.bak` and writes a fresh one whenever the existing file cannot be parsed or restored - the dev instance has five such backups from the 1.16 -> 1.24 era, as PF's config spec grew from 60 keys to 75. When that happens the pack's values are replaced by the mod's defaults, **nothing re-applies them, and nothing reports it**. The player silently gets different gameplay. `sync_instance.py` masks this locally by re-applying indexed config, which is why the dev instance always looked fine.

A false lead worth recording: the spec growing 60 -> 75 keys is *not* itself the trigger. NeoForge's `correct()` fills in missing keys while preserving existing values; only an unparseable/unrestorable file causes the backup-and-recreate. The newest `.bak` predates the 1.4.4 -> 1.5.2 window entirely, so whatever hit Sam was not that.

**Fix shipped.** Every FML-managed override now ships in **both** `pack/config/` and `pack/defaultconfigs/`. `defaultconfigs/` is the directory NeoForge seeds a missing config from - verified against the pinned loader (fancymodloader 4.0.43, NeoForge 21.1.244): `ConfigTracker` checks whether the config file exists and copies `defaultconfigs/<name>.toml` when it does not (`defaultConfigPath` + `Files.copy`), only generating from the mod's spec if no default is supplied. So a recreated config now comes back with the pack's values instead of the mod's.

Nine files are covered (`bcc-common`, `exdeorum-server`, `extendedcrafting-common`, `opolis_utilities`, `productivefrogs-common`, `solcarrot-server`, `sophisticatedbackpacks-server`, `toastcontrol-client`, `torchmaster`). `torchmaster.toml` and `opolis_utilities.toml` lack the `<modid>-<type>` naming convention but were confirmed to be FML-managed by finding the filename string in their own jars. `botanypots.json` is excluded and named explicitly in the script: it is not FML-managed, so `defaultconfigs/` is never consulted for it.

`tools/check_pack_configs.py` enforces byte-identity between the two copies (`--fix` syncs), gated by the `validate-pack` workflow. `release.yml` stamps the modpack version into **both** copies of `bcc-common.toml` and re-runs the check afterward, since only that file is rewritten at export time.

**Verify in-game:** delete `config/productivefrogs-common.toml` from an instance, launch, and confirm the regenerated file reads `tadpoleGrowthTicks = 3600` rather than 24000.

### 🟣 Grass Seeds and Mycelium Spores did nothing when used on dirt
Right-clicking dirt with **Grass Seeds** produced no grass block, and **Mycelium Spores** likewise produced no mycelium. Both simply did nothing, with no message. **Reported on Discord by Sam Gomez (v1.5.1).**

**Root cause (upstream, Ex Deorum 3.11).** 3.11 added four tags so pack authors could configure what each spore item spreads onto: `grass_seeds_spreadables`, `mycelium_spores_spreadables`, `warped_nylium_spores_spreadables`, `crimson_nylium_spores_spreadables`. The registration in `EItems` passed the **same constant, `CRIMSON_NYLIUM_SPORES_SPREADABLES`, to all four items** - a copy-paste slip. That tag contains `#c:netherracks` and `#minecraft:nylium`; the grass and mycelium tags contain `#minecraft:dirt`. So the two items whose whole purpose is converting dirt were checking a list dirt is not on, and their use silently no-opped.

Two details worth keeping:

1. **The warped/crimson half of the swap was harmless.** Those two were also pointed at each other, but both tags ship *identical* values (`#c:netherracks`, `#minecraft:nylium`), so behavior was unchanged. Only Grass Seeds and Mycelium Spores actually broke. A pack that customized those tags would have seen the swap; this one does not.
2. **This mattered more here than in most packs.** Grass Seeds drop from the builders' sieve (`builder_sieve.js`, 10%) and are the **only** grass-block source on a void skyblock. The pack also removes Ex Deorum's `grass_seeds -> moss_block` recipe (`mossy_cobblestone_gate.js`) to protect the Bog-tier mossy cobblestone gate, so the spread-onto-dirt use is the entire remaining point of the item.

**Fix (upstream, Ex Deorum 3.12; pinned in v1.5.3).** Two commits: [`4170f8b9`](https://github.com/thedarkcolour/ExDeorum/commit/4170f8b9) (#187) repointed Grass Seeds and Mycelium Spores at their own tags, and [`b489adba`](https://github.com/thedarkcolour/ExDeorum/commit/b489adba) (#188) un-swapped warped and crimson. Both ship in 3.12. Verified in the pinned jar rather than from the changelog: `EItems.class` now references all four distinct tag constants, where 3.11 referenced only the crimson one. No pack-side change was needed or made.

**Shipped broken in v1.4.4, v1.5.0, v1.5.1, and v1.5.2** - 3.11 was pinned by the mod-pin refresh in [#193](https://github.com/Flatts3000/sky-frogs/pull/193) and nothing in the pack exercised it, so four releases carried it.

**Verify in-game:** sieve until a Grass Seed drops, right-click a dirt block with it, and confirm the block turns to grass.

### 🟣 Take Flight described a jetpack build path Iron Jetpacks does not have
The chapter handed the player a **Basic Coil** and then asked for an **Iron Jetpack**, describing it as "the coil and strap plus an iron cell, thruster, and capacitor." Both halves were wrong, and neither is visible without reading the jar. **Reported on Discord by Hunyol (v1.5.2). Tracked in [#233](https://github.com/Flatts3000/sky-frogs/issues/233).**

**Root cause (the part worth keeping).** Iron Jetpacks generates its jetpack recipes in code (`DynamicRecipeManager`), not data, so nothing in the pack's config or KubeJS reveals the shape:

1. **Coils are assigned per tier by position, not by name.** `JetpackRegistry.getCoilForTier` computes `r = index(tier) / tierCount` over the **registered** tiers (creative's `-1` is excluded; disabled jetpacks are never registered), then `r > 0.75` -> Ultimate, `> 0.5` -> Elite, `> 0.25` -> Advanced, else Basic. The pack's 14 stock jetpacks give tiers `[0,1,2,3,4,5]`, so iron (tier 2) is `2/6 = 0.33` -> **Advanced coil (gold)**. Basic serves wood and stone/copper only. The coil is consumed by the **Cell** (`material + coil + redstone`), which builds the **Thruster** (`material + cell + furnace`) and **Capacitor** (`material + cell`); the jetpack recipe contains no coil at all.
2. **Only the lowest tier is craftable.** `makeJetpackRecipe` returns `null` unless `jetpack.tier == registry.getLowestTier()` (wood here). Every tier above is a `JetpackUpgradeRecipe` with `JetpackTierIngredient.of(tier - 1)` in the centre slot. The real ladder to an Iron Jetpack is **wood -> stone (or copper) -> iron**.

Nothing was broken in game: the Basic Coil crafts, the Iron Jetpack is obtainable via the real ladder, and no task was uncompletable. The defect was confined to the quest book.

**Fix (shipped in PR [#236](https://github.com/Flatts3000/sky-frogs/pull/236)):** copy only. "Off the Ground" now states the ladder and the gold coil the iron cells need; "Basic Coil" says what a coil is for and which tiers it covers; "Leather Strap" no longer claims everything bolts onto it (only the first jetpack uses one); "Advanced Coil" was reworded now that the iron tier already consumed one. No quests added, no config shipped. The alternative considered and declined was shipping `config/ironjetpacks/jetpacks/wood.json` with `"disable": true`, which shifts the mapping to Basic->iron / Advanced->gold / Elite->diamond / Ultimate->emerald and would have made the original copy true - rejected because it ships a config the pack does not carry and invalidates any wood jetpack in an existing save.

**Standing risk, now guarded.** Because the coil mapping is a ratio over the *registered* tier list, anything that adds or disables a jetpack tier - a new mod contributing an ingot tag, or a pack-side `disable` - silently re-maps which coil the iron jetpack needs and makes this copy wrong again. `validate_quests.py` grew **Q-JETPACK-COIL** for exactly that (see [`quest_testing.md`](./quest_testing.md)): it recomputes the ladder from `tools/ironjetpacks_tiers.py` and errors when any claim the chapter makes stops being true, naming the quest to fix. Verified to fail on the drift (disable `wood` and it reports all three broken claims) and pass on the shipped config. Skips with INFO where no jetpack config exists, so CI is unaffected.

**Verify in-game:** JEI on `ironjetpacks:jetpack` (iron variant) should show the upgrade grid with a stone or copper jetpack in the centre, and the iron cell should want a gold coil. The fix was written from the jar, not from a live check.

### 🟢 End portal won't open with 12 frames + eyes (Tier 6 gate redesigned to the End Cake)
The `road_to_void` gate asked players to hand-build a 12-frame End portal. A manually placed ring only lights when **every frame faces inward**, and a wrong-facing frame fails silently - the quest text documented the gotcha, but it still hard-blocked a player at the campaign's climax. **Reported on CurseForge by eager_goodall7 2026-06-05 (comment #8041724). Tracked in [#68](https://github.com/Flatts3000/sky-frogs/issues/68).**

**Fix (shipped in v0.4.0, playtested):** the gate is now Ex Deorum's **End Cake** (the ATM10SKY pattern) - bake it (milk-or-Slime-Milk x3 / eye-egg-eye / wheat x3; the default crushed-end-stone recipe is overridden since end stone is Void-frog-gated here), place it, take a bite, arrive on the obsidian platform. 6 slices per cake. The `kubejs:void/end_portal_frame` recipe is removed; "Frame the Void" became "Bake the End Cake"; the eyes quest dropped 12 -> 2. New `#productivefrogs:slime_milk_buckets` tag (`slime_milk_tags.js`) backs the "any Slime Milk" milk slot. **Workaround on pre-0.4.0 versions:** stand inside the 3x3 hole while placing each frame so it faces you, then socket all 12 eyes. Resolved.

### 🟢 Ultimate Singularity uncraftable: glow_ink_sac + obsidian had no slime recipe
The Ultimate Singularity demands all 40 vanilla froglight resources; `glow_ink_sac` and `obsidian` were the only two with no slime recipe AND no quest - the campaign capstone was unreachable. **Reported on CurseForge by eager_goodall7 2026-06-05 (comment #8042183). Tracked in [#79](https://github.com/Flatts3000/sky-frogs/issues/79).**

**Fix (shipped in v0.5.0):** Glow Ink joined the Cave chain before redstone (table + chamber recipes, quested in `cave_frogs`); obsidian joined the Infernal chain after netherrack (chamber-only, quested in `infernal_frogs`), enabled by PF **1.10.0** reclassing obsidian cave -> infernal (productive-frogs#142/#143). `validate_quests.py` grew **Q-SINGULARITY-COVERAGE** so the gap class cannot silently recur. A maintainer-playtest catch mid-build: the design pivot left stale obsidian rows in the Cave table chain (wrong tier, wrong category stamp) - purged before release; a full threading audit of every table pair, dissolution row, and tier sequence against PF 1.10.0 came back clean. Resolved.

### 🟢 Echo shard slime uncraftable: Chorus Froglight gives popped chorus (PF bug, fix upstream)
The echo shard slime dissolution recipe and the chorus Singularity both want raw `minecraft:chorus_fruit`, but PF's Chorus Froglight smelts to `minecraft:popped_chorus_fruit` - the **only** variant of all 70 where the froglight output differs from the `primer_item`. The frog loop therefore can't feed the echo shard step. **Reported on CurseForge by eager_goodall7 2026-06-05 (same comment, split per one-issue-per-problem). Tracked in [#69](https://github.com/Flatts3000/sky-frogs/issues/69), blocked-upstream.**

**Fix (shipped in v0.4.0, confirmed 2026-06-06):** PF **1.9.2** makes the Chorus Froglight smelt to raw chorus fruit (PF #139/#140); the pack pin moved 1.8.1 -> 1.9.2 in PR #70 and the existing chorus-keyed recipes (echo-shard dissolution row, chorus Singularity) were correct as-is. Maintainer confirmed done; #69 closed. **Workaround on pre-0.4.0 versions:** harvest chorus plants on the outer End islands for raw chorus fruit. Resolved.

### 🟢 Cave Slimes don't spawn on the starter island (SkyblockBuilder spawn protection)
The Tier 1 dark-room farm produces no Cave Slimes near the world-origin starter island. n3twoik found that running `/skyblock create` to make a new island (thousands of blocks out) made them spawn. **Reported on CurseForge by rerezcb + n3twoik 2026-06-04. Tracked in [#58](https://github.com/Flatts3000/sky-frogs/issues/58).**

**Root cause (diagnosed):** `cave_slime` is a MONSTER added to `minecraft:swamp` (the whole overworld is swamp), spawning by standard dark-room rules - nothing pack-side suppresses it, and the starter island is correctly swamp. But **SkyblockBuilder's spawn protection** (`config/skyblockbuilder/spawn.json5`) disables a list of `spawnProtectionEvents` within `spawnProtectionRadius` chunks of world origin, and that list includes **`mobs_spawn`**. The pack did not ship a `spawn.json5`, so players inherited SB's non-zero default radius - hostile spawns were suppressed around the starter island (a world rule, so an op singleplayer could still *build* the dark room there, just nothing spawned). `/skyblock create` islands are ~8192 blocks out, outside the radius, so they spawn fine. Confirmed: with `spawnProtectionRadius: 0`, Cave Slimes spawn at world origin (verified at ~0, 67, 2). **How ATM10SKY handles it:** it ships an explicit `spawn.json5` with `spawnProtectionRadius: 0` (plus the customization/inventory/permissions configs Sky Frogs also lacks).

**Fix (PR #59, pending playtest):** ship `config/skyblockbuilder/spawn.json5` with `spawnProtectionRadius: 0` (the starter island is the player's home on a per-player-island skyblock, so there's nothing to protect at spawn). Also corrected the stale `world.json5` comment (it credited Bog Slime via PF's default; the real spawner is the pack's cave_slime-in-swamp modifier). **Confirmed:** with `spawnProtectionRadius: 0`, Cave Slimes spawn on the starter island at world origin (verified at ~0, 67, 2); the shipped config delivers this to all players. Shipped in v0.2.2. Resolved.

**Audit (2026-06-04):** prompted by this being "a default we never overrode," compared the other SkyblockBuilder configs the pack runs on defaults (`customization`/`inventory`/`permissions`/`client`) against ATM10SKY's tuned versions. `customization`, `inventory`, and `permissions` are identical to ATM10SKY; `client` differs only by a cosmetic key (`removeCustomizeButton`); `inventory.json5` has `clearInitialInventory: false` (so the KubeJS first-join grant is safe). **`spawn.json5` was the only load-bearing gap** - no other SB config override is needed. (Residual: the pack runs these on SB defaults rather than pinning them, so a future SB version could drift a default; pinning is optional defensive hardening, deferred.)

### 🟢 Steel ingot quest demands the AlmostUnified-hidden `mekanism:ingot_steel`
The Mekanism chapter's **Steel** quest (`6ECA15000000000B`, task `6ECA15000000000C`) required the exact item `mekanism:ingot_steel`. But the pack runs **AlmostUnified** with `mod_priorities: [minecraft, alltheores, mekanism]` and `recipe_viewer_hiding: true` (`config/almostunified/unification/materials.json`): `c:ingots/steel` unifies to `alltheores:steel_ingot`, and Mekanism's steel recipe output is rewritten/hidden. So normal play only ever yields the All the Ores ingot - `mekanism:ingot_steel` is uncraftable except via `/give`, and the quest can't be completed without cheating. **Reported on CurseForge by `eager_goodall7` 2026-06-03. Tracked in [#51](https://github.com/Flatts3000/sky-frogs/issues/51).**

**Root cause (diagnosed):** the task pinned a mod-specific item id under tag unification. The downstream **Steel Casing** quest is unaffected - it needs `mekanism:steel_casing` (a Mekanism-unique block, obtainable since its recipe accepts unified steel as input).

**Final fix (on `fix/steel-quest-and-slime-infuser`):** the task now accepts `alltheores:steel_ingot` directly (a plain item task), and the quest icon was repointed there from the unobtainable `mekanism:ingot_steel`. Since AlmostUnified makes `alltheores:steel_ingot` the *only* craftable steel, a plain item task on that id is correct, self-labeling ("Steel Ingot"), and needs no filter mod. The quest description (infuse iron -> enriched iron -> smelt -> steel) stays accurate: AlmostUnified rewrites that recipe's *output* to the unified steel.

**How we got here (two corrected misdiagnoses during 2026-06-04 playtest):**
1. *First attempt* used a tag filter - `ftbfiltersystem:smart_filter` with `item_tag(c:ingots/steel)` - to accept any steel. It rendered as **"Missing Item"**: the `smart_filter` item is provided by the **FTB Filter System** mod, which the pack didn't ship (the format was borrowed from ATM10SKY without verifying the mod is present), and a `tools/validate_quests.py` exemption I'd added had suppressed the `Q-ITEM-EXISTS` signal that would have caught it. **Lesson:** never exempt `Q-ITEM-EXISTS` for an item without confirming the providing mod ships in *this* pack. Fixed the validator: filter items are no longer exempt from `Q-ITEM-EXISTS` (they must be in `item_ids.txt`; a filter item from an absent mod now errors), keeping only the `Q-MATCH-COMPONENTS` exemption (filter items match by expression, not `match_components`).
2. *Second attempt* added the FTB Filter System mod so `smart_filter` resolved - but the task then displayed as **"Smart Filter"** (the filter item's own name), meaningless to players. Rather than paper over it with a task title, switched to the plain `alltheores:steel_ingot` task above (simpler, self-labeling, no mod dependency). **Lesson:** when a quest needs a single, unified item, a plain item task beats a filter; reach for `smart_filter` only when you genuinely need a tag/OR set.

**FTB Filter System (`ftb-filter-system 21.1.4`) is kept** even though the steel quest no longer uses it - it backs smart filters for Modular Routers / AE2 and stays available for future tag-based tasks; the validator's filter-item support (`FILTER_ITEMS`, `is_filter_item`, the `Q-MATCH-COMPONENTS` exemption, `smart_filter` in `item_ids.txt`) stays forward-looking.

**Confirmed in-game 2026-06-04:** the Steel task displays **"Steel Ingot"** (AllTheOres) and accepts the unified steel ingot. Resolved.

### 🟢 Metallurgic Infuser won't accept a survival-obtained Iron Slime bucket (steel slime)
The optional **Steel Slime** quest (`6ECA150000000011`) needs the steel froglight, whose only source is the steel slime made in the Metallurgic Infuser (`steel_slime_infusing.js`; the Dissolution Chamber chain has no steel row). The recipe matched its iron-slime-bucket input with a `neoforge:components` ingredient requiring `bucket_entity_data == {Variant, Category}`. That is full-value compound equality, so it only matches a bucket whose NBT is *exactly* those two keys - true for a cheated/creative or crafted bootstrap bucket, but **not** for one obtained by catching a live slime: `MobBucketItem` dumps the entity's full save data (PF stat ints + age, per `ResourceFrog.addAdditionalSaveData`) into `bucket_entity_data`, so the compound no longer equals `{Variant, Category}` and the infuser silently refuses it. **Reported on CurseForge by `eager_goodall7` 2026-06-03; reproduced 2026-06-04 (a `/give` bucket processes, confirming the clean-vs-captured NBT split). Tracked in [#52](https://github.com/Flatts3000/sky-frogs/issues/52).**

**Root cause (diagnosed + decompiled):** this is exactly the component-keyed-machine-input trap the Dissolution Chamber design deliberately avoids (`dissolution_slime_recipes.js:24-29`); the steel script used the rejected approach and was never runtime-tested (held-for-playtest tier).

**Fix shipped (on `fix/steel-quest-and-slime-infuser`):** keyed the recipe off a plain item id instead - `productivefrogs:iron_slime_milk_bucket` + carbon -> steel slime bucket. The per-variant Slime Milk bucket (PF 1.8 split) has no component to match, so it works for every player and stays iron-specific (no steel-from-anything). Updated the quest description ("Iron Slime in a Bucket" -> "Bucket of Iron Slime Milk"). **Confirmed in-game 2026-06-04:** infusing a Bucket of Iron Slime Milk with carbon yields a Steel Slime bucket. Resolved.

### 🟢 Starter island spawns with a chest
SkyblockBuilder's built-in default island shipped a chest; Sky Frogs grants the first-launch kit via KubeJS instead. **Fix shipped (pending in-game verification):** the pack now ships a custom chestless starter island - `config/skyblockbuilder/templates.json5` plus a generated `default.nbt` (see [`tools/gen_starter_island.py`](../tools/gen_starter_island.py)) - replacing the built-in default. On first load, confirm the custom island loads, spawns the player correctly, and has no chest; then mark 🟢 and archive.

> Related, and a **corrected misdiagnosis**: an earlier note blamed SkyblockBuilder's default starter inventory for the extra hotbar torch/bucket and "fixed" it by emptying `config/skyblockbuilder/starter_inventory.json5`. The items still appear in-game (see "Torch + wooden watering can at world gen" below) - the real source is Ex Deorum. Emptying the SkyblockBuilder starter inventory is still worth keeping (prevents a separate stack), but it is not the fix for the torch/watering can.

### 🟢 Torch + wooden watering can granted at world gen
On first join in a fresh world the player spawns holding a **torch** and a **wooden watering can** (`exdeorum:wooden_watering_can`) next to the quest book. Neither belongs there - the first-launch grant is the quest book only. **Confirmed in-game 2026-05-26.**

**Root cause (diagnosed):** Ex Deorum's server config, not SkyblockBuilder. `exdeorum-server.toml`'s `[server]` section ships `starting_torch = true` and `starting_watering_can = true` ("Whether players in a void world start out with a torch / a full wooden watering can"); Ex Deorum grants them on its own. Ruled out: `first_join.js` grants only `ftbquests:book`, and `config/skyblockbuilder/starter_inventory.json5` is already `items: []`.

**Fix shipped (pending in-game verification):** the pack now ships `config/exdeorum-server.toml` with `[server] starting_torch = false` and `starting_watering_can = false` (minimal merge override - NeoForge fills the remaining `[server]` keys from defaults on load). Ex Deorum's `-server.toml` lives in `config/` in this NeoForge build (confirmed across several instances; no per-world `serverconfig/` copy), so the override applies to existing and new worlds on next launch. On a fresh world, confirm the player spawns holding only the quest book, then mark 🟢.

### 🟢 Welcome chapter branches show no dependency lines (orphaned quests)
In the Welcome chapter the intro spine draws its connecting lines, but the four branches (water / bed / cobble / frog-eggs) showed no lines between their stacked quests, and Wood to Stand On reported "No Dependants" in-game despite four quests listing it as a dependency. **Reported 2026-05-26, root cause found + fixed 2026-05-27.**

**Earlier misdiagnosis (corrected):** an initial pass concluded the chapter data was fine and this was just FTB Quests rendering locked-ahead lines dimly. That was wrong. The comparison against the SBR reference (`apophic_spawners.snbt`) checked the line-relevant *fields* but missed the distinguishing detail: SBR's quest IDs all lead with hex `0-7`, while our hand-authored branch IDs led with `8-F`.

**Root cause (diagnosed 2026-05-27 by diffing the deployed instance file against the repo):** FTB Quests parses object IDs (quest / task / reward / chapter) as **signed 64-bit longs** and only accepts positive values - i.e. a leading hex digit of `0-7`. The hand-authored branch IDs (`F9D9...` for Wood to Stand On, `A1B2...`, `B2C3...`, `C3D4...`, `D4E5...`, `E5F6...`) all lead with `8-F`, so they parse as **negative** longs. On world load FTB rejected them, assigned fresh positive IDs (e.g. `F9D9A7438B1DD129` -> `070AD3ED3E6F8AC0`), and **dropped every `dependencies: ["F9D9A7438B1DD129"]` reference** because that ID no longer resolved - severing the four branches and every quest below them. Confirmed by the perfect correlation: every ID FTB *kept* led with `0-7`, every ID it *regenerated* led with `8-F`.

**Fixed and verified in-game 2026-05-27.** Remapped all 62 negative-leading IDs in `pack/config/ftbquests/quests/chapters/welcome.snbt` into the positive range (leading digit minus 8: `8->0 ... F->7`), via [`tools/fix_quest_ids.py`](../tools/fix_quest_ids.py). The transform is per-ID-string and deterministic, so dependency references remap identically to the IDs they point at and stay linked; a collision guard aborts if any two IDs would converge. Diff was 79/79 symmetric (only ID lines changed; titles / descriptions / tasks / rewards untouched), all 17 dependency references resolve, and Wood to Stand On again has its 4 dependants. Confirmed in-game after `/ftbquests reload`: the four branches draw their dependency lines and Wood to Stand On lists 4 dependants. **Authoring rule going forward:** any hand-authored FTB Quests ID must lead with hex `0-7` (run `tools/fix_quest_ids.py` over a chapter to normalize).

### 🟢 No JEI recipe-transfer ("+"/"?") button in the Crafting Station
Viewing a recipe in JEI while the **Crafting Station** GUI is open shows no recipe-transfer button - the "+" (auto-fill) / "?" (transfer-status) icon JEI normally draws at the bottom-right of a recipe is absent. **Reported 2026-05-26.**

**Root cause (diagnosed):** JEI only draws that button when a recipe-transfer handler is registered for the open container. The pack ships the **base Crafting Station** (modId `craftingstation`, project-id 318551, pinned `craftingstation-neoforge-1.21.1-5.jar` - the newest 1.21.1 file of that project, which has no JEI variant). The JEI plugin + transfer handler live in a **separately distributed JEI-integrated build** of Crafting Station (still modId `craftingstation`; ships `tfar/craftingstation/jei/JeiClientPlugin` + `CraftingStationTransferHandler` and declares a `jei` dependency) - present in FTB OceanBlock 2 (`craftingstation-jei-neoforge-1.21.1-1.5.0.jar`) and Sky Bees Reborn (`craftingstationjei-1.21.1-NeoForge-2.1.1.jar`), both of which ship it alongside the base mod. Sky Frogs shipped only the base mod, so nothing registered the handler. (Confirmed via the CurseForge file list for project 318551 + decompiling the companion jars. One check left undone because the running game locked the instance jar: inspect the *deployed* `craftingstation-*.jar` for `tfar/craftingstation/jei/JeiClientPlugin` to be 100% sure the pinned build doesn't bundle it.)

**Impact: low.** Recipes are still fully viewable in JEI, and the Crafting Station's actual point - remembering the last recipe and pulling ingredients from adjacent inventories - works regardless. You just can't one-click auto-fill a recipe from JEI into the station; arrange manually, or use the vanilla grid / Crafting on a Stick for JEI transfer.

**Fix shipped (pending in-game verification):** swapped the base mod for **Crafting Station: J/EMI Edition Updated** (project-id 1127715, `craftingstationjei-1.21.1-NeoForge-2.1.1.jar`). Its modId is still `craftingstation`, so the quest #4 reward `craftingstation:crafting_station` resolves unchanged (verified the fork registers `block.craftingstation.crafting_station`). The fork's `JeiClientPlugin` registers the recipe-transfer handler, so JEI now draws the "+"/"?" button. Also added **Polymorph** (project-id 388800) - note it turned out to be an *optional* integration (the fork's jei/polymorph/craftingtweaks deps are all `type = "optional"`), kept for its recipe-conflict resolution; the transfer button itself works from JEI alone, which the pack already ships. On a fresh launch, open a recipe with the Crafting Station GUI and confirm the transfer button appears, then mark 🟢.

### 🟢 Duplicate ingots/dusts/etc. across mods (item unification)
Multiple mods ship their own copy of the same material - e.g. **osmium ingot/dust/nugget/raw** exist in both **ATO (All the Ores)** and **Mekanism**, and this multiplies as more tech mods are added. Left alone it means cluttered JEI, fragmented recipes (a recipe wants "an osmium ingot" but two distinct ones exist), and an inconsistent economy.

**Fix shipped (pending in-game verification):** **[Almost Unified](https://www.curseforge.com/minecraft/mc-mods/almostunified)** (`almostunified`, NeoForge 1.21.1 / 1.4.2) - the standard tag-based unifier, and what ATM10 runs for this exact ATO+Mekanism overlap. It collapses items sharing a `c:ingots/<material>` (etc.) tag to one canonical variant, hides the duplicates from the recipe viewer, and rewrites recipe outputs. Config lives at `pack/config/almostunified/` (ported from ATM10's verified 1.4.x schema, trimmed to our mod set):

- **Priority `minecraft > alltheores > mekanism`** - **All the Ores wins** for ingots/dusts/etc.; vanilla always wins for iron/gold/copper/redstone. When a future tech mod lands, append its id to the *end* of `mod_priorities` in `unification/materials.json` (so ATO/Mekanism keep winning) and add any new shared material names to `placeholders.json`.

**PF safety (verified against PF v1.2.0 source):** PF resolves a slime's variant by `primer_item` (exact id) **or** `primer_tag` (tag). All of PF's cross-mod variants - osmium included - use `primer_tag: c:ingots/<material>`, so whichever ingot AU keeps canonical still satisfies the tag and priming still matches. Vanilla variants (iron, gold, ...) use exact `primer_item` ids, but AU never unifies vanilla items, so there's no conflict. **Authoring rule:** any *pack-added* slime_variant for a modded resource must use `primer_tag`, never a mod-specific `primer_item`, or unification can break priming.

**Verify in-game:** set `dump_overview` / `dump_unification` true in `config/almostunified/debug.json` (AU writes this file on first boot), launch once, and confirm osmium collapses to `alltheores:osmium_*` and JEI shows a single variant; then flip the dumps back off. If Mekanism *machine* recipes still emit their own osmium ingot afterward, strip those recipe ids in KubeJS (the way ATM10 does in its `Unification/ingots.js`).

### 🟢 "Configurable Froglight" leaks into client-facing text
**Rule:** anything the player reads in-game must say **"Froglight"** (or "&lt;Material&gt; Froglight"), never "Configurable Froglight" - that's the internal/registry name, not a player-facing one.

The block item itself is already correct - PF's lang names it `Froglight` / `Iron Froglight` / etc. (`block.productivefrogs.configurable_froglight` and its variants). The phrase leaks in only through **descriptive strings**, and the fix splits by which repo owns each one:

**Upstream (Productive Frogs) - fixed at the source, no pack override.** PF's two JEI info strings (`productivefrogs.jei.variant_slime.info`, `productivefrogs.jei.frog.info`) read "...drops a Configurable Froglight stamped with [this/that] variant." Those are PF's own content and an internal inconsistency in PF (it already names the block "Froglight" everywhere else), so the fix belongs in the mod - tracked upstream in Productive Frogs' `docs/known_issues.md`. The pack inherits it on the next `packwiz update productive-frogs`. We deliberately do **not** ship a pack lang override: no point carrying a stopgap for a mod we own and are fixing at the source, and the pack isn't released yet. (If a test export ever needs it visibly correct before the next PF build, a temporary override of those two keys at `pack/kubejs/assets/productivefrogs/lang/en_us.json` is the stopgap - delete it once the PF fix ships.)

**Pack-authored - done.** Removed the phrase from the in-game quest text (`welcome.snbt`), the CurseForge page (`docs/curseforge_page.md`), the README hook, and the voice style guide's proper-noun list. The internal mechanics docs (`progression.md`, `worldgen.md`, `design_overview.md`, `kubejs_overrides.md`, `branding.md`, `quest_book.md`, `roadmap.md`, `backlog.md`) still use the descriptive phrase - left as-is (internal reference; sweep opportunistically).

**Resolved (2026-05-26):** the upstream PF fix shipped in **v1.4.0**, which the pack now pins. Verified the v1.4.0 jar's `en_us.json` has **no** "Configurable Froglight" in any client-facing value - the two JEI info strings (`jei.variant_slime.info`, `jei.frog.info`) now read "Froglight". The most visible leak (the JEI tooltip) is gone; nothing left pack-side.
