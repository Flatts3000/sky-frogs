// Sky Frogs - Steel Slime via the Metallurgic Infuser (optional Mekanism route, Tier 2).
//
// Steel is a Cave-frog variant (PF ships slime_variant/steel.json, Cave category).
// The thematic seed is exactly how Mekanism makes steel: infuse iron with carbon.
//   1x Bucket of Iron Slime Milk + carbon  ->  1x Steel Slime in a Bucket
// Feed the result to a Cave frog (milk it) for renewable steel. Optional route.
//
// Why the milk bucket and NOT the "Iron Slime in a Bucket": matching the slime bucket
// needs a neoforge:components ingredient on bucket_entity_data, and that ingredient is
// full-value equality - it only matches a bucket whose NBT is EXACTLY {Variant, Category}.
// That holds for a cheated/creative or crafted bucket, but NOT for one a player gets by
// catching a live slime: MobBucketItem dumps the entity's full save data (PF stat ints +
// age) into bucket_entity_data, so the compound no longer equals {Variant, Category} and
// the recipe silently refuses it. The per-variant Slime Milk bucket (PF 1.8 split) is a
// plain item id with no component to match, so it works for every player and stays
// iron-specific (no steel-from-anything exploit). The output keeps ItemStack.CODEC, which
// carries the steel variant's bucket_entity_data fine.

ServerEvents.recipes(event => {
  event.custom({
    type: 'mekanism:metallurgic_infusing',
    chemical_input: { amount: 10, chemical: 'mekanism:carbon' },
    item_input: { count: 1, item: 'productivefrogs:iron_slime_milk_bucket' },
    output: {
      id: 'productivefrogs:slime_bucket',
      count: 1,
      components: { 'minecraft:bucket_entity_data': { Variant: 'productivefrogs:steel', Category: 'CAVE' } }
    },
    per_tick_usage: false
  })
})
