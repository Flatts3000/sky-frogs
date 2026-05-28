// Sky Frogs - Bog slime chain (Tier 3). Mirrors the Geode chain exactly.
//
// Bog frogs produce mob drops (string/bone/leather/feather/gunpowder). This chain is
// the progression SPINE - the early trickle you climb to unlock the tier's payoff
// (Mob Grinding Utils + vector plates, which become the bulk source). It is NOT meant
// to out-produce a real mob farm.
//
// Each step: 1 prior-resource Slime Milk + 4 stone + 3 sweetslime + a Bog frogspawn
// bottle -> 1 next-resource Slime in a Bucket. The first step crosses out of Geode:
// diamond Slime Milk (Geode's last resource) seeds the first Bog slime, so you can't
// reach Bog without having finished the Geode chain. The Bog frogspawn itself comes
// from the Spawnery primed with Enriched Diamond (see spawnery_primer/bog.json).
ServerEvents.recipes(event => {
  const chain = [
    ['diamond', 'string'],   // crosses out of the Geode tier
    ['string', 'bone'],
    ['bone', 'leather'],
    ['leather', 'feather'],
    ['feather', 'gunpowder']
  ]
  chain.forEach(step => {
    const from = step[0]
    const to = step[1]
    event.shapeless(
      `productivefrogs:slime_bucket[minecraft:bucket_entity_data={Variant:"productivefrogs:${to}",Category:"BOG"}]`,
      [
        `productivefrogs:slime_milk_bucket[productivefrogs:slime_variant="productivefrogs:${from}"]`,
        'minecraft:stone', 'minecraft:stone', 'minecraft:stone', 'minecraft:stone',
        'productivefrogs:sweetslime', 'productivefrogs:sweetslime', 'productivefrogs:sweetslime',
        `productivefrogs:frog_egg[productivefrogs:contained_category="bog"]`
      ]
    )
  })
})
