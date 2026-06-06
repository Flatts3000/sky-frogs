// Sky Frogs - the Builders' Sieve (#76, suggested by Dergib on Discord).
//
// Pillar 1 (anti.js) kills Ex Deorum's DEFAULT sieving - ores, gems, seeds, the
// whole progression-bypass surface. This file reopens exactly one curated lane:
// a manual oak sieve + string mesh over DIRT and MOSS, dropping COSMETIC AND
// BUILDING FLORA ONLY (saplings, bamboo, flowers, garden plants). Nothing here
// touches the frog spine: no ores, no gems, no mob drops, no progression mats.
// "More than just oak" for builders - dirt is composter-cheap at Tier 0, moss
// is a Bog frog resource.
//
// Mechanics notes:
// - Only these string-mesh recipes exist; the other five meshes craft nothing
//   and stay flagged in anti.js. The compressed sieve has no recipes at all.
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
      ['exdeorum:grass_seeds',         0.10]
    ]],
    ['minecraft:moss_block', [
      // the garden lane
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
