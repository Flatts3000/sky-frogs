// Sky Frogs - Bog slime chain (Tier 3). Mirrors the Geode chain.
//
// Bog is the organic/swamp species: dirt, mud, clay, moss, mycelium, lily pad,
// leather, feather - plus Industrial Foregoing plastic + pink slime when IF is loaded.
//
// The BRIDGE BOOTSTRAP (diamond -> dirt) is special: it consumes 4 MOSSY COBBLESTONE
// instead of plain stone. Mossy cobblestone is made in Mekanism's Metallurgic Infuser
// (cobblestone + bio), so crossing into Bog requires the Geode-tier Infuser - the
// mineral -> mossy -> organic transition. Every later step uses plain stone.
//
// Each step: prior Slime Milk + 4 stone + 3 sweetslime + a Bog frogspawn -> the next
// Slime in a Bucket, so you can't skip ahead. Plastic gates Industrial Foregoing and
// pink slime is the capstone; that IF tail is only chained when IF is loaded.
ServerEvents.recipes(event => {
  // Bridge bootstrap: diamond Slime Milk + mossy cobblestone -> the first Bog (dirt) slime.
  event.shapeless(
    'productivefrogs:slime_bucket[minecraft:bucket_entity_data={Variant:"productivefrogs:dirt",Category:"BOG"}]',
    [
      'productivefrogs:slime_milk_bucket[productivefrogs:slime_variant="productivefrogs:diamond"]',
      'minecraft:mossy_cobblestone', 'minecraft:mossy_cobblestone', 'minecraft:mossy_cobblestone', 'minecraft:mossy_cobblestone',
      'productivefrogs:sweetslime', 'productivefrogs:sweetslime', 'productivefrogs:sweetslime',
      'productivefrogs:frog_egg[productivefrogs:contained_category="bog"]'
    ]
  )

  // The organic chain proper (plain stone).
  const chain = [
    ['dirt', 'mud'],
    ['mud', 'clay_ball'],       // clay variant id is clay_ball (Froglight smelts to clay_ball)
    ['clay_ball', 'moss'],
    ['moss', 'mycelium'],
    ['mycelium', 'lily_pad'],
    ['lily_pad', 'leather'],
    ['leather', 'feather']
  ]
  if (Platform.isLoaded('industrialforegoing')) {
    chain.push(['feather', 'plastic'])      // plastic = the Industrial Foregoing gate
    chain.push(['plastic', 'pink_slime'])   // pink slime = Bog capstone
  }
  chain.forEach(step => {
    const from = step[0]
    const to = step[1]
    event.shapeless(
      `productivefrogs:slime_bucket[minecraft:bucket_entity_data={Variant:"productivefrogs:${to}",Category:"BOG"}]`,
      [
        `productivefrogs:slime_milk_bucket[productivefrogs:slime_variant="productivefrogs:${from}"]`,
        'minecraft:stone', 'minecraft:stone', 'minecraft:stone', 'minecraft:stone',
        'productivefrogs:sweetslime', 'productivefrogs:sweetslime', 'productivefrogs:sweetslime',
        `productivefrogs:frog_egg[productivefrogs:contained_category="bog"]`
      ]
    )
  })
})
