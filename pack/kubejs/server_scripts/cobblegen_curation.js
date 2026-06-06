// Sky Frogs - Cobblegen Galore curation (#90).
//
// Cobblegen Galore ships as the builders' stone-generator mod (the in-pack
// answer to the #85 ruling-5 want), but three of its default blockgen recipes
// produce FROG resources:
//
//   netherrack -> Infernal frog (the tier's first resource)
//   obsidian   -> Infernal frog (the v0.5.0 chain, #79)
//   tuff       -> Geode frog
//
// All three are seeded amplifiers (each generator needs its own output block
// as the modifier), so the tier gates technically hold - but the maintainer
// ruling on #90 (2026-06-06) is the strict reading of #85 ruling 1 ("no easy
// way to make resources that need to be made using frogs"): once seeded, a
// generator mass-produces the resource without a frog farm, which hollows out
// the singularity endgame's "1000 of each = proof you automated every farm."
// Obsidian goes too, despite vanilla water+lava parity, for consistency: it
// IS an Infernal frog resource and a singularity input.
//
// Mechanism: DEFAULT-DENY. One removal strips every cobblegengalore:blockgen/*
// recipe EXCEPT the seven builders' generators (stone, cobblestone, granite,
// diorite, andesite, basalt, cobbled deepslate) - a negative lookahead instead
// of the opolis strip-type-and-re-add pattern, so no recipe JSON is duplicated
// (no codec-drift risk) but a future mod update adding, say, blockgen/end_stone
// or blockgen/mycelium dies here by default instead of shipping unreviewed.
// This also covers the jar's compat recipes (blockgen/ae2/*, atm/*, create/*,
// xycraft/*): their mods aren't in the pack today, but if one ever lands, its
// generator stays dead until explicitly allowlisted. The removal is id-anchored
// to ^cobblegengalore: per the anti.js rule, so future curated kubejs:* re-adds
// would be untouchable by this filter.

ServerEvents.recipes(event => {
  if (!Platform.isLoaded('cobblegengalore')) {
    return
  }

  // Allowlist (the seven): stone, cobblestone, granite, diorite, andesite,
  // basalt, cobbled_deepslate. Everything else under blockgen/ is removed -
  // today that is netherrack, obsidian, tuff (the #90 three) plus the
  // absent-mod compat set.
  event.remove({
    id: /^cobblegengalore:blockgen\/(?!(?:stone|cobblestone|granite|diorite|andesite|basalt|cobbled_deepslate)$).+/
  })
})
