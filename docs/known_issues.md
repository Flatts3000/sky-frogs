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

> Related, and a **corrected misdiagnosis**: an earlier note blamed SkyblockBuilder's default starter inventory for the extra hotbar torch/bucket and "fixed" it by emptying `config/skyblockbuilder/starter_inventory.json5`. The items still appear in-game (see "Torch + wooden watering can at world gen" below) - the real source is Ex Deorum. Emptying the SkyblockBuilder starter inventory is still worth keeping (prevents a separate stack), but it is not the fix for the torch/watering can.

### 🔴 Torch + wooden watering can granted at world gen
On first join in a fresh world the player spawns holding a **torch** and a **wooden watering can** (`exdeorum:wooden_watering_can`) next to the quest book. Neither belongs there - the first-launch grant is the quest book only. **Confirmed in-game 2026-05-26.**

**Root cause (diagnosed):** Ex Deorum's server config, not SkyblockBuilder. `exdeorum-server.toml` ships `starting_torch = true` and `starting_watering_can = true` ("Whether players in a void world start out with a torch / a full wooden watering can"); Ex Deorum grants them on its own. Ruled out: `first_join.js` grants only `ftbquests:book`, and `config/skyblockbuilder/starter_inventory.json5` is already `items: []`.

**Proposed fix (not applied - documentation pass):** override both to `false`. `EConfig$Server` is a NeoForge SERVER-type config (confirmed from the jar), which normally seeds new worlds from `defaultconfigs/exdeorum-server.toml`. The deployed test instance, though, has the live file at `config/exdeorum-server.toml` with no per-world `serverconfig/` copy - so confirm which location actually takes effect and ship the override there. Affects fresh worlds only; existing saves keep their generated value.

### 🔴 Quest dependency lines missing between branch quests
In the Welcome chapter the intro spine draws its connecting lines, but the four branches (water / bed / cobble / frog-eggs) show no lines between their stacked quests in-game. **Reported 2026-05-26.**

**Diagnostic state:** structurally it looks correct - the chapter sets `default_hide_dependency_lines: false`, no quest carries a `hide_dependency_lines` flag, and every `dependencies` entry resolves to a real quest id (integrity-checked). Cause undetermined. Leading hypothesis: FTB Quests renders locked-quest dependency lines in a dim grey that is near-invisible against the dark book background (only the completed/unlocked path shows bright green), so this may be cosmetic rather than truly missing. Needs in-game investigation (compare a locked vs unlocked branch) before deciding if it is a real bug.

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

**Pack-authored - done.** Removed the phrase from the in-game quest text (`welcome.snbt`), the CurseForge page (`docs/curseforge_page.md`), the README hook, and the voice style guide's proper-noun list. The internal mechanics docs (`progression.md`, `worldgen.md`, `design_overview.md`, `kubejs_overrides.md`, `branding.md`, `quest_book.md`, `roadmap.md`, `backlog.md`) still use the descriptive phrase - left as-is (internal reference; sweep opportunistically). Stays 🔴 until the upstream PF JEI strings ship, since the in-game JEI tooltip is the most visible leak.
