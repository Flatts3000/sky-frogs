// Sky Frogs - Bog slime chain (Tier 3). Mirrors the Geode chain.
//
// Bog is the organic/swamp species (PF recategorized it in 9d76161): dirt, mud, clay,
// moss, mycelium, lily pad, leather, feather - plus Industrial Foregoing plastic +
// pink slime when IF is loaded. This chain is the progression SPINE: each step consumes
// the prior resource's Slime Milk + 4 stone + 3 sweetslime + a Bog frogspawn -> the next
// Slime in a Bucket, so you can't skip ahead (you must milk step N to craft step N+1).
//
// The first step crosses out of Geode (diamond Slime Milk seeds the first Bog slime),
// so Bog can't start until Geode is finished. Order is earth -> water -> flora -> fauna
// -> industrial: plastic gates IF (its traditional dry-rubber recipe is removed in
// if_plastic_gate.js) and pink slime is the capstone. The IF tail is only chained when
// IF is present.
ServerEvents.recipes(event => {
  const chain = [
    ['diamond', 'dirt'],        // crosses out of the Geode tier
    ['dirt', 'mud'],
    ['mud', 'clay_ball'],       // clay variant id is clay_ball (its Froglight smelts to brick)
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
