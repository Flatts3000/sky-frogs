// Sky Frogs - hide the severed Opolis loot boxes from the recipe viewer (#115).
//
// Maintainer ruling: NO loot boxes from BBL, anywhere. #117's server side already
// stops the drops (Mob Drop Chance = 1.0) and empties the payout tables; this is
// the last visible surface - the three box items sitting in the JEI ingredient
// list as craft-nothing bait. RecipeViewerEvents is KubeJS 7's viewer-agnostic
// API (covers JEI here, EMI/REI if the pack ever swaps).
//
// The catalogue/wallet/B-Bucks items keep their DISABLED tooltips and stay
// LISTED on purpose: they gate a whole machine the player can still see in
// world if cheated, and the tooltip explains the design. The boxes are pure
// loot bait with no story to tell - they just vanish.

RecipeViewerEvents.removeEntries('item', event => {
  if (!Platform.isLoaded('opolisutilities')) {
    return
  }
  event.remove('opolisutilities:basic_loot_box')
  event.remove('opolisutilities:advanced_loot_box')
  event.remove('opolisutilities:elite_loot_box')
})
