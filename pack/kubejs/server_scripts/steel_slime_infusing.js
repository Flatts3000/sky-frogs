// Sky Frogs - Steel Slime via the Metallurgic Infuser (optional Mekanism route, Tier 2).
//
// Steel is a Cave-frog variant (PF ships slime_variant/steel.json, Cave category).
// The thematic seed is exactly how Mekanism makes steel: infuse iron with carbon.
//
// Mekanism's recipe serializer uses ItemStack.CODEC for the output (the full 1.21
// codec, so bucket_entity_data NBT survives) and a vanilla Ingredient for the item
// input - so a neoforge:components ingredient matches the iron slime SPECIFICALLY
// (not any slime bucket, which would be a steel-from-anything exploit):
//   1x Iron Slime in a Bucket + carbon  ->  1x Steel Slime in a Bucket
// Feed the result to a Cave frog (milk it) for renewable steel. Optional route.

ServerEvents.recipes(event => {
  event.custom({
    type: 'mekanism:metallurgic_infusing',
    chemical_input: { amount: 10, chemical: 'mekanism:carbon' },
    item_input: {
      count: 1,
      type: 'neoforge:components',
      items: 'productivefrogs:slime_bucket',
      components: { 'minecraft:bucket_entity_data': { Variant: 'productivefrogs:iron', Category: 'CAVE' } }
    },
    output: {
      id: 'productivefrogs:slime_bucket',
      count: 1,
      components: { 'minecraft:bucket_entity_data': { Variant: 'productivefrogs:steel', Category: 'CAVE' } }
    },
    per_tick_usage: false
  })
})
