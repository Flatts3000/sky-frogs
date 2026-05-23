# KubeJS Overrides

The KubeJS surface is where Sky Frogs enforces its identity: **frogs replace mining**. This document catalogues what we disable, what we add, and what we shape — with concrete references to the analogous logic in Sky Bees Reborn for each pattern.

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
| `actuallyadditions:lens_of_the_miner`     | Actually Additions     | Same as SBR                                    |
| `industrialforegoing:ore_laser_base`      | Industrial Foregoing   | Same as SBR                                    |
| `rftoolsbuilder:builder` (with mining cards) | RFTools Builder    | Quarry → bypass; recipe-strip the quarry card  |
| Mekanism digital miner                    | Mekanism               | Same — recipe-strip                            |

**Pattern (lifted from `anti.js`):**

```js
// kubejs/server_scripts/anti.js
ServerEvents.recipes(event => {
  event.remove({ type: 'actuallyadditions:mining_lens' })
  event.remove({ type: 'industrialforegoing:laser_drill_ore' })
  // Sky-Frogs additions:
  event.remove({ output: 'rftoolsbuilder:shape_card_void' })
  event.remove({ output: 'mekanism:digital_miner' })
})

ItemEvents.modifyTooltips(event => {
  event.add('actuallyadditions:lens_of_the_miner', [
    Text.red('⚠️ DISABLED'),
    Text.gray('The lens has been disabled to preserve'),
    Text.gray('the progression of the pack')
  ])
  // ...repeat for each disabled item
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

### Pillar 2: Productive Frogs spawn recipes — allow species in any biome

Productive Frogs' parent species (cave/geode/tide/void slime) ship with biome-locked spawn recipes (TBD if PF exposes them as datapack recipes; verify against latest PF). On a void skyblock those biomes don't exist, so we KubeJS-override the spawn recipes to allow any-biome (or specifically `#minecraft:is_overworld`).

Reference pattern (from SBR's [`productivebees.js`](../../sky-bees-reborn-reference/extracted/kubejs/server_scripts/productivebees.js) lines 167-199):

```js
event.remove({ type: 'productivebees:bee_spawning' })

bee_nests.forEach((pair, index) => {
  let builder = {
    type: "productivebees:bee_spawning",
    ingredient: { item: pair.nest },
    results: [ `productivebees:${pair.bee}` ],
    spawn_item: { item: 'productivebees:honey_treat' },
    biomes: '#minecraft:is_overworld',  // <-- the key override
  }
  event.custom(builder).id(`skybeesreborn:nest_spawn_${pair.bee}_${index}`)
})
```

**Sky Frogs equivalent (pending PF API verification):**

```js
// kubejs/server_scripts/productive_frogs.js
const parent_species = [
  { species: 'productivefrogs:cave_slime',   category: 'mineral' },
  { species: 'productivefrogs:geode_slime',  category: 'gem' },
  { species: 'productivefrogs:tide_slime',   category: 'aquatic' },
  { species: 'productivefrogs:void_slime',   category: 'arcane' },
]

ServerEvents.recipes(event => {
  // If PF exposes biome-locked spawn recipes, remove + re-emit with any-biome.
  // If not, skip — parent species are quest-reward-distributed instead.
  // event.remove({ type: 'productivefrogs:parent_species_spawn' })  // TBD
})
```

If PF doesn't expose datapack spawn rules, fallback is **quest-reward distribution** — see [`worldgen.md`](./worldgen.md) and [`quest_book.md`](./quest_book.md).

### Pillar 3: Generate Resource Slime variants for modded resources

Productive Frogs supports cross-mod resource compatibility via JSON: drop a `slime_variant/<name>.json` under any datapack namespace and the matching-category frog will eat it. We use this aggressively — every modded resource we want frog-farmable gets a slime variant JSON, generated via KubeJS data scripts.

**Pattern:**

```js
// kubejs/data/<datapack_ns>/productivefrogs/slime_variant/<resource_name>.json
{
  "category": "metallic",
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
  // Metallic — Mekanism
  { mod: 'mekanism', ns: 'skyfrogs', id: 'osmium',  cat: 'metallic', primer: 'mekanism:ingot_osmium',  smelt: 'mekanism:ingot_osmium' },
  { mod: 'mekanism', ns: 'skyfrogs', id: 'tin',     cat: 'metallic', primer: 'mekanism:ingot_tin',     smelt: 'mekanism:ingot_tin' },
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
