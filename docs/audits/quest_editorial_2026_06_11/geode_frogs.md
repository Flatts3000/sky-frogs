# Audit: geode_frogs ("Geode Frogs")

Mod(s) referenced: Productive Frogs (productivefrogs-1.20.0.jar), Functional Storage (rewards only). Generated chapter: no.

## Mechanic-claims ledger

| Quest | Claim (paraphrase) | Source checked (jar path / pack override) | Verdict |
|-------|--------------------|-------------------------------------------|---------|
| Beyond Lapis | A Geode frog also yields amethyst, emerald, diamond after lapis | PF slime_variant data; geode_slime_chain.js chain lapis->tuff->calcite->amethyst->emerald->diamond | MATCHES |
| Tuff | Craft Tuff Slime in a Bucket from lapis milk + 4 gravel + 3 sweetslime + Geode frogspawn bottle | geode_slime_chain.js step ['lapis','tuff'] (4 gravel, 3 sweetslime, geode frog_egg) | MATCHES |
| Tuff | Smelt Tuff Froglight -> tuff | recipe configurable_froglight_tuff_to_tuff.json result minecraft:tuff | MATCHES |
| Calcite | Craft from tuff milk + 4 gravel + 3 sweetslime + Geode frogspawn bottle | geode_slime_chain.js step ['tuff','calcite'] | MATCHES |
| Calcite | Smelt Calcite Froglight -> calcite | recipe configurable_froglight_calcite_to_calcite.json result minecraft:calcite | MATCHES |
| Amethyst | Craft from calcite milk + 4 gravel + 3 sweetslime + Geode frogspawn bottle | geode_slime_chain.js step ['calcite','amethyst'] | MATCHES |
| Amethyst | Smelt Amethyst Froglight -> amethyst shard | recipe configurable_froglight_amethyst_to_amethyst_shard.json result minecraft:amethyst_shard | MATCHES |
| Emerald | Craft from amethyst milk + 4 gravel + 3 sweetslime + Geode frogspawn bottle | geode_slime_chain.js step ['amethyst','emerald'] | MATCHES |
| Emerald | Smelt Emerald Froglight -> emerald | recipe configurable_froglight_emerald_to_emerald.json result minecraft:emerald | MATCHES |
| Diamond | Craft from emerald milk + 4 gravel + 3 sweetslime + Geode frogspawn bottle | geode_slime_chain.js step ['emerald','diamond'] | MATCHES |
| Diamond | Smelt Diamond Froglight -> diamond | recipe configurable_froglight_diamond_to_diamond.json result minecraft:diamond | MATCHES |
| Count Catalyst | Craft = 2 sweetslime + bone meal; drop into placed Slime Milk pool | recipe count_catalyst.json (2 sweetslime + bone_meal, shapeless) | MATCHES |
| Count Catalyst | Buff saves to source, survives re-bucketing; Count is uncapped | jei.count_catalyst.info "saved to the source and survives re-bucketing... count is uncapped" | MATCHES |
| Count Catalyst | In-game item is named "Count Catalyst" | lang item.productivefrogs.count_catalyst = "Bountiful Catalyst" | WRONG - item display name is "Bountiful Catalyst" -- VERIFY: VERIFIED. PF jar lang `item.productivefrogs.count_catalyst` = "Bountiful Catalyst". Recipe count_catalyst (2 sweetslime + bone meal) + uncapped behavior confirmed. AFTER (title+body -> "Bountiful Catalyst") correct -- apply. |
| Speed Catalyst | Craft = 2 sweetslime + sugar; speeds spawns to a cap | recipe speed_catalyst.json (2 sweetslime + sugar); jei.speed_catalyst.info "up to a cap" | MATCHES |
| Speed Catalyst | In-game item is named "Speed Catalyst" | lang item.productivefrogs.speed_catalyst = "Rapid Catalyst" | WRONG - item display name is "Rapid Catalyst" -- VERIFY: VERIFIED. PF jar lang `item.productivefrogs.speed_catalyst` = "Rapid Catalyst". AFTER (title+body -> "Rapid Catalyst") correct -- apply. |
| Quantity Catalyst | Craft = 2 sweetslime + redstone (NOT glowstone); more slimes per spawn, to a cap | PACK OVERRIDE catalyst_recipes.js (redstone); jei.quantity_catalyst.info "another slime per spawn, up to a cap" | MATCHES (override correctly reflected) |
| Quantity Catalyst | In-game item is named "Quantity Catalyst" | lang item.productivefrogs.quantity_catalyst = "Teeming Catalyst" | WRONG - item display name is "Teeming Catalyst" -- VERIFY: VERIFIED. PF jar lang `item.productivefrogs.quantity_catalyst` = "Teeming Catalyst". Redstone recipe (pack catalyst_recipes.js override) correctly reflected. AFTER (title+body -> "Teeming Catalyst", keep redstone) correct -- apply. |
| Never Runs Dry | Ring 8 Count Catalysts around a diamond -> Infinite Count Catalyst; source never runs dry | recipe infinite_catalyst.json (BBB/BDB/BBB, B=count_catalyst, D=diamond); jei.infinite_catalyst.info "never run dry" | MATCHES (recipe shape) |
| Never Runs Dry | In-game item is named "Infinite Count Catalyst" | lang item.productivefrogs.infinite_catalyst = "Endless Catalyst" | WRONG - item display name is "Endless Catalyst" -- VERIFY: VERIFIED. PF jar lang `item.productivefrogs.infinite_catalyst` = "Endless Catalyst"; recipe infinite_catalyst = BBB/BDB/BBB, B=count_catalyst ("Bountiful Catalyst"), D=diamond -> infinite_catalyst. Both catalyst names in the quest are wrong. AFTER (8 Bountiful Catalysts -> Endless Catalyst) correct -- apply. |

## Per-quest findings

### Beyond Lapis (quest.6E0DE00000000002)
- Disposition: CLEAN
- Gateway quest. Accurate: the Geode frog does hold amethyst/emerald/diamond past lapis, and the chain runs to diamond. Voice is tight and warm. No issues.

### Tuff (quest.6E0DE0000000000E)
- Disposition: CLEAN
- Recipe (lapis milk + 4 gravel + 3 sweetslime + Geode frogspawn bottle), Froglight-check task, and smelt output (tuff) all verified. "Froglight" used correctly. No issues.

### Calcite (quest.6E0DE00000000011)
- Disposition: CLEAN
- Recipe (tuff milk + 4 gravel + 3 sweetslime + Geode frogspawn bottle) and smelt output (calcite) verified. No issues.

### Amethyst (quest.6E0DE00000000005)
- Disposition: CLEAN
- Recipe (calcite milk + 4 gravel + 3 sweetslime + Geode frogspawn bottle), full loop description, and smelt output (amethyst shard - correctly says "shard" not "amethyst") verified. No issues.

### Emerald (quest.6E0DE00000000008)
- Disposition: CLEAN
- Recipe (amethyst milk + 4 gravel + 3 sweetslime + Geode frogspawn bottle) and smelt output (emerald) verified. No issues.

### Diamond (quest.6E0DE0000000000B)
- Disposition: CLEAN
- Recipe (emerald milk + 4 gravel + 3 sweetslime + Geode frogspawn bottle) and smelt output (diamond) verified. "Cap of the gem chain" accurate. No issues.

### Count Catalyst (quest.6E0DE00000000014)
- Disposition: EDIT
- Issues: Terminology: the in-game item is **"Bountiful Catalyst"**, not "Count Catalyst" (`item.productivefrogs.count_catalyst = "Bountiful Catalyst"`). The title and the `&bCount Catalyst&r` reference in the body won't match what a player sees in JEI or their inventory. Recipe (2 sweetslime + bone meal) and behavior (uncapped, saves to source, survives re-bucketing) are accurate.
- Recommended fix: use the real display name as the primary noun while keeping the function clear. (If the pack prefers function-named titles, the alternative is a lang resourcepack override renaming the four catalysts - out of scope for this audit; flag for the maintainer to decide. The minimal text-only fix below names the real item.)
- BEFORE:
  - title: `"Count Catalyst"`
  - quest_subtitle: `"More slime per source."`
  - quest_desc line 1: `"Your Slime Milk sources don't have to run dry so fast. Craft a &bCount Catalyst&r (two &fsweetslime&r and a scoop of &fbone meal&r) and drop it straight into a placed &eSlime Milk&r pool."`
  - quest_desc line 3: `"The buff saves to the source - it even rides along if you bucket the source back up. Stack as many as you like; Count has no cap."`
- AFTER:
  - title: `"Bountiful Catalyst"`
  - quest_subtitle: `"More slime per source."`
  - quest_desc line 1: `"Your Slime Milk sources don't have to run dry so fast. Craft a &bBountiful Catalyst&r (two &fsweetslime&r and a scoop of &fbone meal&r) and drop it straight into a placed &eSlime Milk&r pool."`
  - quest_desc line 3: `"The buff saves to the source - it even rides along if you bucket the source back up. Stack as many as you like; this one has no cap."`

### Speed Catalyst (quest.6E0DE00000000017)
- Disposition: EDIT
- Issues: Terminology: the in-game item is **"Rapid Catalyst"**, not "Speed Catalyst" (`item.productivefrogs.speed_catalyst = "Rapid Catalyst"`). Recipe (2 sweetslime + sugar) and behavior (speeds spawns, climbs to a cap) are accurate.
- BEFORE:
  - title: `"Speed Catalyst"`
  - quest_desc line 1: `"A &bSpeed Catalyst&r (two &fsweetslime&r and &fsugar&r) makes a source spit slimes out faster. Toss it in the pool like the last one."`
  - quest_desc line 3: `"Speed climbs to a cap, so a few per source is plenty."`
- AFTER:
  - title: `"Rapid Catalyst"`
  - quest_desc line 1: `"A &bRapid Catalyst&r (two &fsweetslime&r and &fsugar&r) makes a source spit slimes out faster. Toss it in the pool like the last one."`
  - quest_desc line 3: `"Speed climbs to a cap, so a few per source is plenty."`

### Quantity Catalyst (quest.6E0DE0000000001A)
- Disposition: EDIT
- Issues: Terminology: the in-game item is **"Teeming Catalyst"**, not "Quantity Catalyst" (`item.productivefrogs.quantity_catalyst = "Teeming Catalyst"`). The recipe is correctly stated as redstone (pack override in catalyst_recipes.js - the jar default is glowstone, so the text already reflects the override correctly). Behavior (more slimes per spawn, climbs to a cap) accurate.
- BEFORE:
  - title: `"Quantity Catalyst"`
  - quest_desc line 1: `"A &bQuantity Catalyst&r (two &fsweetslime&r and &fredstone&r) makes a source spawn more slimes at once - more bodies per batch for your frogs to eat."`
- AFTER:
  - title: `"Teeming Catalyst"`
  - quest_desc line 1: `"A &bTeeming Catalyst&r (two &fsweetslime&r and &fredstone&r) makes a source spawn more slimes at once - more bodies per batch for your frogs to eat."`

### Never Runs Dry (quest.6E0DE0000000001D)
- Disposition: EDIT
- Issues: Terminology: this quest crafts the `infinite_catalyst`, whose in-game name is **"Endless Catalyst"**, not "Infinite Count Catalyst" (`item.productivefrogs.infinite_catalyst = "Endless Catalyst"`). It is also built from Count Catalysts, which in-game are "Bountiful Catalysts" - so both catalyst names in this quest are wrong. Recipe (ring 8 count_catalyst around a diamond) and behavior (never runs dry) accurate.
- BEFORE:
  - title: `"Never Runs Dry"`
  - quest_desc line 1: `"The big one. Ring eight &bCount Catalysts&r around a &fdiamond&r to forge an &bInfinite Count Catalyst&r, then drop it in: that source &enever runs dry&r again."`
- AFTER:
  - title: `"Never Runs Dry"`
  - quest_desc line 1: `"The big one. Ring eight &bBountiful Catalysts&r around a &fdiamond&r to forge an &bEndless Catalyst&r, then drop it in: that source &enever runs dry&r again."`

## Chapter summary
- Quests: 10 total, 4 EDIT, 6 CLEAN
- Accuracy bugs (WRONG ledger rows): 4 - all the same class (catalyst item display-name mismatch):
  1. Count Catalyst -> in-game "Bountiful Catalyst"
  2. Speed Catalyst -> in-game "Rapid Catalyst"
  3. Quantity Catalyst -> in-game "Teeming Catalyst"
  4. Infinite Count Catalyst -> in-game "Endless Catalyst" (and its Count-Catalyst ingredient = "Bountiful Catalyst")
- Highest-severity finding: All four Slime Milk catalysts are referenced by descriptive function-names ("Count/Speed/Quantity/Infinite Count Catalyst") that do not match PF v1.20.0's actual display names (Bountiful/Rapid/Teeming/Endless Catalyst). A player following the quest text cannot find these items by name in JEI or their inventory. Note for maintainer: the cross-chapter alternative is a pack lang resourcepack override restoring function-named display names (the descriptive names are arguably clearer for new players) - that is a design call outside this audit's text-only scope; the AFTERs above take the minimal path of matching the real in-game names.
- Note: the gem chain (Tuff/Calcite/Amethyst/Emerald/Diamond) and Beyond Lapis are fully accurate - recipes, threading order, smelt outputs, and Froglight-check law all verified against the jar and geode_slime_chain.js. The Quantity catalyst's redstone recipe (pack override) is correctly reflected in the text. Color codes balanced, no em/en dashes, "Froglight" used throughout (never "Configurable Froglight").
