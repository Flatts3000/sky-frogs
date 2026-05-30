// Sky Frogs - Slime Milk catalyst recipe fit-ups for skyblock.
//
// Productive Frogs v1.7.0 adds four Slime Milk catalysts (Count / Speed / Quantity /
// Infinite Count) you drop into a placed Slime Milk source to buff it. Three of the four
// craft from items the player has by the Geode tier (sweetslime + bone_meal / sugar /
// diamond), but PF's QUANTITY catalyst calls for glowstone_dust - and on a void skyblock
// glowstone is Infernal-gated (PF's nether roster), so it can't be made at the diamond
// point where the catalysts are introduced.
//
// Re-issue the Quantity catalyst with REDSTONE instead (the Cave gem-chain capstone, so it's
// abundant well before diamonds; "redstone = amplify/signal" suits "more slimes per spawn").
// Same override pattern as storage_quartz_free.js / if_plastic_gate.js: PF's default glowstone
// recipe stays intact for other packs; the pack just swaps it for the skyblock-attainable one.
//
// PRESERVES PF's `productivefrogs:config_enabled / milk_catalysts` condition on the override,
// so if a player or server admin disables the catalyst feature in PF's config, both the
// original and our replacement vanish in lockstep (rather than leaking Quantity-only as the
// one craftable catalyst while Count/Speed/Infinite disappear).
//
// Last verified against Productive Frogs v1.7.0 (data/productivefrogs/recipe/quantity_catalyst.json).
// Re-verify the shape and condition fields on every PF pin bump.
ServerEvents.recipes(event => {
  if (!Platform.isLoaded('productivefrogs')) {
    return
  }
  // Remove PF's glowstone recipe (by id) and re-issue it glowstone-free, with the same
  // milk_catalysts config condition the original carried.
  event.remove({ id: 'productivefrogs:quantity_catalyst' })
  event.custom({
    'neoforge:conditions': [
      { type: 'productivefrogs:config_enabled', config: 'milk_catalysts' }
    ],
    type: 'minecraft:crafting_shapeless',
    category: 'misc',
    ingredients: [
      { item: 'productivefrogs:sweetslime' },
      { item: 'productivefrogs:sweetslime' },
      { item: 'minecraft:redstone' }
    ],
    result: {
      id: 'productivefrogs:quantity_catalyst',
      count: 1
    }
  }).id('kubejs:quantity_catalyst_redstone')
})
