// Sky Frogs - deterministic flint from gravel (#159, Discord request).
//
// A void skyblock has no reliable flint: vanilla only drops it as a ~10% chance
// when breaking gravel, and the pack disables Ex Deorum sieving. Flint is needed
// early (Flint & Steel for the Nether portal, etc.), so this shapeless recipe
// gives a dependable supply from frog-farmable gravel (the Geode-tier filler,
// renewable via the cobblegen/frog loop).
//
//   3x gravel  ->  1x flint   (shapeless)

ServerEvents.recipes(event => {
  event.shapeless('minecraft:flint', [
    'minecraft:gravel',
    'minecraft:gravel',
    'minecraft:gravel'
  ]).id('kubejs:flint_from_gravel')
})
