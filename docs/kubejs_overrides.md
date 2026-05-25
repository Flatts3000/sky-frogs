# KubeJS Overrides

> **Status:** DRAFT — non-canonical. The "four pillars" framing and the disabled-item list are first-draft proposals. Sky Bees Reborn's KubeJS is referenced as a worked example so we don't reinvent the wheel on syntax — but Sky Frogs needs to decide its own answer to "what should the player NOT be allowed to do?" That's not just an anti-cheat question; it's an identity question.

The KubeJS surface is where Sky Frogs enforces its identity: **frogs replace mining** (a candidate framing). This document catalogues proposed disables, additions, and reshapings — with cross-references to analogous logic in Sky Bees Reborn for syntax patterns.

## Script layout

Per packwiz convention and mirroring Sky Bees Reborn:

```
kubejs/
  startup_scripts/      # Run before registry freeze. Registry tweaks, fuel definitions.
  server_scripts/       # Run on server start. Recipe add/remove, world rules.
  client_scripts/       # Run on client. JEI/lang tweaks.
  data/<ns>/            # Datapack overrides — tags, loot tables, recipe JSONs, slime variants.
  assets/<ns>/          # Resourcepack overrides — lang files, textures.
```

## The four pillars

### Pillar 1: Disable automated mining shortcuts

This is the load-bearing rule. Anything that lets a player generate resources without going through the frog loop is removed from JEI, marked DISABLED in tooltips, or recipe-stripped.

Reference: [`sky-bees-reborn-reference/extracted/kubejs/server_scripts/anti.js`](../../sky-bees-reborn-reference/extracted/kubejs/server_scripts/anti.js).

**Sky Bees Reborn's list of disabled items:**

| Item                                      | Mod                    | Why disabled                                  |
|-------------------------------------------|------------------------|------------------------------------------------|
| `actuallyadditions:lens_of_the_miner`     | Actually Additions     | Generates ores directly from stone             |
| `industrialforegoing:ore_laser_base`      | Industrial Foregoing   | Generates ores from nothing                    |

**Sky Frogs starting list (extend as we add more mods):**

| Item                                      | Mod                    | Why disabled                                  |
|-------------------------------------------|------------------------|------------------------------------------------|
| All `exdeorum:*_sieve` blocks             | Ex Deorum              | Sky Frogs does not use sieving as a mechanic   |
| All `exdeorum:*_mesh` items               | Ex Deorum              | No sieves = no need for meshes                 |
| `actuallyadditions:lens_of_the_miner`     | Actually Additions     | Generates ores directly from stone             |
| `industrialforegoing:ore_laser_base`      | Industrial Foregoing   | Generates ores from nothing                    |
| `rftoolsbuilder:builder` (with mining cards) | RFTools Builder    | Quarry → bypass; recipe-strip the quarry card  |
| Mekanism digital miner                    | Mekanism               | Same — recipe-strip                            |

**Pattern (lifted from `anti.js`):**

```js
// kubejs/server_scripts/anti.js
ServerEvents.recipes(event => {
  // Sieving disabled at the pack level — Sky Frogs uses a slime-farm bootstrap, not sieving.
  event.remove({ id: /^exdeorum:sieve\// })
  event.remove({ id: /^exdeorum:mesh\// })
  // Mining shortcuts (added as mods land in the pack):
  event.remove({ type: 'actuallyadditions:mining_lens' })
  event.remove({ type: 'industrialforegoing:laser_drill_ore' })
  event.remove({ output: 'rftoolsbuilder:shape_card_void' })
  event.remove({ output: 'mekanism:digital_miner' })
})

ItemEvents.modifyTooltips(event => {
  // Hint to anyone looking up sieves in JEI that the omission is intentional
  ['exdeorum:wooden_sieve', 'exdeorum:string_mesh', 'exdeorum:flint_mesh', 'exdeorum:iron_mesh']
    .forEach(id => event.add(id, [
      Text.red('⚠️ DISABLED'),
      Text.gray('Sky Frogs uses a slime-farm bootstrap.'),
      Text.gray('Build a dark-room mob farm instead.')
    ]))
  event.add('actuallyadditions:lens_of_the_miner', [
    Text.red('⚠️ DISABLED'),
    Text.gray('Mining shortcuts are disabled by design.'),
    Text.gray('Use frogs.')
  ])
})
```

Sky Bees Reborn also blocks **fake-player right-clicks** on `exdeorum` and `animal_pen` blocks to prevent autocrafting cheese — we mirror this:

```js
const fake_player_block_mods = ['exdeorum', 'animal_pen']

BlockEvents.rightClicked(event => {
  const { player, block } = event
  let modID = String(block.id).split(':')[0]
  if (player.fake && fake_player_block_mods.includes(modID)) {
    event.cancel()
  }
})
```

### Pillar 2: Parent species spawn rules — Bog free, others gated

Per PF's `ParentSpeciesEntry`, six parent species map to the six categories:

| Parent entity                    | Category  | Tier 0 spawn rule (Sky Frogs)                                  |
|----------------------------------|-----------|----------------------------------------------------------------|
| `productivefrogs:bog_slime`      | BOG       | **Spawns naturally in the dark room** because the island is forced to `minecraft:swamp` and PF already ships bog_slime spawning there. This is the Tier 0 slime-farm fuel. No pack-side override. |
| `productivefrogs:infernal_slime` | INFERNAL  | PF's shipped rules unchanged — player reaches Nether at Tier 5. |
| `productivefrogs:cave_slime`     | CAVE      | Quest-reward spawn egg unlocked at Tier 2 entry.              |
| `productivefrogs:geode_slime`    | GEODE     | Quest-reward spawn egg at Tier 3.                              |
| `productivefrogs:tide_slime`     | TIDE      | Quest-reward spawn egg at Tier 4.                              |
| `productivefrogs:void_slime`     | VOID      | Quest-reward spawn egg at Tier 6.                              |

The asymmetry is intentional: the Bog parent free-spawns so the player has a Tier 0 fuel source for the mob farm; the other four PF parents are tier-gated via quests so the player can't skip-progress.

**Verified mechanism (settled 2026-05-25). This needs NO pack-side spawn code at all.** Productive Frogs
v1.0.0 already ships bog_slime spawning end to end:

1. A biome modifier (`add_bog_slime_spawn.json`) that adds `productivefrogs:bog_slime` to the monster
   spawn list of `minecraft:swamp` + `minecraft:mangrove_swamp`, so the natural spawner *attempts* it.
2. A light-based placement rule (`checkParentSlimeSpawnRules`, registered via
   `RegisterSpawnPlacementsEvent` REPLACE) so those attempts pass in a dark room.

So the pack does **not** need a KubeJS spawn override, does **not** need its own biome modifier, and does
**not** depend on any PF feature request. The only pack-side requirement is **forcing the SkyblockBuilder
island to the `minecraft:swamp` biome** (see [`worldgen.md`](./worldgen.md)); PF's shipped bog_slime
spawning then fires in a dark room on that island.

> **Note:** the pack-side `slime_spawns.json` biome modifier that an earlier draft proposed has been
> **removed** — PF ships its own biome modifier (`add_bog_slime_spawn.json`), so a duplicate pack-side
> one is unnecessary and would only double-register the spawn entry. There is also no dependency on any
> PF issue for slime spawning; the earlier `minecraft:slime` + placement-rule-flag plan is obsolete.

The other four PF parents (cave/geode/tide/void slime) are acquired via quest-reward spawn eggs in their respective tier chapters. See [`quest_book.md`](./quest_book.md).

### Pillar 3: Generate Resource Slime variants for modded resources

Productive Frogs supports cross-mod resource compatibility via JSON: drop a `slime_variant/<name>.json` under any datapack namespace and the matching-category frog will eat it. We use this aggressively — every modded resource we want frog-farmable gets a slime variant JSON, generated via KubeJS data scripts.

**Pattern:**

```js
// kubejs/data/<datapack_ns>/productivefrogs/slime_variant/<resource_name>.json
{
  "category": "bog",
  "primer_item": "mekanism:ingot_osmium",
  "drop_item": "productivefrogs:configurable_froglight",
  "drop_components": {
    "productivefrogs:variant": "skyfrogs:osmium"
  },
  "smelt_result": "mekanism:ingot_osmium",
  "crush_result": { "item": "mekanism:dust_osmium", "count": 2 },
  "neoforge:conditions": [
    { "type": "neoforge:mod_loaded", "modid": "mekanism" }
  ]
}
```

The conditional load means the JSON is harmless if the player removes Mekanism — the variant just doesn't register. This is the same pattern Productive Frogs ships out of the box for vanilla.

We'll write a KubeJS **startup-time generator** that takes a manifest like:

```js
// kubejs/startup_scripts/slime_variant_generator.js
const SLIME_VARIANTS = [
  // Bog — Mekanism
  { mod: 'mekanism', ns: 'skyfrogs', id: 'osmium',  cat: 'bog', primer: 'mekanism:ingot_osmium',  smelt: 'mekanism:ingot_osmium' },
  { mod: 'mekanism', ns: 'skyfrogs', id: 'tin',     cat: 'bog', primer: 'mekanism:ingot_tin',     smelt: 'mekanism:ingot_tin' },
  // ... ~50 variants across all categories
]
```

…and emits the JSONs at the right paths. This keeps the variant manifest readable in one place.

Reference: Sky Bees Reborn does the equivalent for its custom bees in [`kubejs/data/productivebees/productivebees/`](../../sky-bees-reborn-reference/extracted/kubejs/data/productivebees/productivebees/) (a directory full of custom bee JSONs).

### Pillar 4: Recipe overrides to force frog ingredients

For each tech tier we want the player to actually use frog outputs (not bypass via vanilla crafting), we override the relevant recipes to require Configurable Froglights.

Example for netherite (Tier 5 quest):

```js
ServerEvents.recipes(event => {
  event.remove({ output: 'minecraft:netherite_scrap' })
  event.smelting(
    'minecraft:netherite_scrap',
    { type: 'productivefrogs:component',
      components: { 'productivefrogs:variant': 'skyfrogs:ancient_debris' },
      items: 'productivefrogs:configurable_froglight' }
  ).id('skyfrogs:netherite_scrap_from_froglight')
})
```

The exact list of forced-frog-ingredient recipes is in [`quest_book.md`](./quest_book.md) per chapter — the questbook drives this.

## Other scripts (from SBR's structure)

Sky Bees Reborn ships these additional `server_scripts/`. Sky Frogs analogs:

| SBR script              | Purpose                                      | Sky Frogs equivalent                                                  |
|-------------------------|----------------------------------------------|------------------------------------------------------------------------|
| `barrel.js`             | Iron Barrels mob essence handling            | TBD — same pattern if we ship Iron Furnaces/Barrels                    |
| `botany_pots.js`        | BotanyPots crop additions                    | Same                                                                   |
| `enderio.js`            | EnderIO recipe overrides                     | Same                                                                   |
| `extended_crafting.js`  | Ultimate singularity recipe                  | Same — gated behind Tier 6                                             |
| `functional_storage.js` | Drawer recipe tweaks                         | Same                                                                   |
| `heat_sources.js`       | IF/Mek heat source registrations             | Same                                                                   |
| `market.js`             | Villager trade tweaks                        | Same                                                                   |
| `minecraft.js`          | Vanilla recipe overrides                     | Same — extensively used                                                |
| `player_events.js`      | First-join welcome handler                   | Same — opens Sky Frogs Patchouli book on first join                    |
| `powah.js`              | Powah recipe gates                           | Same                                                                   |
| `productivemetalworks.js` | Smeltery recipe tweaks                     | Same                                                                   |
| `sieve.js`              | Ex Deorum sieve additions / removals         | Same — heavily edited; this is the bootstrap loop                      |
| `tags.js`               | Custom tag definitions                       | Same — define `productivefrogs:primer/*` aliases for modded resources  |

## What we do NOT override

- **Mod internal recipes** that are part of the mod's intended progression but not material-generating. We don't touch Mekanism's reactor recipes, AE2's processor cycles, etc.
- **Vanilla aesthetic recipes** — wool dyeing, banners, decorations. Untouched.
- **JEI display rules** — handled in `client_scripts/jei.js` per-mod, but only for the explicitly DISABLED items (we hide them from JEI). Everything else stays default.

## Open KubeJS questions

- Does PF expose biome-locked parent species spawn recipes that we can override datapack-side? If yes, pattern matches SBR's bee_nests exactly. If no, we need a Java change in PF or a fallback (quest-reward eggs only).
- Do we ship our **slime variant generator** as a startup script or as a python pre-build script that emits JSON to a `kubejs/data/` tree at packaging time? Both work; startup-script is more "live" (no rebuild needed when editing the manifest), python is more legible (no JS sourcemaps to chase if it breaks).
- Should we expose **pack-level config** for difficulty (number of milk source spawns, frog drop rates) via a single `config/skyfrogs.json` read by our KubeJS scripts? Yes, almost certainly — but post-v0.1.
