// Sky Frogs - Geode seed-chain recipes.
//
// Mirrors cave_slime_chain.js one tier up. The first step crosses out of the Cave:
// the Cave's last resource (redstone) Slime Milk seeds the first Geode slime (lapis),
// so the Cave's final lesson feeds the Geode frog's first. From there the gem chain
// runs lapis -> amethyst -> emerald -> diamond, each step converting the prior gem's
// Slime Milk into the next gem's Slime in a Bucket.
//
// Per-step recipe (shapeless, 9 items):
//   1x <prior> Slime Milk bucket  (supplies the bucket; the first step uses Cave redstone milk)
//   4x stone                      (abundant filler, same as the Cave chain)
//   3x sweetslime                 (the frog-coaxing binder)
//   1x Geode frogspawn bottle     (the Geode-category seed)
//   -> 1x <next> Slime in a Bucket (stamped Category GEODE)
//
// Variant ids verified against productivefrogs-1.5.2 slime_variant data: lapis,
// amethyst, emerald, and diamond are all category "geode". The lapis -> ... steps
// are inert until the Geode Frogs chapter quests guide them; they self-gate on
// needing the prior gem's milk.

ServerEvents.recipes(event => {
  // [from-milk variant, output slime-bucket variant]
  const chain = [
    ['redstone', 'lapis'],
    ['lapis', 'amethyst'],
    ['amethyst', 'emerald'],
    ['emerald', 'diamond']
  ]

  chain.forEach(step => {
    const from = step[0]
    const to = step[1]
    event.shapeless(
      `productivefrogs:slime_bucket[minecraft:bucket_entity_data={Variant:"productivefrogs:${to}",Category:"GEODE"}]`,
      [
        `productivefrogs:slime_milk_bucket[productivefrogs:slime_variant="productivefrogs:${from}"]`,
        'minecraft:stone',
        'minecraft:stone',
        'minecraft:stone',
        'minecraft:stone',
        'productivefrogs:sweetslime',
        'productivefrogs:sweetslime',
        'productivefrogs:sweetslime',
        'productivefrogs:frog_egg[productivefrogs:contained_category="geode"]'
      ]
    )
  })
})
