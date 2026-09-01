// Sky Frogs - Geode seed-chain recipes.
//
// Mirrors cave_slime_chain.js one tier up. The first step crosses out of the Cave:
// the Cave's last resource (redstone) Slime Milk seeds the first Geode slime (lapis),
// so the Cave's final lesson feeds the Geode frog's first. From there the Geode chain
// runs lapis -> tuff -> calcite -> amethyst -> emerald -> diamond - the geode-shell
// blocks first, then the crystal and the gems - each step converting the prior
// resource's Slime Milk into the next one's Slime in a Bucket.
//
// Per-step recipe (shapeless, 9 items):
//   1x <prior> Slime Milk bucket  (supplies the bucket; the first step uses Cave redstone milk)
//   4x gravel                      (the Ex Deorum block you sieve gems from; the gem tier's filler)
//   3x sweetslime                 (the frog-coaxing binder)
//   1x Geode frogspawn bottle     (the Geode-category seed)
//   -> 1x <next> Slime in a Bucket (stamped Category GEODE)
//
// Variant ids verified against productivefrogs-1.5.2 slime_variant data: lapis,
// tuff, calcite, amethyst, emerald, and diamond are all category "geode". The
// lapis -> ... steps are inert until the Geode Frogs chapter quests guide them;
// they self-gate on needing the prior resource's milk.
//
// Both identity carriers are stamped (#247): the nested bucket_entity_data.Variant
// that the Slime Milker and the release path read, and the flat
// productivefrogs:slime_variant component PF 1.26.0 made the stable identity key.
// The six gateway quests match the component under fuzzy, so a bucket minted with
// only the tag would not complete the quest it satisfied before.

ServerEvents.recipes(event => {
  // [from-milk variant, output slime-bucket variant]
  const chain = [
    ['redstone', 'lapis'],
    ['lapis', 'tuff'],
    ['tuff', 'calcite'],
    ['calcite', 'amethyst'],
    ['amethyst', 'emerald'],
    ['emerald', 'diamond']
  ]

  chain.forEach(step => {
    const from = step[0]
    const to = step[1]
    event.shapeless(
      `productivefrogs:slime_bucket[minecraft:bucket_entity_data={Variant:"productivefrogs:${to}",Category:"GEODE"},productivefrogs:slime_variant="productivefrogs:${to}"]`,
      [
        `productivefrogs:${from}_slime_milk_bucket`,
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
        'minecraft:gravel',
        'productivefrogs:sweetslime',
        'productivefrogs:sweetslime',
        'productivefrogs:sweetslime',
        'productivefrogs:frog_egg[productivefrogs:contained_category="geode"]'
      ]
    )
  })
})
