// Sky Frogs - Fluorite from calcite (maintainer ruling, PR #126).
//
// Mekanism's fluorite only comes from ore processing, and a void skyblock has
// no fluorite ore - without this, the Fluorite Slime was split-discovery-only
// and the Sister Ponds census couldn't be finished. The Enrichment Chamber
// (the same machine the ore-doubling line starts on) presses frog-farmed
// CALCITE into fluorite: both are Geode minerals, and calcite is
// mass-renewable off the Calcite frog by the time Mekanism is running.
//
// 1:1 is fine as economics - this is the bootstrap, not the farm. One gem
// primes the Fluorite Slime (the chamber's self-keyed row takes #c:gems/
// fluorite), and from there the Fluorite frog IS the fluorite mine.
//
// Recipe shape verified against the Mekanism 1.21.1 jar (enriching recipes
// flatten the ingredient into the input object: {count, item|tag}).

ServerEvents.recipes(event => {
  if (!Platform.isLoaded('mekanism')) {
    return
  }
  event.custom({
    type: 'mekanism:enriching',
    input: { count: 1, item: 'minecraft:calcite' },
    output: { count: 1, id: 'mekanism:fluorite_gem' }
  }).id('kubejs:mekanism/fluorite_from_calcite')
})
