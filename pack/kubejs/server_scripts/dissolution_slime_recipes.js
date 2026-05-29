// Sky Frogs - Dissolution Chamber slime recipes (the Bog / Industrial Foregoing verb).
//
// Once you've built the Dissolution Chamber (gated at the end of Bog: its frame needs
// plastic from the Bog plastic-frog, see if_plastic_gate.js), it becomes the machine
// that makes slimes. This registers, for every slime variant you've already unlocked,
// an IF Dissolution Chamber recipe that pours out that variant's Slime in a Bucket:
//
//   fluid:  100 mb industrialforegoing:latex   (tap it from logs with a Fluid Extractor)
//   items:  1x that variant's Slime Milk bucket (the variant SELECTOR - PF's milk fluid
//             is variant-agnostic, so the variant has to ride on the bucket ITEM)
//           4x the tier filler block            (Cave=stone, Geode=gravel, Bog=mossy cobblestone)
//           3x productivefrogs:sweetslime
//   -> 1x   that variant's Slime in a Bucket    (stamped Variant + Category)
//
// The milk is the gate: you only own a variant's milk after unlocking it through the
// crafting-table seed-chain, so the Chamber can't skip progression - only mass-produce
// what you've earned, by machine instead of by hand.
//
// GOING FORWARD: from Tier 4 (Tide) on, this same machine is the BOOTSTRAP too - the
// prior tier's milk seeds the next tier's first slime, replacing the crafting-table
// seed-chain pattern. Those rows get added to the table below when Tide ships.
//
// Authored as raw recipe JSON via event.custom, reusing the proven component-recipe
// pattern from steel_slime_infusing.js: a neoforge:components ingredient matches the
// milk bucket by its slime_variant, and the ItemStack-codec output carries the
// bucket_entity_data component (IF/Mekanism both keep components through ItemStack.CODEC).
// VERIFY in JEI after /reload that each recipe shows the right milk in and slime out.

// [Category stamp, tier filler block, [variants...]]
const SLIME_TIERS = [
  ['CAVE', 'minecraft:stone', ['iron', 'copper', 'gold', 'coal', 'redstone']],
  ['GEODE', 'minecraft:gravel', ['lapis', 'tuff', 'calcite', 'amethyst', 'emerald', 'diamond']],
  ['BOG', 'minecraft:mossy_cobblestone', ['dirt', 'mud', 'clay_ball', 'moss', 'mycelium', 'lily_pad', 'leather', 'feather', 'plastic', 'pink_slime']]
  // Tier 4+ (Tide) and beyond: dissolution becomes the bootstrap - add the tier here
  // (prior-tier milk -> next-tier first slime) once those variants ship.
]

ServerEvents.recipes(event => {
  // The whole mechanic is an Industrial Foregoing machine, so it only exists with IF.
  if (!Platform.isLoaded('industrialforegoing')) {
    return
  }

  SLIME_TIERS.forEach(tier => {
    const category = tier[0]
    const filler = tier[1]
    const variants = tier[2]

    variants.forEach(variant => {
      const v = `productivefrogs:${variant}`
      event.custom({
        type: 'industrialforegoing:dissolution_chamber',
        input: [
          // The variant selector: any Slime Milk bucket carrying this slime_variant.
          // neoforge:components is the proven component-match ingredient in this pack
          // (see steel_slime_infusing.js); it subset-matches on the listed components.
          { count: 1, type: 'neoforge:components', items: 'productivefrogs:slime_milk_bucket', components: { 'productivefrogs:slime_variant': v } },
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
