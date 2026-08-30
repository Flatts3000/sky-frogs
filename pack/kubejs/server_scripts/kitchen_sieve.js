// Sky Frogs - the Kitchen Sieve (#280, suggested by Seeker on Discord, backed by
// Nic_Knack819). Seeker had already built this as a datapack and offered it over.
//
// The problem is not "these seeds are rare", it is that they do not exist here.
// Mama's Herbs and Harvest ships NO worldgen and NO trades for its seeds: all 57
// are handed out by loot modifiers into structure chests only (mineshafts,
// villages, strongholds, trial chambers, ancient cities, shipwrecks - 42 targets
// each), and a void skyblock generates none of them. Grapes are worse off still,
// with no chest entry at all. Farmer's Delight is the same shape for cabbage,
// tomato, onion and rice: wild-crop worldgen plus village chests.
//
// So the pack was handing out 32 finished Farmer's Delight dishes from the Good
// Food Loot Crate that nobody could cook, while Spice of Life: Carrot Edition
// charged players hearts for the missing variety.
//
// This reopens one more curated lane: the same oak sieve + string mesh, over MUD.
// Mud is Tier 0 (dirt + a water bottle) and the third input after the builders'
// dirt and moss. Food is not a frog resource and nothing here is - no ores, no
// gems, no mob drops, no progression materials - so the frog spine is untouched.
// Same standing that let #87 restore the vanilla food-seed lane on dirt.
//
// Mechanics notes:
// - The HARDWARE lives in builder_sieve.js: anti.js strips Ex Deorum's own sieve
//   and mesh crafts, and builder_sieve.js re-adds the oak sieve + string mesh
//   under kubejs ids. This file only adds recipes; it crafts nothing.
// - Recipe ids carry the source namespace because Mama's Herbs and Harvest and
//   Farmer's Delight both register onion, rice, cabbage_seeds and tomato_seeds.
// - Every chance sits at or below Ex Deorum's own seed rates (its dirt lane runs
//   0.10 to 0.125). Each seed is a one-time unlock: plant it once and the crop
//   re-drops its own seed, so the lane is a door, not an income stream.

ServerEvents.recipes(event => {
  if (!Platform.isLoaded('exdeorum')) {
    return
  }

  const INPUT = 'minecraft:mud'

  // Staple vegetables, grains, roots and beans. The everyday half of a kitchen.
  const STAPLE = 0.08
  // Herbs and spices. Small, and most recipes want only a pinch.
  const HERB = 0.06
  // Berries, fruit crops and the thistle.
  const FRUIT = 0.05
  // Fruit trees. Each one is a renewable orchard, so they come slowest.
  const TREE = 0.03

  // [mod id, [[seed item, chance], ...]]
  const LANES = [
    ['herbsandharvest', [
      ['herbsandharvest:asparagus_seeds',      STAPLE],
      ['herbsandharvest:barley_seeds',         STAPLE],
      ['herbsandharvest:broccoli_seeds',       STAPLE],
      ['herbsandharvest:cabbage_seeds',        STAPLE],
      ['herbsandharvest:cauliflower_seeds',    STAPLE],
      ['herbsandharvest:celery_seeds',         STAPLE],
      ['herbsandharvest:corn_kernels',         STAPLE],
      ['herbsandharvest:cucumber_seeds',       STAPLE],
      ['herbsandharvest:eggplant_seeds',       STAPLE],
      ['herbsandharvest:green_bean_seeds',     STAPLE],
      ['herbsandharvest:green_pepper_seeds',   STAPLE],
      ['herbsandharvest:lettuce_seeds',        STAPLE],
      ['herbsandharvest:oats',                 STAPLE],
      ['herbsandharvest:onion',                STAPLE],
      ['herbsandharvest:peanuts',              STAPLE],
      ['herbsandharvest:peas',                 STAPLE],
      ['herbsandharvest:pinto_beans',          STAPLE],
      ['herbsandharvest:radish_seeds',         STAPLE],
      ['herbsandharvest:rice',                 STAPLE],
      ['herbsandharvest:rye_seeds',            STAPLE],
      ['herbsandharvest:squash_seeds',         STAPLE],
      ['herbsandharvest:sweet_potato',         STAPLE],
      ['herbsandharvest:tomato_seeds',         STAPLE],
      ['herbsandharvest:turnip_seeds',         STAPLE],
      ['herbsandharvest:zucchini_seeds',       STAPLE],

      ['herbsandharvest:basil_seeds',          HERB],
      ['herbsandharvest:bay_leaf_seeds',       HERB],
      ['herbsandharvest:chive_seeds',          HERB],
      ['herbsandharvest:cilantro_seeds',       HERB],
      ['herbsandharvest:dill_seeds',           HERB],
      ['herbsandharvest:garlic_clove',         HERB],
      ['herbsandharvest:ginger_root',          HERB],
      ['herbsandharvest:lemongrass_seeds',     HERB],
      ['herbsandharvest:mint_seeds',           HERB],
      ['herbsandharvest:mustard_seeds',        HERB],
      ['herbsandharvest:oregano_seeds',        HERB],
      ['herbsandharvest:parsley_seeds',        HERB],
      ['herbsandharvest:peppercorn_seeds',     HERB],
      ['herbsandharvest:rosemary_seeds',       HERB],
      ['herbsandharvest:sage_seeds',           HERB],
      ['herbsandharvest:thyme_seeds',          HERB],
      ['herbsandharvest:turmeric_root',        HERB],

      ['herbsandharvest:blackberry_seeds',     FRUIT],
      ['herbsandharvest:blueberry_seeds',      FRUIT],
      // Grapes are the item that plants the vine, and the mod gives them no
      // chest entry, so this is their only source anywhere in the pack.
      ['herbsandharvest:grapes',               FRUIT],
      ['herbsandharvest:pineapple_seeds',      FRUIT],
      ['herbsandharvest:raspberry_seeds',      FRUIT],
      ['herbsandharvest:strawberry_seeds',     FRUIT],
      ['herbsandharvest:thistle',              FRUIT],

      ['herbsandharvest:avocado_fruit_sapling', TREE],
      ['herbsandharvest:cherry_fruit_sapling',  TREE],
      ['herbsandharvest:cinnamon_sapling',      TREE],
      ['herbsandharvest:lemon_fruit_sapling',   TREE],
      ['herbsandharvest:lime_fruit_sapling',    TREE],
      ['herbsandharvest:orange_fruit_sapling',  TREE],
      ['herbsandharvest:peach_fruit_sapling',   TREE],
      ['herbsandharvest:pear_fruit_sapling',    TREE],
      ['herbsandharvest:plum_fruit_sapling',    TREE]
    ]],
    // Mama's Herbs and Harvest already fills the c:crops tags these four share,
    // so Farmer's Delight cooking unlocks either way. They earn their place
    // because Botany Pots ships crop data for Farmer's Delight and none for
    // Mama's, which makes these the only four a player can automate.
    ['farmersdelight', [
      ['farmersdelight:cabbage_seeds', STAPLE],
      ['farmersdelight:onion',         STAPLE],
      ['farmersdelight:rice',          STAPLE],
      ['farmersdelight:tomato_seeds',  STAPLE]
    ]]
  ]

  LANES.forEach(lane => {
    const mod = lane[0]
    if (!Platform.isLoaded(mod)) {
      return
    }
    lane[1].forEach(drop => {
      const item = drop[0]
      const chance = drop[1]
      event.custom({
        type: 'exdeorum:sieve',
        ingredient: { item: INPUT },
        mesh: { item: 'exdeorum:string_mesh' },
        result: { count: 1, id: item },
        result_amount: { type: 'minecraft:binomial', n: 1.0, p: chance }
      }).id(`kubejs:kitchen_sieve/mud/${mod}/${item.split(':')[1]}`)
    })
  })
})
