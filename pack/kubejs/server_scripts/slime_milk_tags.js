// Sky Frogs - #productivefrogs:slime_milk_buckets item tag.
//
// PF v1.8 split Slime Milk into per-variant bucket items (productivefrogs:<variant>_slime_milk_bucket)
// but ships no tag that groups them. The End Cake override (void_recipes.js) wants "any Slime Milk"
// in its milk slots, so we build the tag here with a regex over whatever buckets are actually
// registered - no hardcoded variant list, so PF adding/removing compat variants can't break it.
// If PF ever ships this tag natively the add() just merges into it, so this stays safe to keep.
ServerEvents.tags('item', event => {
  event.add('productivefrogs:slime_milk_buckets', /^productivefrogs:[a-z0-9_]+_slime_milk_bucket$/)
})
