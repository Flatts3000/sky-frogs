// Sky Frogs - clear the empty-bucket craft remainder on PF Slime Milk buckets.
//
// PF's per-variant Slime Milk buckets (productivefrogs:<variant>_slime_milk_bucket)
// carry craftRemainder = minecraft:bucket, so using one in a crafting recipe hands the
// empty bucket BACK. In the slime-chain recipes (milk bucket -> slime in a bucket) that
// duplicated a bucket every craft: you got the slime bucket out AND the empty bucket back.
//
// The slime chains are the ONLY crafting use of milk buckets in this pack, and the intent
// was always "the milk bucket supplies the slime's bucket" (1 bucket in, 1 bucket out).
// Clearing the remainder makes that true: the milk bucket becomes the slime bucket, no dupe.
// (craftRemainder only matters in crafting; placing milk / using the Slime Milker is untouched.)
ItemEvents.modification(event => {
  event.modify(/^productivefrogs:.+_slime_milk_bucket$/, item => {
    // KubeJS exposes the setter setCraftingRemainder(...) as the JS bean property
    // `craftingRemainder`. (An earlier `craftRemainder` was a no-op - no such setter -
    // so the remainder was never cleared and the dupe persisted.)
    item.craftingRemainder = 'minecraft:air'
  })
})
