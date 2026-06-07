// Sky Frogs - Cave seed-chain recipes.
//
// Each Cave resource's "slime in a bucket" is crafted from the PRIOR resource's
// Slime Milk, threading a seed-chain:
//   iron -> copper -> gold -> coal -> glow_ink_sac -> breeze_rod -> redstone.
// (iron is the bootstrap from the Your First Iron Ingot chapter; the steps below
// produce the rest. Lapis moved to Geode. glow_ink_sac was originally skipped as
// off-theme, but the Ultimate Singularity demands every vanilla froglight
// resource (#79) - it slots in before redstone, which stays the chapter capstone
// AND the resource the Geode boundary threads off (lapis takes redstone; that
// bridge is unchanged). Obsidian is NOT here: it's an Infernal-category variant
// (PF 1.10.0), chamber-only, threaded netherrack -> obsidian in
// dissolution_slime_recipes.js and quested in infernal_frogs.)
//
// Per-step recipe (shapeless, 9 items):
//   1x <prior> Slime Milk bucket  (what you convert from; supplies the bucket too)
//   4x stone                      (on-brand for the Cave / stone-and-ore frog)
//   3x sweetslime                 (the frog-coaxing binder)
//   1x Cave frogspawn bottle      (the Cave-category seed)
//   -> 1x <next> Slime in a Bucket
//
// The output stamps both Variant and Category into bucket_entity_data to match
// PF's JEI slime-bucket subtype (keyed on the full bucket_entity_data string).

ServerEvents.recipes(event => {
  // [from-milk variant, output slime-bucket variant]
  const chain = [
    ['iron', 'copper'],
    ['copper', 'gold'],
    ['gold', 'coal'],
    ['coal', 'glow_ink_sac'],
    // PF 1.13.0 (#161): breeze_rod joins before redstone (the capstone + Geode
    // bridge). water + lava are deliberately NOT chain steps - the fluid pair is
    // self-keyed in the chamber (dissolution_slime_recipes.js) per maintainer ruling.
    ['glow_ink_sac', 'breeze_rod'],
    ['breeze_rod', 'redstone']
  ]

  // The FLUID PAIR (maintainer ruling): water + lava slimes craft like the chain
  // steps but keyed on the FLUID BUCKET instead of a prior Slime Milk - water
  // from a barrel, lava from the Tier 0 cobble crucible. Outside the seed chain
  // on purpose; vanilla bucket remainders apply (the empty bucket comes back).
  const fluids = { water: 'minecraft:water_bucket', lava: 'minecraft:lava_bucket' }
  Object.keys(fluids).forEach(variant => {
    event.shapeless(
      `productivefrogs:slime_bucket[minecraft:bucket_entity_data={Variant:"productivefrogs:${variant}",Category:"CAVE"}]`,
      [
        fluids[variant],
        'minecraft:stone',
        'minecraft:stone',
        'minecraft:stone',
        'minecraft:stone',
        'productivefrogs:sweetslime',
        'productivefrogs:sweetslime',
        'productivefrogs:sweetslime',
        'productivefrogs:frog_egg[productivefrogs:contained_category="cave"]'
      ]
    )
  })

  chain.forEach(step => {
    const from = step[0]
    const to = step[1]
    event.shapeless(
      `productivefrogs:slime_bucket[minecraft:bucket_entity_data={Variant:"productivefrogs:${to}",Category:"CAVE"}]`,
      [
        `productivefrogs:${from}_slime_milk_bucket`,
        'minecraft:stone',
        'minecraft:stone',
        'minecraft:stone',
        'minecraft:stone',
        'productivefrogs:sweetslime',
        'productivefrogs:sweetslime',
        'productivefrogs:sweetslime',
        'productivefrogs:frog_egg[productivefrogs:contained_category="cave"]'
      ]
    )
  })
})
