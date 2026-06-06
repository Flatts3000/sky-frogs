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
// The seven builders' generators (stone, cobblestone, granite, diorite,
// andesite, basalt, cobbled deepslate) stay as shipped. Removals are
// id-anchored to ^cobblegengalore: per the anti.js rule, so any future
// curated kubejs:* re-adds would be untouchable by these filters.

ServerEvents.recipes(event => {
  if (!Platform.isLoaded('cobblegengalore')) {
    return
  }

  event.remove({ id: 'cobblegengalore:blockgen/netherrack' })
  event.remove({ id: 'cobblegengalore:blockgen/obsidian' })
  event.remove({ id: 'cobblegengalore:blockgen/tuff' })
})
