// Sky Frogs - Tide slime chain (Tier 4). Mirrors the Bog chain.
//
// Tide is the aquatic species: prismarine, prismarine crystals, sponge, ink sac,
// sea pickle, nautilus shell (all vanilla; PF's Mythic-Metals aquarium variant is
// auto-excluded - that mod isn't in the pack).
//
// Tide's themed crafting block is MYCELIUM (Cave=stone, Geode=gravel, Bog=mossy
// cobblestone). Mycelium is a Bog chain resource, so by Tier 4 it's mass-renewable
// off the Bog frog loop - the swamp tier literally seeds the shore tier's filler.
// (This deliberately departs from the earlier "filler is a plain non-resource block"
// convention; it's safe because mycelium is fully produced within Bog, before Tide,
// so there's no circular dependency.)
//
// Each step: prior Slime Milk + 4 mycelium + 3 sweetslime + a Tide frogspawn -> the
// next Slime in a Bucket, so you can't skip ahead. The bridge bootstrap consumes
// pink_slime (Bog's capstone) Slime Milk, so it needs Industrial Foregoing loaded
// (PF's pink_slime variant is IF-conditioned); IF is a required pack dependency, the
// guard below is dev-safety only. The vanilla-aquatic chain steps need no guard.
ServerEvents.recipes(event => {
  // Bridge bootstrap: pink_slime Slime Milk + mycelium -> the first Tide (prismarine) slime.
  // Gated on IF because the pink_slime variant (and thus its milk bucket) is IF-only.
  if (Platform.isLoaded('industrialforegoing')) {
    event.shapeless(
      'productivefrogs:slime_bucket[minecraft:bucket_entity_data={Variant:"productivefrogs:prismarine",Category:"TIDE"}]',
      [
        'productivefrogs:pink_slime_slime_milk_bucket',
        'minecraft:mycelium', 'minecraft:mycelium', 'minecraft:mycelium', 'minecraft:mycelium',
        'productivefrogs:sweetslime', 'productivefrogs:sweetslime', 'productivefrogs:sweetslime',
        'productivefrogs:frog_egg[productivefrogs:contained_category="tide"]'
      ]
    )
  }

  // The aquatic chain proper (mycelium filler, same as the bridge). All vanilla variants.
  const chain = [
    ['prismarine', 'prismarine_crystals'],
    ['prismarine_crystals', 'sponge'],
    ['sponge', 'ink_sac'],
    ['ink_sac', 'sea_pickle'],
    ['sea_pickle', 'nautilus_shell']
  ]
  chain.forEach(step => {
    const from = step[0]
    const to = step[1]
    event.shapeless(
      `productivefrogs:slime_bucket[minecraft:bucket_entity_data={Variant:"productivefrogs:${to}",Category:"TIDE"}]`,
      [
        `productivefrogs:${from}_slime_milk_bucket`,
        'minecraft:mycelium', 'minecraft:mycelium', 'minecraft:mycelium', 'minecraft:mycelium',
        'productivefrogs:sweetslime', 'productivefrogs:sweetslime', 'productivefrogs:sweetslime',
        `productivefrogs:frog_egg[productivefrogs:contained_category="tide"]`
      ]
    )
  })
})
