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

### 🟣 Starter island spawns with a chest
SkyblockBuilder's built-in default island shipped a chest; Sky Frogs grants the first-launch kit via KubeJS instead. **Fix shipped (pending in-game verification):** the pack now ships a custom chestless starter island - `config/skyblockbuilder/templates.json5` plus a generated `default.nbt` (see [`tools/gen_starter_island.py`](../tools/gen_starter_island.py)) - replacing the built-in default. On first load, confirm the custom island loads, spawns the player correctly, and has no chest; then mark 🟢 and archive.

> Related and already fixed: the extra hotbar starter items (torch, bucket) were SkyblockBuilder's *default starter inventory* stacking on top of our grant. Emptied via `config/skyblockbuilder/starter_inventory.json5`.

### 🟣 Duplicate ingots/dusts/etc. across mods (item unification)
Multiple mods ship their own copy of the same material - e.g. **osmium ingot/dust/nugget/raw** exist in both **ATO (All the Ores)** and **Mekanism**, and this multiplies as more tech mods are added. Left alone it means cluttered JEI, fragmented recipes (a recipe wants "an osmium ingot" but two distinct ones exist), and an inconsistent economy.

**Fix shipped (pending in-game verification):** **[Almost Unified](https://www.curseforge.com/minecraft/mc-mods/almostunified)** (`almostunified`, NeoForge 1.21.1 / 1.4.2) - the standard tag-based unifier, and what ATM10 runs for this exact ATO+Mekanism overlap. It collapses items sharing a `c:ingots/<material>` (etc.) tag to one canonical variant, hides the duplicates from the recipe viewer, and rewrites recipe outputs. Config lives at `pack/config/almostunified/` (ported from ATM10's verified 1.4.x schema, trimmed to our mod set):

- **Priority `minecraft > alltheores > mekanism`** - **All the Ores wins** for ingots/dusts/etc.; vanilla always wins for iron/gold/copper/redstone. When a future tech mod lands, append its id to the *end* of `mod_priorities` in `unification/materials.json` (so ATO/Mekanism keep winning) and add any new shared material names to `placeholders.json`.

**PF safety (verified against PF v1.2.0 source):** PF resolves a slime's variant by `primer_item` (exact id) **or** `primer_tag` (tag). All of PF's cross-mod variants - osmium included - use `primer_tag: c:ingots/<material>`, so whichever ingot AU keeps canonical still satisfies the tag and priming still matches. Vanilla variants (iron, gold, ...) use exact `primer_item` ids, but AU never unifies vanilla items, so there's no conflict. **Authoring rule:** any *pack-added* slime_variant for a modded resource must use `primer_tag`, never a mod-specific `primer_item`, or unification can break priming.

**Verify in-game:** set `dump_overview` / `dump_unification` true in `config/almostunified/debug.json` (AU writes this file on first boot), launch once, and confirm osmium collapses to `alltheores:osmium_*` and JEI shows a single variant; then flip the dumps back off. If Mekanism *machine* recipes still emit their own osmium ingot afterward, strip those recipe ids in KubeJS (the way ATM10 does in its `Unification/ingots.js`).

### 🔴 "Configurable Froglight" leaks into client-facing text
**Rule:** anything the player reads in-game must say **"Froglight"** (or "&lt;Material&gt; Froglight"), never "Configurable Froglight" - that's the internal/registry name, not a player-facing one.

The block item itself is already correct - PF's lang names it `Froglight` / `Iron Froglight` / etc. (`block.productivefrogs.configurable_froglight` and its variants). The phrase leaks in only through **descriptive strings**, and the fix splits by which repo owns each one:

**Upstream (Productive Frogs) - fixed at the source, no pack override.** PF's two JEI info strings (`productivefrogs.jei.variant_slime.info`, `productivefrogs.jei.frog.info`) read "...drops a Configurable Froglight stamped with [this/that] variant." Those are PF's own content and an internal inconsistency in PF (it already names the block "Froglight" everywhere else), so the fix belongs in the mod - tracked upstream in Productive Frogs' `docs/known_issues.md`. The pack inherits it on the next `packwiz update productive-frogs`. We deliberately do **not** ship a pack lang override: no point carrying a stopgap for a mod we own and are fixing at the source, and the pack isn't released yet. (If a test export ever needs it visibly correct before the next PF build, a temporary override of those two keys at `pack/kubejs/assets/productivefrogs/lang/en_us.json` is the stopgap - delete it once the PF fix ships.)

**Pack-authored - fixed here.** Edit `config/ftbquests/quests/chapters/welcome.snbt` (quest "Frogs, Not Pickaxes"): "&eConfigurable Froglight&r" -> "&eFroglight&r". Then sweep the CurseForge page (`docs/curseforge_page.md`) for the phrase. Dev docs (`progression.md`, `worldgen.md`) are internal - fix opportunistically.
