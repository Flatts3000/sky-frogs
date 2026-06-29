// Sky Frogs - clay block -> clay balls, the decompress half of the pair (Discord
// request, Hullah).
//
// Functional Storage compacting drawers register a compression tier only when
// BOTH directions exist as crafting recipes: compress (N items -> 1 block) and
// decompress (1 block -> N items). Clay ships with just the compress half
// (4 clay balls -> clay block); vanilla has no way back. So a compacting drawer
// won't treat clay as compactable, and a stack of farmed clay (the Bog frog's
// resource) can't pack down. Sophisticated's drawers handle it because they
// compact off their own list, not crafting recipes.
//
// This shapeless recipe adds the missing decompress half, so Functional Storage
// recognises the clay_ball <-> clay pair and clay compacts like every other
// resource.
//
//   1x clay block  ->  4x clay ball   (shapeless)

ServerEvents.recipes(event => {
  event.shapeless(Item.of('minecraft:clay_ball', 4), [
    'minecraft:clay'
  ]).id('kubejs:clay_ball_from_block')
})
