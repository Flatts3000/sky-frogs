// Sky Frogs - Dissolution Chamber slime recipes (Industrial Foregoing tech; chamber lives in road_to_tide.snbt).
//
// The chamber is the pack's slime engine. Each per-variant recipe threads off a PRIOR
// vanilla resource, mirroring the Cave/Geode/Bog crafting-table seed chains, just
// transposed into the IF machine:
//
//   fluid:  100 mb industrialforegoing:latex   (tap it from logs with a Fluid Extractor)
//   items:  1x prior resource                   (see threading note below)
//           4x tier filler block
//           3x productivefrogs:sweetslime
//   -> 1x   that variant's Slime in a Bucket    (stamped Variant + Category)
//
// Threading:
//   - WITHIN a tier, each variant's chamber input is the PRIOR variant's resource
//     (e.g. copper takes iron_ingot, gold takes copper_ingot).
//   - AT a tier boundary, the first variant of the new tier takes the LAST resource
//     of the prior tier (Geode's lapis takes redstone; Bog's dirt takes diamond; Tide's
//     first variant will take pink_slime when Tide ships).
//   - IRON is the exception: there's no pre-Cave resource to thread off, so iron's
//     chamber input is BONE MEAL - the same "starter" ingredient the crafting-table
//     bootstrap (iron_slime_bucket.js) uses. Bone meal is abundant by Bog (composter +
//     organic mats), so chamber-bootstrapping iron at end-of-Bog is a clean payoff.
//
// Resource-keyed (NOT milk-keyed): the smelted resource is a distinct vanilla item id,
// so it round-trips through IF/Titanium's JSON recipe codec. A milk-keyed recipe would
// need a neoforge:components ingredient, which IF can't network-sync (PF declined the
// per-variant component-free handle; productive-frogs#127 closed won't-fix). The
// output slime bucket carries Variant + Category via ItemStack.CODEC, which handles
// JSON components broadly; verify the round-trip stays green on the first Tier 4 row.
//
// Why parallel to the crafting-table chains (and not replacing them): the chamber is
// only available at end-of-Bog (its frame needs plastic), so Cave/Geode/Bog players
// don't have it yet - the crafting tables remain the path TO the chamber. Once you
// have the chamber, you can automate the same slime production via hopper-fed input
// instead of hand-crafting. The economics are a 1:1 wash; the value is automation.

// [Category stamp, tier filler block, [[variant, prior-resource], ...]]
//
// Rows in the order a tier's chain runs. The first row of each tier consumes the prior
// tier's last resource (or bone_meal for iron's bootstrap); every other row consumes
// the variant above it.
const SLIME_TIERS = [
  ['CAVE', 'minecraft:stone', [
    ['iron',     'minecraft:bone_meal'],   // bootstrap (also crafted at table via iron_slime_bucket.js)
    ['copper',   'minecraft:iron_ingot'],
    ['gold',     'minecraft:copper_ingot'],
    ['coal',     'minecraft:gold_ingot'],
    ['redstone', 'minecraft:coal']
  ]],
  ['GEODE', 'minecraft:gravel', [
    ['lapis',    'minecraft:redstone'],      // bridges from Cave's last
    ['tuff',     'minecraft:lapis_lazuli'],
    ['calcite',  'minecraft:tuff'],
    ['amethyst', 'minecraft:calcite'],
    ['emerald',  'minecraft:amethyst_shard'],
    ['diamond',  'minecraft:emerald']
  ]],
  ['BOG', 'minecraft:mossy_cobblestone', [
    ['dirt',       'minecraft:diamond'],            // bridges from Geode's last
    ['mud',        'minecraft:dirt'],
    ['clay_ball',  'minecraft:mud'],
    ['moss',       'minecraft:clay_ball'],
    ['mycelium',   'minecraft:moss_block'],
    ['lily_pad',   'minecraft:mycelium'],
    ['leather',    'minecraft:lily_pad'],
    ['feather',    'minecraft:leather'],
    ['plastic',    'minecraft:feather'],
    ['pink_slime', 'industrialforegoing:plastic']
  ]],
  ['TIDE', 'minecraft:mycelium', [
    ['prismarine',          'industrialforegoing:pink_slime'],  // bridges from Bog's last
    ['prismarine_crystals', 'minecraft:prismarine_shard'],
    ['sponge',              'minecraft:prismarine_crystals'],
    ['ink_sac',             'minecraft:sponge'],
    ['sea_pickle',          'minecraft:ink_sac'],
    ['nautilus_shell',      'minecraft:sea_pickle']
  ]],
  ['INFERNAL', 'minecraft:prismarine', [
    ['netherrack',      'minecraft:nautilus_shell'],   // bridges from Tide's last; filler is prismarine (Tide, mass-renewable - netherrack would be circular)
    ['quartz',          'minecraft:netherrack'],
    ['glowstone_dust',  'minecraft:quartz'],
    ['soul_sand',       'minecraft:glowstone_dust'],
    ['soul_soil',       'minecraft:soul_sand'],
    ['blaze',           'minecraft:soul_soil'],
    ['netherite_scrap', 'minecraft:blaze_powder']
  ]],
  ['VOID', 'minecraft:soul_soil', [
    ['ender_pearl',   'minecraft:netherite_scrap'],     // bridges from Infernal's last; filler is soul_soil (Infernal, mass-renewable - end_stone would be circular)
    ['end_stone',     'minecraft:ender_pearl'],
    ['chorus_fruit',  'minecraft:end_stone'],
    ['echo_shard',    'minecraft:chorus_fruit'],         // prior variant chorus_fruit's resource (raw, its primer_item)
    ['sculk',         'minecraft:echo_shard'],
    ['shulker_shell', 'minecraft:sculk']
  ]]
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
      // Category-prefixed id so a future-tier variant can never accidentally collide on
      // bare name with a Cave/Geode/Bog row (variant ids are unique within a tier today,
      // but the slime_variant registry has no global-uniqueness guarantee across tiers).
      }).id(`kubejs:dissolution_slime/${category.toLowerCase()}_${variant}`)
    })
  })
})
