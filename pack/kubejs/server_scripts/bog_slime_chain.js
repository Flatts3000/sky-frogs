// Sky Frogs - Bog slime chain (Tier 3). Mirrors the Geode chain.
//
// Bog is the organic/swamp species: dirt, mud, clay, moss, mycelium, lily pad,
// leather, feather, then the mob-drop wing (armadillo scute, honeycomb, bone,
// gunpowder, rotten flesh, string) - plus Industrial Foregoing plastic + pink
// slime when IF is loaded.
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
// guard below is dev-safety only (PF's plastic/pink_slime variants are IF-conditioned).
ServerEvents.recipes(event => {
  // Bridge bootstrap: diamond Slime Milk + mossy cobblestone -> the first Bog (dirt) slime.
  event.shapeless(
    'productivefrogs:slime_bucket[minecraft:bucket_entity_data={Variant:"productivefrogs:dirt",Category:"BOG"}]',
    [
      'productivefrogs:diamond_slime_milk_bucket',
      'minecraft:mossy_cobblestone', 'minecraft:mossy_cobblestone', 'minecraft:mossy_cobblestone', 'minecraft:mossy_cobblestone',
      'productivefrogs:sweetslime', 'productivefrogs:sweetslime', 'productivefrogs:sweetslime',
      'productivefrogs:frog_egg[productivefrogs:contained_category="bog"]'
    ]
  )

  // The organic chain proper (mossy cobblestone, same as the bridge).
  const chain = [
    ['dirt', 'mud'],
    ['mud', 'clay_ball'],       // clay variant id is clay_ball (Froglight smelts to clay_ball)
    ['clay_ball', 'moss'],
    ['moss', 'mycelium'],
    ['mycelium', 'lily_pad'],
    ['lily_pad', 'leather'],
    ['leather', 'feather'],
    // PF 1.13.0 (#161): the Bog stragglers - same insertion as the chamber chain.
    ['feather', 'armadillo_scute'],
    ['armadillo_scute', 'honeycomb'],
    // PF 1.14.0: the mob-drop wave - same insertion as the chamber chain.
    ['honeycomb', 'bone'],
    ['bone', 'gunpowder'],
    ['gunpowder', 'rotten_flesh'],
    ['rotten_flesh', 'string']
  ]
  if (Platform.isLoaded('industrialforegoing')) {
    chain.push(['string', 'plastic'])       // plastic = the Industrial Foregoing gate
    chain.push(['plastic', 'pink_slime'])   // pink slime = Bog capstone
  }
  chain.forEach(step => {
    const from = step[0]
    const to = step[1]
    event.shapeless(
      `productivefrogs:slime_bucket[minecraft:bucket_entity_data={Variant:"productivefrogs:${to}",Category:"BOG"}]`,
      [
        `productivefrogs:${from}_slime_milk_bucket`,
        'minecraft:mossy_cobblestone', 'minecraft:mossy_cobblestone', 'minecraft:mossy_cobblestone', 'minecraft:mossy_cobblestone',
        'productivefrogs:sweetslime', 'productivefrogs:sweetslime', 'productivefrogs:sweetslime',
        `productivefrogs:frog_egg[productivefrogs:contained_category="bog"]`
      ]
    )
  })
})
