// Sky Frogs - Cave seed-chain recipes.
//
// Each Cave resource's "slime in a bucket" is crafted from the PRIOR resource's
// Slime Milk, threading a seed-chain:
//   iron -> copper -> gold -> coal -> glow_ink_sac -> obsidian -> redstone.
// (iron is the bootstrap from the Your First Iron Ingot chapter; the steps below
// produce the rest. Lapis moved to Geode. glow_ink_sac and obsidian were
// originally skipped as off-theme/deferred, but the Ultimate Singularity demands
// every vanilla froglight resource (#79), and PF classes both as Cave - so they
// slot in before redstone, which stays the chapter capstone AND the resource the
// Geode boundary threads off (lapis takes redstone; that bridge is unchanged).)
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
    ['glow_ink_sac', 'obsidian'],
    ['obsidian', 'redstone']
  ]

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
