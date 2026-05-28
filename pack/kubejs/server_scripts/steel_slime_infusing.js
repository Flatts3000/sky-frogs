// Sky Frogs - Steel Slime via the Metallurgic Infuser (optional Mekanism route).
//
// Steel is a Cave-frog variant (PF 1.5.2), and the thematic way to seed a Steel
// Slime is exactly how Mekanism makes steel: infuse iron with carbon. This adds a
// metallurgic_infusing recipe (the Infuser built earlier in the chapter):
//   1x Iron Slime in a Bucket + carbon  ->  1x Steel Slime in a Bucket
// Feed the result to the Cave frog for renewable steel. Optional side route, not
// required to finish the chapter.
//
// Carbon chemical id (mekanism:carbon) confirmed via the chemical_conversion recipe;
// chemical_input { amount, chemical } shape confirmed against alloy/infused.json.
//
// FEASIBILITY NOTE (load-test on reload, watch the game log for a parse error):
// the item_input + output carry bucket_entity_data NBT. If Mekanism's recipe codec
// rejects NBT item ingredients/outputs, the fallback is a KubeJS crafting recipe
// gated behind the player owning a Metallurgic Infuser.

ServerEvents.recipes(event => {
  event.custom({
    type: 'mekanism:metallurgic_infusing',
    chemical_input: { amount: 10, chemical: 'mekanism:carbon' },
    item_input: {
      count: 1,
      item: 'productivefrogs:slime_bucket',
      components: { 'minecraft:bucket_entity_data': { Variant: 'productivefrogs:iron', Category: 'CAVE' } }
    },
    output: {
      count: 1,
      id: 'productivefrogs:slime_bucket',
      components: { 'minecraft:bucket_entity_data': { Variant: 'productivefrogs:steel', Category: 'CAVE' } }
    },
    per_tick_usage: false
  })
})
