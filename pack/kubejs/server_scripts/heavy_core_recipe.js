// Sky Frogs - the Heavy Core press (#127, maintainer pick: chamber-pressed).
//
// The Heavy Core only drops from Ominous Vaults in Trial Chambers - structures
// that never generate on a void skyblock - so the Mace was unobtainable even
// after PF 1.13 made its other half (the breeze rod) frog-farmable. The
// Dissolution Chamber presses one from dense mass-renewables instead:
//
//   fluid:  100 mb industrialforegoing:latex
//   items:  4x iron block   (Cave ore, 36 ingots of dense)
//           4x prismarine   (Tide stone, 16 shards)
//   -> 1x   Heavy Core
//
// Tide-gated by construction: the chamber itself is built at the Tide
// boundary, and prismarine is the Tide frog's opening resource. That lands
// the Mace in the same tier as the jetpack (Take Flight) - the weapon that
// scales with fall height arrives exactly when the player learns to fly.
// Quested as the Take Flight side branch (The Heavy Core -> Drop the Hammer).
ServerEvents.recipes(event => {
  if (!Platform.isLoaded('industrialforegoing')) {
    return
  }
  event.custom({
    type: 'industrialforegoing:dissolution_chamber',
    input: [
      { item: 'minecraft:iron_block' },
      { item: 'minecraft:iron_block' },
      { item: 'minecraft:iron_block' },
      { item: 'minecraft:iron_block' },
      { item: 'minecraft:prismarine' },
      { item: 'minecraft:prismarine' },
      { item: 'minecraft:prismarine' },
      { item: 'minecraft:prismarine' }
    ],
    inputFluid: { fluid: 'industrialforegoing:latex', amount: 100 },
    output: {
      id: 'minecraft:heavy_core',
      count: 1
    },
    processingTime: 200
  }).id('kubejs:heavy_core_press')
})
