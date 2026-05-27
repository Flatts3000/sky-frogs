// Sky Frogs - Cave seed-chain recipes.
//
// Each Cave resource's "slime in a bucket" is crafted from the PRIOR resource's
// Slime Milk, threading a seed-chain: iron -> copper -> gold -> coal -> redstone.
// (iron is the bootstrap from the Your First Iron Ingot chapter; the steps below
// produce the rest. Lapis moved to Geode; obsidian is deferred to the Infernal
// gate; glow_ink_sac is omitted - it's not a stone-and-ore resource.)
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
    ['coal', 'redstone']
  ]

  chain.forEach(step => {
    const from = step[0]
    const to = step[1]
    event.shapeless(
      `productivefrogs:slime_bucket[minecraft:bucket_entity_data={Variant:"productivefrogs:${to}",Category:"CAVE"}]`,
      [
        `productivefrogs:slime_milk_bucket[productivefrogs:slime_variant="productivefrogs:${from}"]`,
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
