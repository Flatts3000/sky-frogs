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
ServerEvents.recipes(event => {
  if (!Platform.isLoaded('productivefrogs')) {
    return
  }
  // Remove PF's glowstone recipe (by id) and re-issue it glowstone-free.
  event.remove({ id: 'productivefrogs:quantity_catalyst' })
  event.shapeless(
    'productivefrogs:quantity_catalyst',
    ['productivefrogs:sweetslime', 'productivefrogs:sweetslime', 'minecraft:redstone']
  )
})
