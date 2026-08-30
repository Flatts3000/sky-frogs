// Sky Frogs - the Builders' Sieve (#76, suggested by Dergib on Discord).
//
// Pillar 1 (anti.js) kills Ex Deorum's DEFAULT sieving - ores, gems, seeds, the
// whole progression-bypass surface. This file reopens the builders' lane:
// a manual oak sieve + string mesh over DIRT and MOSS, dropping BUILDING FLORA
// (saplings, bamboo, flowers, garden plants) plus the VANILLA FOOD PLANTS that
// have no reachable source here - the seed lane restored in #87/#91, and the
// berries and mushrooms the #280 audit turned up. Nothing here touches
// the frog spine: no ores, no gems, no mob drops, no progression mats.
// "More than just oak" for builders - dirt is composter-cheap at Tier 0, moss
// is a Bog frog resource.
//
// Mechanics notes:
// - This file owns the HARDWARE: anti.js strips Ex Deorum's own oak sieve and
//   string mesh crafts, and they are re-added below under kubejs ids. The
//   kitchen lane (kitchen_sieve.js, #280) adds recipes against that same sieve
//   and mesh, so do not remove either craft without checking there too.
// - Only string-mesh recipes exist; the other five meshes craft nothing and
//   stay flagged in anti.js. The compressed sieve has no recipes at all.
// - The Mechanical Sieve block remains uncraftable (anti.js strips it): this
//   lane is manual by design - it's decor, not an economy.
// - Recipe shape mirrors Ex Deorum's own data (binomial result_amount, p =
//   drop chance per sieve action).

ServerEvents.recipes(event => {
  if (!Platform.isLoaded('exdeorum')) {
    return
  }

  // The hardware: Ex Deorum's own oak sieve + string mesh recipes, re-added
  // under kubejs ids (anti.js removes the exdeorum:-id originals).
  event.shaped(
    'exdeorum:oak_sieve',
    [
      'O O',
      'O_O',
      'I I'
    ],
    {
      O: 'minecraft:oak_planks',
      _: 'minecraft:oak_slab',
      I: '#c:rods/wooden'
    }
  ).id('kubejs:builder_sieve/oak_sieve')

  event.shaped(
    'exdeorum:string_mesh',
    [
      '###',
      '###',
      '###'
    ],
    {
      '#': '#c:strings'
    }
  ).id('kubejs:builder_sieve/string_mesh')

  // [input block, [[drop item, chance], ...]]
  const LANES = [
    ['minecraft:dirt', [
      // wood variety - the actual ask
      ['minecraft:oak_sapling',        0.13],
      ['minecraft:birch_sapling',      0.10],
      ['minecraft:spruce_sapling',     0.10],
      ['minecraft:jungle_sapling',     0.07],
      ['minecraft:acacia_sapling',     0.07],
      ['minecraft:dark_oak_sapling',   0.07],
      ['minecraft:cherry_sapling',     0.05],
      ['minecraft:mangrove_propagule', 0.05],
      ['minecraft:azalea',             0.05],
      ['minecraft:bamboo',             0.08],
      // ground-cover building plants
      ['minecraft:sugar_cane',         0.08],
      ['minecraft:cactus',             0.05],
      // Ex Deorum's grass seeds (right-click dirt -> grass block) - was in the
      // mod's own dirt defaults; re-added on player request (#87, bizarr0).
      ['exdeorum:grass_seeds',         0.10],
      // The default FOOD lane, restored by maintainer ruling 2026-06-06 at Ex
      // Deorum's own chances. Food is not a frog resource, so this bypasses
      // nothing; it just gives Tier 0 islands a seed source besides luck.
      // The vanilla seeds are the whole of it - the modded food seeds have
      // their own lane over mud in kitchen_sieve.js (#280).
      ['minecraft:wheat_seeds',        0.125],
      ['minecraft:pumpkin_seeds',      0.10],
      ['minecraft:melon_seeds',        0.10],
      ['minecraft:beetroot_seeds',     0.10],
      ['minecraft:potato',             0.10],
      ['minecraft:carrot',             0.10],
      ['minecraft:poisonous_potato',   0.05],
      // Sweet berries at Ex Deorum's own dirt chance. Nothing else in the pack
      // grows them (#280 audit): Ex Deorum's defaults are off, no structure
      // generates a bush, and Botany Pots' sweet_berry_bush is block-derived, so
      // it needs a berry to plant a berry.
      ['minecraft:sweet_berries',      0.05]
    ]],
    ['minecraft:moss_block', [
      // the garden lane
      // Kelp joins by maintainer ruling (#131, suggested by Dergib): with the
      // Water Singularity removed, kelp is decor/food again (dried kelp, kelp
      // blocks) - the wet plant in the wet lane, at Ex Deorum's own sand-sieve
      // chance. Vanilla growth takes water columns the island can build.
      ['minecraft:kelp',               0.10],
      // The lush-cave food plants, all three at Ex Deorum's own moss chances
      // (glow berries at its string-mesh value exactly). Same #280 audit: glow
      // berries had one path in the whole pack, Mekanism's combiner, which takes
      // a sweet berry as its input, and sweet berries had none.
      ['minecraft:sweet_berries',      0.03],
      ['minecraft:glow_berries',       0.04],
      // Mushrooms had exactly ONE path, and it is easy to miss: an Ex Deorum
      // barrel of water with mycelium on top turns into witch water over 1700
      // ticks and spits out red and brown mushrooms as byproducts. That is
      // Bog-tier (mycelium is a Bog frog resource, same as moss), undiscoverable
      // without reading the mod's data, and #270 proposes deleting the witch
      // water recipes outright - which would take the mushrooms with them. This
      // is a second path at the same tier, not a first one. Farmer's Delight's
      // colonies are worldgen and Botany Pots' mushroom crops are block-derived,
      // so both are circular here. Ex Deorum ships no mushroom SIEVE recipe, so
      // 0.05 is a pack decision with no upstream chance to copy.
      ['minecraft:brown_mushroom',     0.05],
      ['minecraft:red_mushroom',       0.05],
      ['minecraft:flowering_azalea',   0.05],
      ['minecraft:glow_lichen',        0.08],
      ['minecraft:vine',               0.08],
      ['minecraft:pink_petals',        0.06],
      ['minecraft:hanging_roots',      0.06],
      ['minecraft:big_dripleaf',       0.04],
      ['minecraft:small_dripleaf',     0.04],
      ['minecraft:spore_blossom',      0.03],
      // small flowers
      ['minecraft:dandelion',          0.08],
      ['minecraft:poppy',              0.08],
      ['minecraft:blue_orchid',        0.05],
      ['minecraft:allium',             0.05],
      ['minecraft:azure_bluet',        0.05],
      ['minecraft:oxeye_daisy',        0.05],
      ['minecraft:cornflower',         0.05],
      ['minecraft:lily_of_the_valley', 0.05],
      ['minecraft:red_tulip',          0.04],
      ['minecraft:orange_tulip',       0.04],
      ['minecraft:white_tulip',        0.04],
      ['minecraft:pink_tulip',         0.04],
      // tall flowers
      ['minecraft:sunflower',          0.03],
      ['minecraft:lilac',              0.03],
      ['minecraft:rose_bush',          0.03],
      ['minecraft:peony',              0.03]
    ]]
  ]

  LANES.forEach(lane => {
    const input = lane[0]
    const drops = lane[1]
    const inputName = input.split(':')[1]
    drops.forEach(drop => {
      const item = drop[0]
      const chance = drop[1]
      event.custom({
        type: 'exdeorum:sieve',
        ingredient: { item: input },
        mesh: { item: 'exdeorum:string_mesh' },
        result: { count: 1, id: item },
        result_amount: { type: 'minecraft:binomial', n: 1.0, p: chance }
      }).id(`kubejs:builder_sieve/${inputName}/${item.split(':')[1]}`)
    })
  })
})
