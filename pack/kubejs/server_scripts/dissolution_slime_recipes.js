// Sky Frogs - Dissolution Chamber slime recipes (the Bog / Industrial Foregoing verb).
//
// STATUS: DISABLED 2026-05-29, pending a design call. See the BLOCKER below.
//
// Intent: once you've built the Dissolution Chamber (gated at end-of-Bog by plastic), it
// becomes the machine that makes slimes - bulk-making any unlocked Cave/Geode/Bog variant,
// and (from Tier 4 on) bootstrapping each new tier's slimes.
//
// BLOCKER (confirmed from the IF 3.6.38 + Titanium 4.0.43 jars and a client crash report):
//   IF recipes sync to the client through Titanium's CodecRecipeSerializer, which round-trips
//   the WHOLE recipe as JSON (FriendlyByteBuf.write/readJsonWithCodec, re-encoding server-side).
//   A per-variant recipe MUST match the milk bucket by its slime_variant COMPONENT - every
//   variant shares one item id (slime_milk_bucket) and one variant-agnostic milk fluid - i.e.
//   a `neoforge:components` ingredient. That ingredient's `items` HolderSet does NOT survive
//   IF's JSON round-trip: the server encodes `items` as a bare string, the client decode
//   demands a json array, and clientbound/minecraft:update_recipes throws a DecoderException
//   so the world won't load. (Mekanism's BINARY stream codec round-trips the same ingredient
//   fine - that's why steel_slime_infusing.js works - but IF's JSON path does not, and the
//   re-encode is server-side, so no recipe-JSON form fixes it.)
//
// Net: IF dissolution inputs can only be vanilla item/tag ingredients, which can't select a
// PF variant by component. Resolution: deferred pending a Productive Frogs feature that exposes
// a distinct-per-variant item handle (so a non-component recipe can pick a variant) - tracked
// at Flatts3000/productive-frogs#127. Re-enable these recipes once PF ships it. The
// tier/variant/filler data is parked here for that.

// [Category stamp, tier filler block, [variants...]]
const SLIME_TIERS = [
  ['CAVE', 'minecraft:stone', ['iron', 'copper', 'gold', 'coal', 'redstone']],
  ['GEODE', 'minecraft:gravel', ['lapis', 'tuff', 'calcite', 'amethyst', 'emerald', 'diamond']],
  ['BOG', 'minecraft:mossy_cobblestone', ['dirt', 'mud', 'clay_ball', 'moss', 'mycelium', 'lily_pad', 'leather', 'feather', 'plastic', 'pink_slime']]
]

ServerEvents.recipes(event => {
  // Disabled: see BLOCKER above. Registering nothing keeps update_recipes decodable so the
  // world loads; the IF chapter is unaffected. Re-enable once the approach is settled.
  return
})
