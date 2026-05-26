# Known Issues

Living tracker of Sky Frogs playtest bugs, limitations, and accepted-for-now quirks. Open *design questions* and deferred features live in [backlog.md](./backlog.md); this doc is for things observed in-game.

## Status legend

| Symbol | Meaning |
|---|---|
| 🔴 | Open. Fix pending. |
| 🟡 | Open. Workaround available. |
| 🔵 | Accepted for now. Low priority; may revisit. |
| 🟢 | Resolved. |

---

## Open

### 🔵 Starter island spawns with a chest
SkyblockBuilder's built-in default island shipped a chest; Sky Frogs grants the first-launch kit via KubeJS instead. **Fix shipped (pending in-game verification):** the pack now ships a custom chestless starter island - `config/skyblockbuilder/templates.json5` plus a generated `default.nbt` (see [`tools/gen_starter_island.py`](../tools/gen_starter_island.py)) - replacing the built-in default. On first load, confirm the custom island loads, spawns the player correctly, and has no chest; then mark 🟢 and archive.

> Related and already fixed: the extra hotbar starter items (torch, bucket) were SkyblockBuilder's *default starter inventory* stacking on top of our grant. Emptied via `config/skyblockbuilder/starter_inventory.json5`.

### 🔴 Duplicate ingots/dusts/etc. across mods (need item unification)
Multiple mods ship their own copy of the same material - e.g. **osmium ingot/dust/nugget/raw/rod** exist in both **ATO (All the Ores)** and **Mekanism**, and this multiplies as more tech mods are added. Result: cluttered JEI, fragmented recipes (a recipe wants "an osmium ingot" but two distinct ones exist), and an inconsistent economy.

**Fix (researched):** tag-based unification via **[Almost Unified](https://www.curseforge.com/minecraft/mc-mods/almostunified)** (`almostunified`) - the standard solution, and what ATM10 / ATM10SKY use for this exact ATO+Mekanism overlap. It collapses items sharing a `c:ingots/<material>` (etc.) tag to a single preferred variant, hides the duplicates from JEI, and rewrites recipe outputs to the preferred item. A configurable mod-priority list decides which variant wins. (Per-mod add-ons exist, e.g. AU: Immersive Engineering.)

**Decide before adding it:**
1. **Mod priority** - which variant is canonical per material (e.g. prefer Mekanism's osmium over ATO's, or vice versa).
2. **PF slime-variant interaction (important).** PF infusion matches a variant's `primer_item`. If a variant's primer is an exact item id (e.g. `mekanism:ingot_osmium`) and unification makes ATO's ingot the canonical one the player ends up holding, infusion could silently fail. Confirm whether PF variant primers use an item *tag* (unification-safe) or an exact id, and align the priority so the frog-farmable primer matches the unified item.

Hold off on adding Almost Unified until priority + the PF-primer interaction are settled.
