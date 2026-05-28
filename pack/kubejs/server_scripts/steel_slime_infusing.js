// Sky Frogs - Steel Slime (optional Mekanism side route, Tier 2).
//
// Steel is a Cave-frog variant (PF ships data/.../slime_variant/steel.json,
// primer c:ingots/steel). The thematic seed mirrors how Mekanism makes steel
// itself: iron + carbon.
//
// This was originally a mekanism:metallurgic_infusing recipe, but Mekanism's
// infusing codec carries NO item NBT on either its input or its output - it would
// strip the bucket_entity_data and emit a variant-less slime bucket the Slime
// Milker can't read, breaking the route. So it's a crafting recipe instead (the
// player has built the Infuser by this point in the chapter, so the flavor holds):
//   1x Iron Slime in a Bucket + 1 carbon (coal or charcoal) -> 1x Steel Slime in a Bucket
// Feed the result to a Cave frog (milk it) for renewable steel. Optional; not
// required to finish the chapter.

ServerEvents.recipes(event => {
  const steelSlime = 'productivefrogs:slime_bucket[minecraft:bucket_entity_data={Variant:"productivefrogs:steel",Category:"CAVE"}]'
  const ironSlime = 'productivefrogs:slime_bucket[minecraft:bucket_entity_data={Variant:"productivefrogs:iron",Category:"CAVE"}]'
  // Carbon = coal or charcoal; one recipe each so the player can use either.
  event.shapeless(steelSlime, [ironSlime, 'minecraft:coal'])
  event.shapeless(steelSlime, [ironSlime, 'minecraft:charcoal'])
})
