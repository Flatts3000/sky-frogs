// Sky Frogs - compaction support Functional Storage doesn't pick up on its own
// (Discord requests, Hullah). Two separate gaps, two separate fixes below.

ServerEvents.recipes(event => {

  // --- Gap 1: missing decompress crafting half (clay, snow) ---
  //
  // A compacting drawer registers a standard tier only when BOTH directions
  // exist as crafting recipes: compress (N items -> 1 block) and decompress
  // (1 block -> N items). A few vanilla blocks ship only the compress half, so a
  // compacting drawer won't pack them down and a farmed stack just sits loose.
  // (Sophisticated's drawers handle these because they compact off their own
  // list, not crafting recipes.)
  //
  // Clay and snow are the two Hullah hit. Each ships only `N items -> block`
  // (4 clay balls -> clay; 4 snowballs -> snow block), with no vanilla way back.
  // These shapeless recipes add the missing decompress half so both compact like
  // every other resource, at the same 4:1 ratio vanilla compresses (no dupe).
  //
  //   1x clay block  ->  4x clay ball
  //   1x snow block  ->  4x snowball
  event.shapeless(Item.of('minecraft:clay_ball', 4), [
    'minecraft:clay'
  ]).id('kubejs:clay_ball_from_block')

  event.shapeless(Item.of('minecraft:snowball', 4), [
    'minecraft:snow_block'
  ]).id('kubejs:snowball_from_block')

  // --- Gap 2: a non-standard ratio the drawer's auto-detect skips (coal, charcoal) ---
  //
  // Opolis Utilities adds Mini Coal and Mini Charcoal and ships both crafting
  // directions for each (1 coal -> 8 mini; 8 mini -> 1 coal; same for charcoal).
  // But the drawer's automatic tier detection only understands the standard
  // 4:1 (2x2) and 9:1 (3x3) crafting ratios, so the 8:1 Mini <-> full step is
  // invisible to it and a compacting drawer ignores Mini Coal/Charcoal entirely.
  // Functional Storage exposes a `custom_compacting` recipe type for exactly this -
  // it declares a tier directly, ratio and all.
  //
  // Coal spans three tiers; charcoal only two (vanilla has no charcoal block):
  //
  //   8x mini coal      <->  1x coal      <->  (9x coal) 1x block of coal
  //   8x mini charcoal  <->  1x charcoal
  //
  // The Coal <-> Block tier is normally auto-detected from vanilla, but Coal now
  // carries a custom tier (as the higher_input above it), so we declare the block
  // tier too - that keeps the whole chain on the explicit path and forms cleanly
  // in a single drawer. Pure representation change, no duplication.
  event.custom({
    type: 'functionalstorage:custom_compacting',
    higher_input: { count: 1, id: 'minecraft:coal' },
    lower_input: { count: 8, id: 'opolisutilities:mini_coal' }
  }).id('kubejs:compacting/coal_from_mini_coal')

  event.custom({
    type: 'functionalstorage:custom_compacting',
    higher_input: { count: 1, id: 'minecraft:coal_block' },
    lower_input: { count: 9, id: 'minecraft:coal' }
  }).id('kubejs:compacting/coal_block_from_coal')

  event.custom({
    type: 'functionalstorage:custom_compacting',
    higher_input: { count: 1, id: 'minecraft:charcoal' },
    lower_input: { count: 8, id: 'opolisutilities:mini_charcoal' }
  }).id('kubejs:compacting/charcoal_from_mini_charcoal')
})
