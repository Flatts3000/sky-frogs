# FTB Quests Reference

> Capability reference for the FTB Quests mod as shipped in this pack:
> **`ftb-quests-neoforge-2101.1.24`** (Minecraft 1.21.1 / NeoForge, SNBT-based quest files).
> Verified three ways: the mod jar's task/reward classes (the authoritative type list for our
> version), the FTB-Quests source + FTB docs, and this pack's own working quest files. Where a
> field is version-sensitive or unconfirmed, it's flagged. Author quests in SNBT (or the in-game
> editor); use this as the "what's possible and how does it serialize" map.

Related: [`quest_testing.md`](./quest_testing.md) (the validator that encodes the load-bearing
rules below), [`quest_book.md`](./quest_book.md) (this pack's chapter plan).

---

## 1. File layout: `pack/config/ftbquests/quests/`

```
quests/
  data.snbt              # questbook-wide settings (one object)
  chapter_groups.snbt    # ordered list of chapter-group IDs (titles go to lang)
  chapters/<name>.snbt   # one file per chapter; `filename` must match the file name
  reward_tables/<n>.snbt # one file per reward table / loot crate
  lang/en_us.snbt        # ALL titles/subtitles/descriptions, keyed by object ID
```

**Edit STRUCTURE in chapter files, TEXT in `lang/en_us.snbt`.** On world load FTB extracts all
human-readable text out of the chapters into the lang file (keyed by ID) and wipes inline text
from the chapter. Inline `title`/`description` in a chapter file will not render and gets removed
on the next save. (See section 9.)

**Windows/LF note for this pack:** FTB rewrites snbt to CRLF on world load. Always run
`python tools/pack_refresh.py` (not bare `packwiz refresh`) so the index records the LF hashes the
committed blobs actually have.

---

## 2. `data.snbt` (questbook-wide settings)

```snbt
{
    default_quest_shape: "circle"          # default node shape
    default_consume_items: false           # default for item tasks
    default_autoclaim_rewards: "disabled"  # disabled | enabled | invisible
    default_reward_team: false             # rewards granted per-team vs per-player
    progression_mode: "linear"             # "linear" (deps gate) | "flexible" (free)
    detection_delay: 20                     # ticks between inventory auto-detection passes
    pause_game: false
    drop_book_on_death: false
    grid_scale: 0.5d
    show_lock_icons: false
    fallback_locale: "en_us"
    version: 13
}
```

Notable: `progression_mode` `"linear"` means dependencies gate access; `"flexible"` (free) makes
every quest startable anytime. `default_consume_items` is the fallback for item tasks that don't
set `consume_items` themselves.

---

## 3. `chapter_groups.snbt`

```snbt
{
    chapter_groups: [
        { id: "0C4F0E0000000001" }
        { id: "0C4F0E0000000002" }
    ]
}
```

Display order of the sidebar groups = list order here. Group **titles** are NOT here - they're in
lang as `chapter_group.<id>.title`. A chapter joins a group via its `group` field; `group: ""`
is the implicit ungrouped/default group (renders first - this pack's `welcome.snbt` uses it).

---

## 4. Chapter object

```snbt
{
    id: "7CA7E000C0DE0001"
    filename: "cave_frogs"            # MUST equal the .snbt file name
    group: "0C4F0E0000000001"         # chapter-group id; "" = default
    order_index: 2                    # position within the group (lower = earlier)
    icon: { id: "minecraft:copper_ingot" }
    autofocus_id: "7CA7E000C0DE0002"  # quest the book centers on when opened
    default_quest_shape: ""           # "" = inherit from data.snbt
    default_hide_dependency_lines: false
    quest_links: [ ]
    quests: [ ... ]
}
```

| Field | Meaning |
|---|---|
| `id` | chapter id (16-hex positive long - see section 8) |
| `filename` | base filename; must match the `.snbt` name |
| `group` | chapter-group id; `""` = ungrouped |
| `order_index` | position within the group |
| `icon` | `{ id: "..." }` (item), or an entity/image form |
| `autofocus_id` | quest the view auto-centers on |
| `default_quest_shape` / `default_quest_size` | per-chapter defaults (`""` / `0` inherit) |
| `default_hide_dependency_lines` | hide dep lines by default |
| `quests[]` | quest objects |
| `quest_links[]` | ghost-copies of quests from other chapters (section 10) |
| `images[]` | decorative/interactive canvas overlays (section 10) |
| `progression_mode` | per-chapter override of linear/flexible |
| `always_invisible` | hide the whole chapter |

Title lives in lang as `chapter.<id>.title`.

---

## 5. Quest object

```snbt
{
    id: "7CA7E000C0DE0005"
    x: 0.0d
    y: 1.5d
    shape: "hexagon"                  # "" inherits chapter default
    size: 1.5d                        # 0 = chapter default
    icon: { id: "minecraft:copper_ingot" }
    dependencies: ["7CA7E000C0DE0002"]
    optional: true
    tasks: [ ... ]
    rewards: [ ... ]
}
```

| Field | Meaning |
|---|---|
| `id` | quest id (positive long) |
| `x`, `y` | canvas position (doubles; this pack spaces nodes 1.5 apart) |
| `shape` | `circle` `square` `hexagon` `diamond` `octagon` `pentagon` `gear` `heart` ... (`""` inherits) |
| `size` | icon scale; `0` = chapter default; `1.5d` is this pack's "milestone" size |
| `icon` | display icon; if omitted FTB derives one from a task/reward |
| `dependencies[]` | prerequisite object ids (usually quests; ids resolve GLOBALLY, so cross-chapter deps work and are how tier-gating works here) |
| `dependency_requirement` | `all_completed` (default), `one_completed`, `all_started`, `one_started` |
| `min_required_dependencies` | "N of the listed M" (0 = use the requirement above) |
| `hide_dependency_lines` / `hide_dependent_lines` | suppress drawn lines in/out |
| `hide_until_deps_visible` / `hide_until_deps_complete` | fully hide (vs the default "locked + padlock") until deps are visible/complete |
| `invisible` | always hidden (scripted/secret quests) |
| `optional` | doesn't block chapter completion; deps treat it as satisfiable |
| `can_repeat` / `repeat_cooldown` | repeatable quest + cooldown (ticks) |
| `require_sequential_tasks` | tasks must complete in listed order |
| `subtitle` / `description` | live in lang (`quest.<id>.quest_subtitle` / `.quest_desc`) |
| `tasks[]` / `rewards[]` | see sections 6 and 7 |

**Lock vs hide:** until deps are met a quest is *locked* (visible, padlock, unstartable). The
`hide_until_deps_*` flags make it fully invisible instead. `invisible: true` hides unconditionally.

---

## 6. Task types (complete, from the jar)

Every task has `id` and `type`. The complete usable `type` set in our jar:

| `type` | Purpose | Key fields |
|---|---|---|
| `item` | Submit/hold an item | `item` (ItemStack or `{ tag: "..." }`), `count` (long), `consume_items`, `only_from_crafting`, `match_components`, `task_screen_only` - see below |
| `checkmark` | Manual "click to complete" | none (title in lang) |
| `advancement` | Earn an advancement | `advancement` (id), `criterion` (`""` = whole advancement) |
| `dimension` | Enter a dimension | `dimension` (e.g. `minecraft:the_nether`) |
| `biome` | Stand in a biome | `biome` |
| `stat` | Reach a vanilla stat value | `stat`, `value` (int) |
| `kill` | Kill N of an entity | `entity` and/or `entity_type_tag`, `value` (count) |
| `location` | Be inside a region | `dimension`, `ignore_dimension`, `position` (x,y,z), `size` (w,h,d) |
| `observation` | Look at a target | `observe_type` (block / block_tag / block_state / entity_type / entity_type_tag), `to_observe`, `timer` (ticks) |
| `fluid` | Submit a fluid | `fluid`, `amount` (mB, default 1000) |
| `energy` / `forge_energy` | Submit FE | `value` (long), `max_input` (per-tick cap) |
| `xp` | Spend/hold XP | `value` (int), `points` (bool - true=points, false=levels) |
| `stage` | Have a game stage | `stage`, `team_stage` (bool) |
| `structure` | Be inside a structure | `structure` (id/tag) |
| `custom` | KubeJS-driven | `id` matched in `FTBQuestsEvents.customTask` (section 11) |

### The ITEM task and component matching (the one that bites)

```snbt
tasks: [{
    id: "7CA7E000C0DE0006"
    type: "item"
    item: { components: { "productivefrogs:slime_variant": "productivefrogs:copper" }, count: 1, id: "productivefrogs:configurable_froglight" }
    match_components: "strict"
}]
```

**`match_components` controls how data components on the filter are compared.** This is the single
most important FTB Quests fact for this pack, and getting it wrong is silent:

| `match_components` | Behavior | Use when |
|---|---|---|
| absent / `""` | **Item id only; components IGNORED.** ANY stack of that item completes the task. | the item has no discriminating component (a plain `minecraft:torch`), OR you deliberately want any variant |
| `"strict"` | Submitted stack's components must match the filter **exactly** (no extra components). | the real item carries ONLY the discriminating component - e.g. a dropped **Froglight** has just `slime_variant` |
| `"fuzzy"` | Submitted stack must **contain** the filter's components (extra components allowed). | the real item carries the discriminating component PLUS others - e.g. an **Iron Jetpack** has `jetpack_id` plus live energy/engine/hover state components |

**The trap:** a task that *specifies* a `components` filter but *omits* `match_components` matches
by id only - so one Copper Froglight completed every Cave-tier resource quest (they were all
`configurable_froglight` with different `slime_variant`, and the component was ignored). This pack
adds `match_components` to all 32 component-discriminated tasks; the validator's `Q-MATCH-COMPONENTS`
check enforces it forever.

**Strict vs fuzzy, concretely:**
- **Froglight -> strict.** A frog-dropped `configurable_froglight` carries only
  `productivefrogs:slime_variant`. Strict pins it exactly; a different variant can't satisfy it.
- **Iron Jetpack -> fuzzy.** `ironjetpacks:jetpack` stores its tier in `ironjetpacks:jetpack_id`
  but a real one also carries `jetpack_energy`/`jetpack_engine`/`jetpack_hover`/`jetpack_throttle`/
  `jetpack_hud`. Strict would demand an exact set and never match a crafted jetpack; fuzzy requires
  it to *contain* `jetpack_id = ironjetpacks:iron` while tolerating the state, and still rejects a
  gold jetpack. Setting a component on an item also fixes its DISPLAY (a bare `ironjetpacks:jetpack`
  renders as the null "Undefined Jetpack").

**Other item-task fields:**
- `count` - total required (serialized as a long, e.g. `count: 16L`; `count: 1` may render without the `L`).
- `consume_items` (tristate) - take items on submit, vs just hold them. Absent = `data.snbt` default.
- `only_from_crafting` (tristate) - only count items obtained by crafting.
- `task_screen_only` (bool) - only submittable via the quest GUI, not auto-detected from inventory.
- **Tag form:** `item: { tag: "c:ingots/iron", count: 1 }` matches any item in the tag (mutually exclusive with an `id`).

---

## 7. Reward types (complete, from the jar)

Every reward has `id` and `type`. The complete set in our jar:

| `type` | Purpose | Key fields |
|---|---|---|
| `item` | Give an item | `item` (stack template, usually `count: 1`), `count` (how many to give), `random_bonus` (extra 0..N) |
| `xp` | Give XP points | `xp` (int) |
| `xp_levels` | Give XP levels | `xp_levels` (int) |
| `loot` / `random` | Roll a reward table (random) | `table_id` (-> a `reward_tables/` entry) or inline `table_data` |
| `choice` | Player picks one of a table's entries | `table_id` / `table_data` |
| `all_table` | Grant ALL of a table's entries | `table_id` / `table_data` |
| `command` | Run a server command | `command` (`@p` = player), `permission_level` (0-4), `silent`, `team`, `feedback_message` |
| `advancement` | Grant an advancement | `advancement` |
| `stage` | Add/remove a game stage | `stage`, `remove` (bool) |
| `currency` | Grant FTB currency | amount (needs a recent FTB Library) |
| `toast` | Show a popup only | title/description |
| `custom` | KubeJS-driven | `id` matched in `FTBQuestsEvents.customReward` |

```snbt
rewards: [
    { id: "...", type: "xp", xp: 10 }
    { id: "...", type: "item", count: 16, item: { count: 1, id: "minecraft:torch" } }
]
```

**Two count fields on item rewards:** inner `item.count` is the stack template (usually 1); outer
`count` on the reward is how many to actually grant. This pack's `count: 4` food rewards use this.
Auto-claim follows `data.snbt`'s `default_autoclaim_rewards`.

---

## 8. IDs (the positive-long rule)

Every object (group, chapter, quest, task, reward, table, link) has an `id` that is a **signed
64-bit long written as a 16-char uppercase hex string** (e.g. `7CA7E000C0DE0001`). IDs are unique
**across the whole questbook** (deps, `table_id`, `autofocus_id`, `quest_links` all resolve globally).

**The trap (load-bearing):** the leading hex digit encodes the sign. An id starting with **8-F is a
negative long**, which FTB rejects on load, **regenerates** to a fresh id, and rewrites - silently
**dropping every `dependencies` reference that pointed at the old id** (severing whole branches).
**Always lead hand-authored ids with hex `0-7`.** This pack enforces it with
`tools/fix_quest_ids.py` (remaps a chapter's negative-leading ids into the positive range,
remapping dependency references identically) and the validator's `Q-ID-POSITIVE` check.

When FTB itself generates ids (in-editor) they're always valid; the rule only matters for
hand-authored snbt.

---

## 9. Lang / text extraction

On world load FTB moves all human-readable text into `lang/<locale>.snbt`, keyed by object id.
Chapters keep only structure. Keys:

```snbt
{
    chapter_group.0C4F0E0000000001.title: "Tier 1: Cave"
    chapter.7CA7E000C0DE0001.title: "Cave Frogs"
    quest.01A8E068925B319F.title: "Welcome to Sky Frogs"
    quest.01A8E068925B319F.quest_subtitle: "..."
    quest.01A8E068925B319F.quest_desc: [
        "Line one of the description."
        ""
        "A blank \"\" entry is a blank line. Colors use the &alegacy&r form."
    ]
}
```

- `quest_desc` is a **list of strings**, one per rendered line (`""` = blank line).
- Color/format codes use `&` (`&a`, `&e`, `&b`, `&f`, `&r`, ...). This pack's convention:
  `&e` machines/blocks, `&b` goal items, `&f` raw materials; "Froglight" not "Configurable Froglight".
- `fallback_locale` (default `en_us`) backs untranslated keys.
- **Authoring rule:** put text here, not inline in chapters. The validator's `Q-LANG-ORPHAN`
  flags lang keys whose quest no longer exists; `Q-NO-DASHES` flags em/en-dashes in lang values.

---

## 10. Links, images, cross-chapter deps, progression, teams

- **Quest links** (`quest_links[]`): a ghost copy of another chapter's quest on this canvas.
  Fields: `id`, `linked_quest` (the real id), `x`, `y`, `shape`, `size`. Progress mirrors the original.
- **Images** (`images[]`): decorative/interactive overlays. Fields include `x`, `y`, `width`,
  `height`, `rotation`, `image` (resource id), `alpha`, `click` (command/link), `dev` (editor-only),
  `dependency` (show only when a quest is in a state).
- **Cross-chapter dependencies:** ids are global, so a quest's `dependencies` may point at a quest
  in another chapter. This is exactly how this pack gates tiers (e.g. `road_to_tide` quests depend
  on the `bog_frogs` capstone).
- **Teams:** FTB Quests is team-based (via FTB Teams). Completion and reward claims are tracked
  **per team**, and live in world save data (`<world>/ftbquests/`), NOT in `config/` - so the
  committed quest files are team-agnostic templates. `default_reward_team` / a reward's `team` flag
  grant once per team.

---

## 11. Reward tables / loot crates (`reward_tables/`)

A reward table is its own object (`id`, one file per table) referenced by a reward's `table_id`.

| Field | Meaning |
|---|---|
| `id` | table id (what `table_id` references) |
| `loot_size` | rolls per grant |
| `empty_weight` | weight of the "nothing" outcome |
| `use_title` | show the table title in the reward listing |
| `rewards[]` | `[{ reward: { <a reward object> }, weight: <float> }]` |
| `loot_crate` | present only if the table is a physical droppable crate (`string_id`, `item_name`, `color`, `glow`, per-rarity `drops`) |

A `weight: 0` entry is **granted every roll** (guaranteed); positive weights are random-rolled.
This pack does not currently use reward tables (all rewards are inline `item`/`xp`).

---

## 12. KubeJS integration (`FTBQuestsEvents`)

Author quests in SNBT/editor; use KubeJS only for **custom tasks/rewards and completion hooks**
(not bulk generation). On 1.21 the surface is exposed via FTB XMod Compat.

```js
// A `type: "custom"` task whose id matches "mypack:special_task"
FTBQuestsEvents.customTask("mypack:special_task", event => {
  event.maxProgress = 100
  event.checkTimer = 20            // re-check every 20 ticks
  event.check = (task, player) => { /* advance/return progress */ }
})

// A `type: "custom"` reward
FTBQuestsEvents.customReward("mypack:special_reward", event => {
  event.player.give("minecraft:diamond 3")
})

// Completion hook
FTBQuestsEvents.completed("<questId>", event => { event.player.tell("done") })
```

The exact event/method surface shifts between KubeJS + FTB XMod Compat releases; verify against the
installed builds before relying on a specific accessor.

---

## 13. This pack's conventions (and how they're enforced)

- **Positive-leading ids** (section 8) - `tools/fix_quest_ids.py` + validator `Q-ID-POSITIVE`.
- **`match_components` on every component-discriminated item task** (section 6) - validator
  `Q-MATCH-COMPONENTS`. Strict for single-component items (Froglights), fuzzy for multi-component
  items (jetpacks).
- **Text in lang, structure in chapters** (section 9) - validator `Q-LANG-INLINE` / `Q-LANG-ORPHAN`.
- **No em/en-dashes** in authored text - validator `Q-NO-DASHES`.
- **Dependencies resolve, ids unique, no cycles** - validator `Q-DEP-RESOLVES` / `Q-ID-UNIQUE` /
  `Q-DEP-ACYCLIC`.
- **Quest variant matches a recipe that makes it** - validator `Q-VARIANT-MADE`.

Run `python tools/validate_quests.py` after any quest edit (the pre-commit hook and CI enforce it).
In-game runtime smoke test: `/sf_selftest`. See [`quest_testing.md`](./quest_testing.md).

---

## 14. Version-sensitive / verify-in-editor notes

- **Components vs NBT:** 1.21.1 uses `components` + `match_components` (`""`/`fuzzy`/`strict`).
  Pre-1.20.5 docs mentioning `nbt:` / `weak_nbt` describe the old system; ignore for this pack.
- **Exact hide-flag key names** (`hide_until_deps_complete` vs the chapter-level
  `hide_quest_until_deps_complete`) can vary by minor version - toggle in-editor and diff the snbt
  to confirm before hand-authoring.
- **Newer fields** (`max_completable_dependents`, `repeat_cooldown`, `currency` reward, `all_table`
  reward, `team_stage`) are 2101.x additions; older packs won't have them.
- When in doubt about a field's exact serialized form, build it in the in-game editor and read the
  resulting snbt - that's always ground truth for the installed version.
