# KubeJS Overrides

> **Status:** PARTIAL DRAFT. The Tier 0-3 overrides documented here are **built and live** in `pack/kubejs/server_scripts/` (anti, seed-chains, spawnery primers, the storage/plastic/steel/log overrides). Only the Tier 4-6 specifics (Tide / Infernal / Void variants and their forced recipes) remain a sketch.

The KubeJS surface is where Sky Frogs enforces its identity: **frogs are the resource path.** This document catalogues the shipped disables, additions, and reshapings, plus the design laws they follow. Sky Bees Reborn's KubeJS is cross-referenced for syntax patterns only; Sky Frogs answered "what should the player NOT be allowed to do?" on its own terms.

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

Shipped in [`pack/kubejs/server_scripts/anti.js`](../pack/kubejs/server_scripts/anti.js). The list below reflects what `anti.js` actually disables today, not a candidate sketch.

**Sky Frogs disabled list (as shipped):**

| Target                                    | Mod                    | Why disabled                                   |
|-------------------------------------------|------------------------|------------------------------------------------|
| `exdeorum:sieve` recipe type (default, id-anchored `^exdeorum:`) | Ex Deorum | Kills the DEFAULT sieve drop tables (ores/gems/seeds - the progression bypass); the curated `kubejs:builder_sieve/*` lane is exempt by id |
| `exdeorum:compressed_sieve` recipe type (id-anchored) | Ex Deorum | Same, for the compressed-sieve variant; no curated recipes exist for it |
| `exdeorum:<wood>_sieve` block crafting    | Ex Deorum              | Strips all sieve-block crafts via regex; `builder_sieve.js` re-adds ONLY the oak sieve under a kubejs id. The Mechanical Sieve stays uncraftable (the lane is manual-only) |
| `#exdeorum:sieve_meshes` tag (id-anchored) | Ex Deorum             | Five of six meshes stay dead weight; the STRING mesh is re-added for the builders' lane |
| `mekanism:digital_miner`                  | Mekanism               | Automated ore miner = a direct frog-loop bypass |

**The one deliberate exception (#76):** [`builder_sieve.js`](../pack/kubejs/server_scripts/builder_sieve.js) reopens a curated lane - oak sieve + string mesh over **dirt** (saplings of every overworld wood, bamboo, sugar cane, cactus, plus grass seeds and the food-seed lane as of #87/#91) and **moss** (azaleas, vines, glow lichen, dripleaf, every small/tall flower). Cosmetic and building flora plus food seeds only; no ores, gems, mob drops, or progression materials. Dirt is composter-cheap at Tier 0; moss is a Bog frog resource.

The Actually Additions mining lens and the IF laser drill are **scaffold lines kept commented** in `anti.js` (those mods aren't in the pack, and live `event.remove` on unmatched ids logs noise). The only live mining-shortcut disable is the Mekanism Digital Miner.

**Per-mod curation scripts (the Pillar 1 pattern, one file per curated mod):**

| Script | Mod | What it curates |
|---|---|---|
| [`anti.js`](../pack/kubejs/server_scripts/anti.js) + [`builder_sieve.js`](../pack/kubejs/server_scripts/builder_sieve.js) | Ex Deorum, Mekanism | Default sieving stripped; the curated builders' lane; Digital Miner |
| [`opolis_curation.js`](../pack/kubejs/server_scripts/opolis_curation.js) | Opolis Utilities (BBL Utility) | Six #85 rulings: stone-lane Resource Generator, severed Fluid Generator + Catalogue/B-Bucks economy, glow_squid/squid summons stripped |
| [`cobblegen_curation.js`](../pack/kubejs/server_scripts/cobblegen_curation.js) | Cobblegen Galore | #90 ruling: the netherrack/obsidian/tuff blockgen recipes stripped (all three outputs are frog resources + singularity inputs); the seven builders' stone generators stay |
| [`upstream_recipe_fixes.js`](../pack/kubejs/server_scripts/upstream_recipe_fixes.js) | Iron Furnaces | A different category: removals of BROKEN upstream recipes (unparseable ATM-metal upgrades), not design disables - future broken-recipe fixes belong here |

Conventions every curation file follows: removals **id-anchored to the source mod's namespace** (so curated `kubejs:*` re-adds are untouchable), `Platform.isLoaded` guards on every event that touches the mod's ids, and item probing via **`Item.exists()`** never `Item.of()` (whose parse errors LOG past any try/catch - learned on #86).

**Pattern (as shipped in `anti.js`):**

```js
// kubejs/server_scripts/anti.js
ServerEvents.recipes(event => {
  // 1. Kill the sieving MECHANIC (both recipe types cover every sieve variant).
  event.remove({ type: 'exdeorum:sieve' })
  event.remove({ type: 'exdeorum:compressed_sieve' })
  // 2. Strip the sieve BLOCK crafts (regex catches oak_sieve, mechanical_sieve, modded woods, ...).
  event.remove({ id: /^exdeorum:[a-z0-9_]+_sieve$/ })
  // 3. Strip mesh crafting via the tag (string/flint/iron/golden/diamond/netherite + future).
  event.remove({ output: '#exdeorum:sieve_meshes' })
  // 4. Mekanism Digital Miner: the only live mining-shortcut disable.
  event.remove({ output: 'mekanism:digital_miner' })
  // Scaffold (kept commented until the mods land, to avoid unmatched-recipe noise):
  // event.remove({ type: 'actuallyadditions:mining_lens' })
  // event.remove({ type: 'industrialforegoing:laser_drill_ore' })
})

ItemEvents.modifyTooltips(event => {
  // Per-ID (not tag) - that's the verified-working modifyTooltips signature.
  const meshes = ['exdeorum:string_mesh', 'exdeorum:flint_mesh', 'exdeorum:iron_mesh',
                  'exdeorum:golden_mesh', 'exdeorum:diamond_mesh', 'exdeorum:netherite_mesh']
  meshes.forEach(id => event.add(id, [
    Text.red('Disabled in Sky Frogs'),
    Text.gray('No sieving here - the frogs handle resources.'),
    Text.gray('Build a dark-room slime farm instead.')
  ]))
  event.add('mekanism:digital_miner', [
    Text.red('Disabled in Sky Frogs'),
    Text.gray('Automated mining bypasses the frogs - not in this pack.')
  ])
})
```

`anti.js` also blocks **fake-player right-clicks** on the Ex Deorum blocks we keep (barrels/crucibles) to prevent automation cheese:

```js
const fake_player_block_mods = ['exdeorum']

BlockEvents.rightClicked(event => {
  const { player, block } = event
  const modId = String(block.id).split(':')[0]
  if (player.fake && fake_player_block_mods.includes(modId)) {
    event.cancel()
  }
})
```

### Pillar 2: Parent species spawn rules — the pack owns spawning

Per PF's `ParentSpeciesEntry`, six parent species map to the six categories. Because progression is **species-gated** (see [`progression.md`](./progression.md)), only the *current* species should ever be obtainable, so the pack owns spawn policy entirely and PF just supplies a light-based placement-rule hook.

Tier mapping (built): Tier 0 Welcome (cave_slime farm bootstrap) -> Tier 1 **CAVE** -> Tier 2 **GEODE** -> Tier 3 **BOG**. Cave is the Tier 1 starter species. Tide / Infernal / Void are not built yet.

| Parent entity                    | Category  | Tier   | How the player gets it in Sky Frogs                            |
|----------------------------------|-----------|--------|----------------------------------------------------------------|
| `productivefrogs:cave_slime`     | CAVE      | 1      | **Spawns in the Tier 0 dark room** - the pack adds it to the island biome (below). The starter species. |
| `productivefrogs:geode_slime`    | GEODE     | 2      | Bootstrapped from the Cave line via a seed-chain recipe (below). |
| `productivefrogs:bog_slime`      | BOG       | 3      | Bootstrapped from the Geode line via a seed-chain recipe (below). |
| `productivefrogs:tide_slime`     | TIDE      | (sketch) | Not built. Will follow the Bog line.                         |
| `productivefrogs:infernal_slime` | INFERNAL  | (sketch) | Not built. Will follow the Tide line.                        |
| `productivefrogs:void_slime`     | VOID      | (sketch) | Not built. Will follow the Infernal line.                    |

Only Cave spawns naturally; every later species is bootstrapped from the previous tier via the **seed-chain / slime-in-a-bucket** override pattern (see Pillar 3). You can't reach a Geode Slime before finishing the Cave line.

**Mechanism (pack owns it; PF supports it):**

1. **Disable PF's default spawns.** PF ships per-species biome modifiers (`add_*_slime_spawn.json`) targeting vanilla biomes (cave -> dripstone/deep_dark, bog -> swamp, ...) - right for a normal world, wrong for a gated skyblock. The pack overrides all six with `{"type":"neoforge:none"}` at `kubejs/data/productivefrogs/neoforge/biome_modifier/add_*_slime_spawn.json`, so nothing spawns unless the pack says so.
2. **Add Cave to the island.** `kubejs/data/skyfrogs/neoforge/biome_modifier/add_cave_slime_island.json` adds `productivefrogs:cave_slime` to the island biome (`minecraft:swamp`).
3. **PF's hook does the rest.** PF's `checkParentSlimeSpawnRules` (registered via `RegisterSpawnPlacementsEvent`) is light-based, so cave_slime spawns in a dark room on the island regardless of the biome's theme.

> **Needs in-game verification:** that KubeJS's `data/` folder overrides PF's biome modifiers (datapack load order), so the `neoforge:none` disables actually take. Confirmed-working assumption; check on first load.

### Pillar 3: The seed-chain / slime-in-a-bucket override pattern

This is the **dominant** KubeJS override in the pack. The original sketch here proposed a single startup-time generator emitting ~50 `slime_variant` JSONs from a manifest. The build did **not** go that way: PF v1.5+ already ships the per-resource `slime_variant` data (each carrying its own category, primer, and `smelt_result`), so the pack does not author variant JSONs at all. Instead the pack hand-authored **per-tier seed-chain scripts** that thread the player from one resource to the next. Hand-authored chains won over a generator because the threading order (which resource seeds which) is a design decision per tier, not something a manifest expresses cleanly.

**The Froglight-check principle (pack-wide design law).** Per-tier resource quests detect the variant **Froglight** the frog drops, NOT the smelted resource. The Configurable Froglight carries a `productivefrogs:slime_variant` component (a namespaced variant id like `productivefrogs:copper`), and a quest that checks for `productivefrogs:configurable_froglight` carrying that component cannot be gamed by handing in an ingot you got elsewhere - the Froglight is the frog's proof of work. (Confirm the component key in the chain scripts: it is `productivefrogs:slime_variant`, **not** `productivefrogs:variant`.) Deliberate exceptions:
- **"Your First Iron Ingot"** capstone keeps an `iron_ingot` check (it's the tutorial smelt; the Froglight is already gated upstream by the "Feed the Frog" step).
- The main Mekanism **"Steel"** quest keeps an `ingot_steel` check (steel via the infuser is a genuine Mekanism craft); the *optional* steel-slime quest carries the Froglight check instead.

**The seed-chain mechanism.** Each step is a shapeless recipe that converts the prior resource's Slime Milk into the next resource's slime-in-a-bucket:

```
1x <prior> Slime Milk bucket   (what you convert from; supplies the empty bucket too)
4x <tier filler block>         (on-brand for the tier; see table below)
3x productivefrogs:sweetslime  (the frog-coaxing binder)
1x <tier> frogspawn bottle     (the category seed; frog_egg with contained_category)
  -> 1x <next> Slime in a Bucket
```

The output stamps both `Variant` and `Category` into `minecraft:bucket_entity_data` to match PF's JEI slime-bucket subtype (keyed on the full `bucket_entity_data` string). Run the result through the Slime Milker for that resource's Slime Milk, place it, and the matching slimes spawn for the frog to eat. As shipped in [`cave_slime_chain.js`](../pack/kubejs/server_scripts/cave_slime_chain.js):

```js
event.shapeless(
  `productivefrogs:slime_bucket[minecraft:bucket_entity_data={Variant:"productivefrogs:${to}",Category:"CAVE"}]`,
  [
    `productivefrogs:${from}_slime_milk_bucket`,
    'minecraft:stone', 'minecraft:stone', 'minecraft:stone', 'minecraft:stone',
    'productivefrogs:sweetslime', 'productivefrogs:sweetslime', 'productivefrogs:sweetslime',
    'productivefrogs:frog_egg[productivefrogs:contained_category="cave"]'
  ]
)
```

The `<from>` Slime Milk ingredient is a **per-variant item** (`productivefrogs:<variant>_slime_milk_bucket`) as of PF v1.8.0. Earlier versions used a single `slime_milk_bucket` carrying the variant in a `productivefrogs:slime_variant` component; v1.8 split each variant into its own fluid + bucket so pipe automation preserves the variant, and the component form no longer exists.

**Per-tier filler blocks.** The 4 filler blocks are themed per tier, with one hard constraint: the filler must be attainable AT that tier (never a chain output, never gated behind a later tier).

| Tier  | Filler block         | Why it fits the tier                                              |
|-------|----------------------|-------------------------------------------------------------------|
| Cave  | `minecraft:stone`    | On-brand for the stone-and-ore Cave frog                          |
| Geode | `minecraft:gravel`   | The Ex Deorum gem-sieving block (gem tier); reachable via Cobblegen Galore's cobblestone->gravel hammer path |
| Bog   | `minecraft:mossy_cobblestone` | Made in Mekanism's Metallurgic Infuser / Enrichment Chamber (the Geode-era machines); ties the mineral->organic transition |

**The shipped seed-chain scripts:**

| Script                                                                                  | Tier  | Chain                                                                 |
|-----------------------------------------------------------------------------------------|-------|-----------------------------------------------------------------------|
| [`cave_slime_chain.js`](../pack/kubejs/server_scripts/cave_slime_chain.js)              | 1 Cave  | iron -> copper -> gold -> coal -> redstone                          |
| [`geode_slime_chain.js`](../pack/kubejs/server_scripts/geode_slime_chain.js)            | 2 Geode | redstone (Cave) -> lapis -> tuff -> calcite -> amethyst -> emerald -> diamond |
| [`bog_slime_chain.js`](../pack/kubejs/server_scripts/bog_slime_chain.js)                | 3 Bog   | diamond (Geode bridge) -> dirt -> mud -> clay_ball -> moss -> mycelium -> lily_pad -> leather -> feather -> plastic -> pink_slime |
| [`iron_slime_bucket.js`](../pack/kubejs/server_scripts/iron_slime_bucket.js)            | 1 boot  | Bootstrap: conjures the first Iron Slime in a bucket (no iron needed) |
| [`osmium_slime_bucket.js`](../pack/kubejs/server_scripts/osmium_slime_bucket.js)        | 2 boot  | Bootstrap: redstone (Cave) milk -> osmium slime, seeding the Mekanism chapter |
| [`steel_slime_infusing.js`](../pack/kubejs/server_scripts/steel_slime_infusing.js)      | 2 opt   | Iron Slime bucket + carbon -> Steel Slime bucket via the Metallurgic Infuser |

`iron_slime_bucket.js` and `osmium_slime_bucket.js` exist because a void skyblock has no iron or osmium ore - PF's normal "prime an Iron Slime with an iron ingot" route is a chicken-and-egg soft-lock, so these conjure the first slime from items the player already has. The Bog chain's plastic and pink_slime steps are appended only when Industrial Foregoing is loaded (it always is in this pack; the `Platform.isLoaded` guard is dev-safety).

### Pillar 4: Recipe overrides to force (or gate) frog ingredients

Where a tech tier could be bypassed by a non-frog route, the pack either removes the bypass or re-issues the recipe to require the frog's Froglight (component key `productivefrogs:slime_variant`). The shipped gates and stopgaps:

- [`spawnery_primer/*` tag overrides](../pack/kubejs/data/productivefrogs/tags/item/spawnery_primer/) (datapack). PF reads a `spawnery_primer/<category>` item tag to decide what primes each category's Spawnery. The pack overrides four (`replace: true`) so the primer is a tier-appropriate item: `cave -> minecraft:cobblestone`, `geode -> minecraft:redstone`, `bog -> mekanism:enriched_diamond`, `tide -> industrialforegoing:pink_slime` (Bog's capstone primes the next tier).
- [`storage_quartz_free.js`](../pack/kubejs/server_scripts/storage_quartz_free.js). Re-issues the Sophisticated + Functional Storage controller recipes without nether quartz (quartz is gated behind Infernal), making the analog (no-power) storage network a Cave-era stopgap. Refined Storage at Infernal stays the real upgrade.
- [`if_plastic_gate.js`](../pack/kubejs/server_scripts/if_plastic_gate.js). Removes Industrial Foregoing's only traditional plastic recipe **by id** (so the Froglight smelt survives), making the Bog plastic Froglight the sole plastic source - hard-gating Industrial Foregoing behind the Bog plastic-frog.
- [`dissolution_slime_recipes.js`](../pack/kubejs/server_scripts/dissolution_slime_recipes.js). Industrial Foregoing **Dissolution Chamber** slime recipes (the pack's slime engine). A `SLIME_TIERS` builder threads each variant off a prior vanilla resource (the previous tier's last resource for the first variant in a tier; the previous variant's resource for each step after) + tier filler + 3x sweetslime + 100 mb latex -> that variant's Slime in a Bucket. **Cave, Geode, Bog, and Tide** ship today (27 rows; iron bootstraps off bone meal, mirroring the original `iron_slime_bucket.js` crafting-table bootstrap; Tide threads off `industrialforegoing:pink_slime` with `minecraft:mycelium` filler); **Tier 5+** rows land as those tiers ship. Cave/Geode/Bog also have crafting-table chains as a parallel hand-craft path (the chamber is only available after Bog, so the tables are the path TO the chamber); **Tide and every later tier are chamber-only** - by Tier 4 the chamber is already built, so no hand-craft chain exists (there is no `tide_slime_chain.js`). **Resource-keyed inputs** (not milk-keyed) so the recipe round-trips through IF/Titanium's JSON codec; milk-keyed inputs crash `update_recipes` and PF declined adding a component-free per-variant handle (closed [productive-frogs#127](https://github.com/Flatts3000/productive-frogs/issues/127) as won't-fix).
- [`steel_slime_infusing.js`](../pack/kubejs/server_scripts/steel_slime_infusing.js). Adds the optional Steel Slime route (iron slime + carbon -> steel slime) via the Metallurgic Infuser, using a `neoforge:components` ingredient so only the iron slime bucket matches (no steel-from-anything exploit).
- [`log_recipes.js`](../pack/kubejs/server_scripts/log_recipes.js). Logs-direct stick/chest recipes (break-even ratios; just fewer crafting steps on a tree-farm skyblock).
- [`catalyst_recipes.js`](../pack/kubejs/server_scripts/catalyst_recipes.js). Re-issues PF's **Quantity** Slime Milk catalyst (PF v1.7.0) with **redstone** instead of glowstone - glowstone is Infernal-gated on a void skyblock, but the catalysts are introduced at the Geode diamond gate, so all four need to be craftable there. Count/Speed/Infinite already use skyblock-attainable mats; PF's default glowstone recipe is left intact for other packs.
- [`jdt_recipes.js`](../pack/kubejs/server_scripts/jdt_recipes.js). Re-issues JDT's tier-1 **Primogel Goo Block** with **mycelium** centered instead of dirt. Mycelium is a Bog Frogs chain variant, so this gates the JDT entry into the Bog mid-tier progression naturally (and "fungal substrate" suits the goo better than plain dirt anyway). Same shape and other ingredients as JDT default; JDT's stock dirt recipe is left intact for other packs.

The exact list of forced-frog-ingredient recipes is in [`quest_book.md`](./quest_book.md) per chapter - the questbook drives this. A future netherite gate (Tier 5+) would follow the same shape, re-issuing the smelt to require a `productivefrogs:configurable_froglight` carrying the matching `productivefrogs:slime_variant` component.

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
| `sieve.js`              | Ex Deorum sieve additions / removals         | N/A - Sky Frogs disables sieving in `anti.js`; the bootstrap is the slime seed-chains (Pillar 3), not sieving |
| `tags.js`               | Custom tag definitions                       | Shipped as datapack tag overrides (`spawnery_primer/*`, Pillar 4) rather than a server script |

## What we do NOT override

- **Mod internal recipes** that are part of the mod's intended progression but not material-generating. We don't touch Mekanism's reactor recipes, AE2's processor cycles, etc.
- **Vanilla aesthetic recipes** — wool dyeing, banners, decorations. Untouched.
- **JEI display rules** — handled in `client_scripts/jei.js` per-mod, but only for the explicitly DISABLED items (we hide them from JEI). Everything else stays default.

## Resolved KubeJS questions

- **Does PF expose spawn rules we can override datapack-side?** RESOLVED: yes. PF ships per-species `neoforge:biome_modifier` JSONs (`add_*_slime_spawn.json`); the pack overrides all six with `{"type":"neoforge:none"}` and adds Cave to the island via `skyfrogs` (Pillar 2). No Java change needed.
- **Generator vs python pre-build script for variants?** RESOLVED: neither. PF v1.5+ ships the `slime_variant` data itself, so the pack authors no variant JSONs. The work that remained (threading resources tier by tier) became the hand-authored **seed-chain scripts** (Pillar 3), which won because the threading order is a per-tier design decision, not a manifest entry.
- **Is the variant component schema stable?** RESOLVED: yes. `productivefrogs:slime_variant` (on the Froglight) and `minecraft:bucket_entity_data` with `Variant` + `Category` (on slime buckets) are stable and in active use across all three chain scripts.

## Still open

- Should we expose **pack-level config** for difficulty (number of milk source spawns, frog drop rates) via a single `config/skyfrogs.json` read by our KubeJS scripts? Probably, but post-v0.x.
- Tier 4-6 (Tide / Infernal / Void) seed-chains and forced recipes are unwritten - the patterns above are the template, but each tier's filler block and threading order are still open design decisions.
