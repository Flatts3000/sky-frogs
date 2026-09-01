// Sky Frogs - Bog slime chain (Tier 3). Mirrors the Geode chain.
//
// Bog is the organic/swamp species, split into two lanes:
//  - canonical (the spine to Tide): dirt, mud, clay, moss, mycelium, lily pad, then
//    Industrial Foregoing plastic + pink slime when IF is loaded.
//  - mob-drop lane (terminal): bone (the bootstrap, made from bone meal), then
//    gunpowder, rotten flesh, string, leather, feather, armadillo scute, honeycomb -
//    chained off bone so the un-farmable drops (scute/honeycomb) need no special mob.
//
// Bog's themed crafting block is MOSSY COBBLESTONE (Cave uses plain stone). Every step
// - the diamond -> dirt bridge bootstrap and every chain step after it - takes 4 mossy
// cobblestone, made in Mekanism's Metallurgic Infuser or Enrichment Chamber
// (cobblestone + bio). So the whole tier leans on the Geode-era Mekanism machines: the
// mineral -> mossy -> organic transition.
//
// Each step: prior Slime Milk + 4 mossy cobblestone + 3 sweetslime + a Bog frogspawn ->
// the next Slime in a Bucket, so you can't skip ahead. Plastic gates Industrial Foregoing
// and pink slime is the capstone. IF is a required pack dependency; the Platform.isLoaded
// guard below is dev-safety only (PF's plastic/pink_slime variants are IF-conditioned).//
// Both identity carriers are stamped (#247): the nested bucket_entity_data.Variant
// that the Slime Milker and the release path read, and the flat
// productivefrogs:slime_variant component PF 1.26.0 made the stable identity key.
// The six gateway quests match the component under fuzzy, so a bucket minted with
// only the tag would not complete the quest it satisfied before.
ServerEvents.recipes(event => {
  // Bridge bootstrap: diamond Slime Milk + mossy cobblestone -> the first Bog (dirt) slime.
  event.shapeless(
    'productivefrogs:slime_bucket[minecraft:bucket_entity_data={Variant:"productivefrogs:dirt",Category:"BOG"},productivefrogs:slime_variant="productivefrogs:dirt"]',
    [
      'productivefrogs:diamond_slime_milk_bucket',
      'minecraft:mossy_cobblestone', 'minecraft:mossy_cobblestone', 'minecraft:mossy_cobblestone', 'minecraft:mossy_cobblestone',
      'productivefrogs:sweetslime', 'productivefrogs:sweetslime', 'productivefrogs:sweetslime',
      'productivefrogs:frog_egg[productivefrogs:contained_category="bog"]'
    ]
  )

  // bone bootstrap: the mob-drop lane seeds off BONE MEAL (abundant - composter, or
  // one skeleton bone -> 3 meal), like the dirt bridge above - NOT from a prior frog's
  // milk. It seeds off bone meal rather than bone because the next link (bone milk ->
  // gunpowder) claims the bone resource; two recipes on the same input would collide.
  // The rest of the lane chains off bone below, so the un-farmable drops
  // (armadillo_scute - no armadillos; honeycomb - no bees) come down-chain.
  event.shapeless(
    'productivefrogs:slime_bucket[minecraft:bucket_entity_data={Variant:"productivefrogs:bone",Category:"BOG"},productivefrogs:slime_variant="productivefrogs:bone"]',
    [
      'minecraft:bone_meal',
      'minecraft:mossy_cobblestone', 'minecraft:mossy_cobblestone', 'minecraft:mossy_cobblestone', 'minecraft:mossy_cobblestone',
      'productivefrogs:sweetslime', 'productivefrogs:sweetslime', 'productivefrogs:sweetslime',
      'productivefrogs:frog_egg[productivefrogs:contained_category="bog"]'
    ]
  )

  // Two lanes (mirrors the chamber chain in dissolution_slime_recipes.js):
  //  - canonical (organics + Industrial Foregoing tail): the spine to Tide.
  //  - mob-drop lane: terminal, bootstrapped off the bone slime above.
  // Every [from, to] step below is an adjacent pair in the chamber chain, so the
  // Q-TABLE-CHAIN-MIRROR check stays green.
  const chain = [
    // canonical lane
    ['dirt', 'mud'],
    ['mud', 'clay_ball'],       // clay variant id is clay_ball (Froglight smelts to clay_ball)
    ['clay_ball', 'moss'],
    ['moss', 'mycelium'],
    ['mycelium', 'lily_pad'],
    // mob-drop lane (off the bone bootstrap), terminal
    ['bone', 'gunpowder'],
    ['gunpowder', 'rotten_flesh'],
    ['rotten_flesh', 'string'],
    ['string', 'leather'],
    ['leather', 'feather'],
    ['feather', 'armadillo_scute'],
    ['armadillo_scute', 'honeycomb']
  ]
  if (Platform.isLoaded('industrialforegoing')) {
    chain.push(['lily_pad', 'plastic'])     // plastic re-threads off lily_pad (the Industrial Foregoing gate)
    chain.push(['plastic', 'pink_slime'])   // pink slime = Bog capstone + Tide bridge
  }
  chain.forEach(step => {
    const from = step[0]
    const to = step[1]
    event.shapeless(
      `productivefrogs:slime_bucket[minecraft:bucket_entity_data={Variant:"productivefrogs:${to}",Category:"BOG"},productivefrogs:slime_variant="productivefrogs:${to}"]`,
      [
        `productivefrogs:${from}_slime_milk_bucket`,
        'minecraft:mossy_cobblestone', 'minecraft:mossy_cobblestone', 'minecraft:mossy_cobblestone', 'minecraft:mossy_cobblestone',
        'productivefrogs:sweetslime', 'productivefrogs:sweetslime', 'productivefrogs:sweetslime',
        `productivefrogs:frog_egg[productivefrogs:contained_category="bog"]`
      ]
    )
  })
})
