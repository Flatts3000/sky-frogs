// Sky Frogs - Osmium Slime in a Bucket (Mekanism bootstrap recipe).
//
// Osmium is Mekanism's entry metal and a Cave-category PF variant (frog-only on a
// void skyblock; the ore is unreachable). PF's osmium variant is gated on All the
// Ores being loaded (it is - `ato`), and primes off the `c:ingots/osmium` tag.
//
// This is the Mekanism chapter's opener: it seeds the first Osmium Slime off the
// Cave frog the same way cave_slime_chain.js seeds the metals - redstone Slime Milk
// (the Cave chain's last resource) + stone + sweetslime + a Cave frogspawn bottle.
// Run it through the Slime Milker, place the milk, feed the slimes to a Cave Frog,
// and smelt the Froglight for osmium - no ore ever mined. Resolves the Cave->Mekanism
// gate (Mekanism stops needing a missing ore node and hands the player osmium itself).
//
// Output stamps Variant + Category into bucket_entity_data to match PF's JEI subtype.

ServerEvents.recipes(event => {
  event.shapeless(
    'productivefrogs:slime_bucket[minecraft:bucket_entity_data={Variant:"productivefrogs:osmium",Category:"CAVE"}]',
    [
      'productivefrogs:slime_milk_bucket[productivefrogs:slime_variant="productivefrogs:redstone"]',
      'minecraft:stone',
      'minecraft:stone',
      'minecraft:stone',
      'minecraft:stone',
      'productivefrogs:sweetslime',
      'productivefrogs:sweetslime',
      'productivefrogs:sweetslime',
      'productivefrogs:frog_egg[productivefrogs:contained_category="cave"]'
    ]
  )
})
