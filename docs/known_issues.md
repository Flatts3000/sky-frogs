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

---

## Open

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

**Fixed and verified in-game 2026-05-27.** Remapped all 62 negative-leading IDs in `pack/config/ftbquests/quests/chapters/welcome.snbt` into the positive range (leading digit minus 8: `8->0 ... F->7`), via [`tools/fix_quest_ids.py`](../../tools/fix_quest_ids.py). The transform is per-ID-string and deterministic, so dependency references remap identically to the IDs they point at and stay linked; a collision guard aborts if any two IDs would converge. Diff was 79/79 symmetric (only ID lines changed; titles / descriptions / tasks / rewards untouched), all 17 dependency references resolve, and Wood to Stand On again has its 4 dependants. Confirmed in-game after `/ftbquests reload`: the four branches draw their dependency lines and Wood to Stand On lists 4 dependants. **Authoring rule going forward:** any hand-authored FTB Quests ID must lead with hex `0-7` (run `tools/fix_quest_ids.py` over a chapter to normalize).

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
