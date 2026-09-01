// Sky Frogs - All the Ores seed-chain recipes (maintainer ruling, PR #126).
//
// The seven ATO metals have no ore on a void skyblock and no native recipe for
// their ingots - without a chain, their slimes were split-discovery-only and
// the Sister Ponds census couldn't be finished. This chain makes them
// craftable the same way the Cave metals are: each metal's "slime in a bucket"
// is crafted from the PRIOR metal's Slime Milk, threading off OSMIUM (which
// osmium_slime_bucket.js bootstraps from redstone milk, end of the Cave chain):
//   osmium -> aluminum -> lead -> nickel -> silver -> tin -> uranium -> zinc.
// Alphabetical past osmium; uranium landing late is a happy accident - it
// gates Powah's uraninite (the Orb presses uranium ingots into uraninite).
//
// All eight are CAVE-category variants (metals belong to the stone-and-ore
// frog), so the recipe shape is cave_slime_chain.js verbatim:
//   1x <prior> Slime Milk bucket
//   4x stone
//   3x sweetslime
//   1x Cave frogspawn bottle
//   -> 1x <next> Slime in a Bucket
//
// The chamber's MODDED_SELF_KEYED rows (dissolution_slime_recipes.js) stay the
// scaling path: once a metal's first frog exists, one ingot + the chamber
// skips the milk chain entirely. This table chain is the bootstrap.
//
// Both identity carriers are stamped (#247): the nested bucket_entity_data.Variant
// that the Slime Milker and the release path read, and the flat
// productivefrogs:slime_variant component PF 1.26.0 made the stable identity key.
// The six gateway quests match the component under fuzzy, so a bucket minted with
// only the tag would not complete the quest it satisfied before.

ServerEvents.recipes(event => {
  if (!Platform.isLoaded('alltheores')) {
    return
  }

  // [from-milk variant, output slime-bucket variant]
  const chain = [
    ['osmium',   'aluminum'],
    ['aluminum', 'lead'],
    ['lead',     'nickel'],
    ['nickel',   'silver'],
    ['silver',   'tin'],
    ['tin',      'uranium'],
    ['uranium',  'zinc']
  ]

  chain.forEach(step => {
    const from = step[0]
    const to = step[1]
    event.shapeless(
      `productivefrogs:slime_bucket[minecraft:bucket_entity_data={Variant:"productivefrogs:${to}",Category:"CAVE"},productivefrogs:slime_variant="productivefrogs:${to}"]`,
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
