# Audit: road_to_void ("Road to the Void")

Mod(s) referenced: Productive Frogs (PF 1.20.0), Ex Deorum (End Cake), Industrial Foregoing (Dissolution Chamber), vanilla Minecraft. Generated chapter: no.

## Mechanic-claims ledger

| Quest | Claim (paraphrase) | Source checked (jar path / pack override) | Verdict |
|-------|--------------------|-------------------------------------------|---------|
| Pearls from the Dark | Endermen spawn in full darkness; gather 12 ender pearls | vanilla mob spawning; chapter task `item count:12 minecraft:ender_pearl` | MATCHES |
| Pearls from the Dark | 2 pearls -> Eyes of Ender, rest prime the Void Spawnery | PF `slime_variant/ender_pearl.json` `primer_item: minecraft:ender_pearl` | MATCHES (ender pearl is the void primer; exact spawnery pearl-cost not decompiled) |
| Eyes of Ender | 1 blaze rod -> 2 blaze powder; pearl + powder -> Eye of Ender | vanilla recipes; no pack override (grep `pack/kubejs` clean for ender_eye/blaze_powder recipe) | MATCHES |
| Eyes of Ender | task requires crafting 2 Eyes of Ender | chapter task `item count:2 minecraft:ender_eye` | MATCHES |
| Bake the End Cake | End Cake = 3 milk top / egg between 2 Eyes of Ender / 3 wheat | pack override `void_recipes.js` shaped `MMM/PEP/WWW`, M=milk OR `#productivefrogs:slime_milk_buckets`, P=ender_eye, E=`#c:eggs`, W=wheat | MATCHES |
| Bake the End Cake | plain Milk Buckets return empty buckets; Slime Milk consumed whole (bucket and all) | `void_recipes.js` comment + `startup_scripts/milk_bucket_no_remainder.js` clears slime-milk remainder pack-wide; vanilla milk keeps its bucket-return | MATCHES |
| Into the End | Eat the placed End Cake -> teleport to the End | `exdeorum` `EndCakeBlock.class` extends vanilla `CakeBlock`, `tryTeleport` via `EndPortalBlock` DimensionTransition to END | MATCHES |
| Into the End | "6 slices per cake" | `EndCakeBlock` uses vanilla `CakeBlock.BITES` (0..6); blockstate has bites=0..6 = **7 eats/teleports** per fresh cake | WRONG (off by one - 7, not 6). See note below. |
| | | | VERIFY: VERIFIED - javap confirms `EndCakeBlock extends net.minecraft.world.level.block.CakeBlock`, uses vanilla `BITES` IntegerProperty, eat logic `if_icmpge 6` (vanilla MAX_BITES). Fresh cake (bites=0) -> 7 eats/teleports before removal. Truth is **7**, not 6. (`void_recipes.js` header comment also says "6 slices = 6 trips" - same miscount, worth fixing too.) AFTER fix drops the number ("several trips") - safe; could instead assert "7". |
| Into the End | Land on an obsidian platform beside the central island | vanilla End spawn behavior (Ex Deorum does not override) | MATCHES |
| Slay the Dragon | Ender Dragon guards the central island; kill it | chapter task `kill minecraft:ender_dragon value:1` | MATCHES |
| Void Frogspawn | Ender pearl primes the Spawnery for Void slimes; raise a Void frog, turn in frogspawn bottle | PF `ender_pearl.json` primer; chapter task `item productivefrogs:frog_egg {contained_category:void}` | MATCHES (mechanic); item display name is "Bottle of Void Frog Eggs" not "...Frogspawn" - see terminology note |
| | | | VERIFY: VERIFIED - PF lang `item.productivefrogs.frog_egg.void` = "Bottle of Void Frog Eggs". "Bottle of Void Frog Frogspawn" is a pack-wide convention; correctly deferred to a single pack-wide pass, not diverged here. |
| A Bucket of Ender Pearl Slime | Dissolution Chamber: netherite scrap + soul soil filler -> Ender Pearl Slime in a Bucket | pack override `dissolution_slime_recipes.js` VOID row `['ender_pearl','minecraft:netherite_scrap']`, filler `minecraft:soul_soil` (x4) + 3 sweetslime + latex | MATCHES (resource + filler correct; sweetslime/latex omitted, acceptable simplification) |
| | | | VERIFY: VERIFIED - lines 124-125 `['VOID','minecraft:soul_soil', [['ender_pearl','minecraft:netherite_scrap']...`. PF lang `slime_bucket.ender_pearl` = "Bucket of Ender Pearl Slime". Item-name-inversion fix correct. |
| A Bucket of Ender Pearl Slime | by-hand path: prime a Void Slime with an ender pearl and catch it | PF `ender_pearl.json` `primer_item: minecraft:ender_pearl` | MATCHES |
| Milk It | Run the slime through the Slime Milker -> Bucket of Ender Pearl Slime Milk | PF item `ender_pearl_slime_milk_bucket` = "Bucket of Ender Pearl Slime Milk"; chapter task matches | MATCHES |
| First Ender Pearl | Feed the milk, take the Ender Pearl Froglight | PF block `configurable_froglight.ender_pearl` = "Ender Pearl Froglight"; chapter task `configurable_froglight {slime_variant: ender_pearl}` | MATCHES |
| Princess's Kiss | Dragon drops Princess's Kiss; right-click a frog -> becomes a plain unemployed villager, shower of particles | PF `PrincessKissHandler.convertToVillager` sets `VillagerData`/`VillagerType` (no profession), spawns `HAPPY_VILLAGER` particles; lang hint "Right-click a frog to turn it into a villager" | MATCHES |
| Princess's Kiss | Net a prize frog first; the Kiss works on any frog | PF handler targets any Frog entity (no variant gate) | MATCHES |

## Per-quest findings

### Pearls from the Dark (quest.601D000000000002)
- Disposition: CLEAN
- Mechanic, task, terminology, formatting, punctuation all verified. (Note: subtitle/desc use "Void Spawnery"; PF's block is just "Spawnery" but "Void Spawnery" reads as a descriptive phrase, not a wrong item name - acceptable.)

### Eyes of Ender (quest.601D000000000005)
- Disposition: CLEAN
- Blaze-rod-to-powder math and Eye recipe verified vanilla. Task count (2) matches prose.

### Bake the End Cake (quest.601D000000000008)
- Disposition: CLEAN
- Override recipe verified column-for-column. Milk-vs-Slime-Milk remainder asymmetry verified against `milk_bucket_no_remainder.js`. Strong, accurate quest.

### Into the End (quest.601D00000000000B)
- Disposition: EDIT
- Issues:
  - Factual accuracy: "&e6 slices&r per cake" is off by one. The End Cake extends vanilla `CakeBlock` (BITES 0..6), which yields **7 eats/teleports** per fresh cake, not 6. (The `void_recipes.js` header comment makes the same "6 slices = 6 trips" miscount.) Safest editorial fix: drop the exact count and let the existing "covers a few trips" hedge carry it - avoids asserting a number that contradicts vanilla cake mechanics. (Could not in-game count; flagging for the verify pass. If a maintainer confirms 7, state "7 trips".)
- BEFORE:
  ```
  "Set the &dEnd Cake&r down somewhere you trust and &etake a bite&r. Each slice teleports whoever eats it straight to the End - &e6 slices&r per cake, so one bake covers a few trips (or a team)."
  ```
- AFTER:
  ```
  "Set the &dEnd Cake&r down somewhere you trust and &etake a bite&r. Each bite teleports whoever eats it straight to the End, and one cake feeds &eseveral trips&r - enough for a few runs (or a team)."
  ```

### Slay the Dragon (quest.601D00000000000E)
- Disposition: CLEAN
- Kill task matches. Concise and accurate.

### Void Frogspawn (quest.601D000000000011)
- Disposition: CLEAN (with a cross-chapter terminology note, not a chapter-local fix)
- Note: prose says "Bottle of Void Frog Frogspawn"; the PF item display name is "Bottle of Void Frog Eggs". This "Frog Frogspawn" phrasing is a **pack-wide convention** (also in `welcome`/Cave and `road_to_tide` chapters), so it should be corrected pack-wide in one pass if at all, not diverged here. Logging for the orchestrator; no isolated AFTER to avoid creating inconsistency across chapters.

### A Bucket of Ender Pearl Slime (quest.601D000000000014)
- Disposition: EDIT
- Issues:
  - Terminology (minor): "Ender Pearl Slime in a Bucket" inverts the PF item name "Bucket of Ender Pearl Slime". The chapter title already uses the inverted form too, but the in-game item is "Bucket of Ender Pearl Slime". Aligning the desc to the real item name is low-cost and helps a player searching JEI.
- BEFORE:
  ```
  "Feed your &eDissolution Chamber&r &fnetherite scrap&r and &fsoul soil&r filler for an &5Ender Pearl Slime in a Bucket&r - the seed of the Void milk chain."
  ```
- AFTER:
  ```
  "Feed your &eDissolution Chamber&r &fnetherite scrap&r and &fsoul soil&r filler for a &5Bucket of Ender Pearl Slime&r - the seed of the Void milk chain."
  ```
- (Second paragraph "Prime a Void Slime with an ender pearl and catch it" is accurate and stays.)

### Milk It (quest.601D000000000017)
- Disposition: CLEAN
- Slime Milker -> "Bucket of Ender Pearl Slime Milk" verified against PF item name. One tight sentence; on-voice.

### First Ender Pearl (quest.601D00000000001A)
- Disposition: CLEAN
- "Ender Pearl Froglight" matches PF block name exactly; "Froglight" (not "Configurable Froglight") correct. Task component matches.

### Princess's Kiss (quest.601D00000000001D)
- Disposition: CLEAN
- Villager-conversion mechanic verified against `PrincessKissHandler` (sets VillagerData, no profession = unemployed; HAPPY_VILLAGER particles = "shower of particles"). "Any frog" claim correct. Drop-from-dragon gating correct. Warm and accurate.

## Chapter summary
- Quests: 10 total, 2 EDIT, 8 CLEAN
- Accuracy bugs (WRONG ledger rows): 1
  - "Into the End": "6 slices per cake" is off by one - End Cake is a vanilla CakeBlock (BITES 0..6 = 7 eats/teleports per fresh cake). Recommend dropping the exact number (verify pass should confirm 7 in-game before asserting it).
- Highest-severity finding: the End Cake slice/trip count (factual, MEDIUM) - it understates how many End trips one cake provides and the same miscount is echoed in the `void_recipes.js` comment. The other EDIT (item-name inversion in quest 0014) and the pack-wide "Frog Frogspawn" vs "Frog Eggs" terminology drift are both low severity.
