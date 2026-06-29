// Sky Frogs - the "decompress" half of compaction pairs Functional Storage is
// missing (Discord request, Hullah).
//
// A Functional Storage compacting drawer registers a compression tier only when
// BOTH directions exist as crafting recipes: compress (N items -> 1 block) and
// decompress (1 block -> N items). A few vanilla blocks ship only the compress
// half, so a compacting drawer won't pack them down and a farmed stack just sits
// loose. (Sophisticated's drawers handle these because they compact off their
// own list, not crafting recipes.)
//
// Clay and snow are the two Hullah hit. Each ships only `N items -> block`
// (4 clay balls -> clay; 4 snowballs -> snow block), with no vanilla way back.
// These shapeless recipes add the missing decompress half so both compact like
// every other resource. Both reverse at the same 4:1 ratio their vanilla craft
// uses (1 block -> 4 items), so the loop is neutral - no duplication.
//
//   1x clay block  ->  4x clay ball
//   1x snow block  ->  4x snowball

ServerEvents.recipes(event => {
  event.shapeless(Item.of('minecraft:clay_ball', 4), [
    'minecraft:clay'
  ]).id('kubejs:clay_ball_from_block')

  event.shapeless(Item.of('minecraft:snowball', 4), [
    'minecraft:snow_block'
  ]).id('kubejs:snowball_from_block')
})
