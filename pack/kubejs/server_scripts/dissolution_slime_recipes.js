// Sky Frogs - Dissolution Chamber slime recipes (the Bog / Industrial Foregoing verb).
//
// The chamber is the slime engine for Tier 4 (Tide) and beyond. Each per-variant recipe
// threads off a PRIOR vanilla resource, mirroring the Cave/Geode/Bog crafting-table seed
// chains, just transposed into the IF machine:
//
//   fluid:  100 mb industrialforegoing:latex   (tap it from logs with a Fluid Extractor)
//   items:  1x prior resource                   (the previous TIER's last resource for the
//                                                 FIRST variant in a tier; the previous
//                                                 VARIANT's resource for each step after)
//           4x tier filler block
//           3x productivefrogs:sweetslime
//   -> 1x   that variant's Slime in a Bucket    (stamped Variant + Category)
//
// Resource-keyed (NOT milk-keyed): the variant's smelted resource is a distinct vanilla
// item id, so it round-trips through IF/Titanium's JSON recipe codec fine. A milk-keyed
// recipe would need a neoforge:components ingredient, which IF can't network-sync (PF
// declined adding a per-variant component-free handle - see PF issue #127 - so the
// chamber operates on the froglight -> resource production loop instead). The output
// slime bucket carries its Variant + Category components via ItemStack.CODEC, which
// handles JSON components broadly; that's the one round-trip to keep an eye on when
// the first Tier 4 row lands.
//
// Tier 1-3 (Cave/Geode/Bog) stay on their crafting-table seed-chains (cave_slime_chain.js
// / geode_slime_chain.js / bog_slime_chain.js); retrofitting them to chamber-only would
// be a wash (spend an iron ingot to make an iron slime) and they're already shipped.
// The chamber rule starts at Tier 4 - exactly when the player has just earned it by
// clearing Bog.

// [Category stamp, tier filler block, [[variant, prior-resource], ...]]
//
// The FIRST variant in a tier consumes the PRIOR TIER'S LAST resource (Bog ends at
// productivefrogs:pink_slime, so Tide's first variant takes pink_slime). Each subsequent
// row consumes the variant ABOVE it in the list. Order within a tier is the progression
// order, the same way Cave's chain is iron -> copper -> gold -> coal -> redstone.
//
// No rows yet - design pending per tier:
const SLIME_TIERS = [
  // ['TIDE', 'minecraft:<filler>', [
  //   ['<first-variant>', 'industrialforegoing:pink_slime'],
  //   ['<next-variant>',  'minecraft:<first-variant-resource>'],
  //   ...
  // ]],
  // ['INFERNAL', 'minecraft:<filler>', [...]],
  // ['VOID', 'minecraft:<filler>', [...]],
]

ServerEvents.recipes(event => {
  if (!Platform.isLoaded('industrialforegoing')) {
    return
  }

  SLIME_TIERS.forEach(tier => {
    const category = tier[0]
    const filler = tier[1]
    const rows = tier[2]

    rows.forEach(row => {
      const variant = row[0]
      const priorResource = row[1]
      const v = `productivefrogs:${variant}`

      event.custom({
        type: 'industrialforegoing:dissolution_chamber',
        input: [
          { item: priorResource },
          { item: filler },
          { item: filler },
          { item: filler },
          { item: filler },
          { item: 'productivefrogs:sweetslime' },
          { item: 'productivefrogs:sweetslime' },
          { item: 'productivefrogs:sweetslime' }
        ],
        inputFluid: { fluid: 'industrialforegoing:latex', amount: 100 },
        output: {
          id: 'productivefrogs:slime_bucket',
          count: 1,
          components: { 'minecraft:bucket_entity_data': { Variant: v, Category: category } }
        },
        processingTime: 200
      }).id(`kubejs:dissolution_slime/${variant}`)
    })
  })
})
