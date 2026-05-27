// Sky Frogs - Iron Slime in a Bucket (Tier 1 bootstrap recipe).
//
// PF primes an Iron Slime with an iron ingot, but a void skyblock has no iron -
// a chicken-and-egg soft-lock. This recipe conjures the first Iron Slime straight
// into a bucket from things the player already has after the Welcome chapter: a Cave
// frogspawn bottle, slime balls, string, bone meal, and the empty bucket handed out
// by the Slime Milker quest. Run the result through the Slime Milker for Iron Slime
// Milk, place that, and Iron Slimes spawn on their own - no iron ever spent.
//
// The output carries the iron variant in bucket_entity_data.Variant, which is exactly
// what the Slime Milker reads (ResourceTadpoleBucketItem#readVariant) to stamp the
// matching Iron Slime Milk.

ServerEvents.recipes(event => {
  event.shaped(
    'productivefrogs:slime_bucket[minecraft:bucket_entity_data={Variant:"productivefrogs:iron",Category:"CAVE"}]',
    [
      'SBS',
      'TKT',
      'SFS'
    ],
    {
      S: 'minecraft:slime_ball',
      B: 'minecraft:bone_meal',
      T: 'minecraft:string',
      F: 'productivefrogs:frog_egg[productivefrogs:contained_category="cave"]',
      K: 'minecraft:bucket'
    }
  )
})
