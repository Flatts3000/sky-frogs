// Sky Frogs - Dissolution Chamber slime recipes (Industrial Foregoing tech; chamber lives in road_to_tide.snbt).
//
// The chamber is the pack's slime engine. Each per-variant recipe threads off a PRIOR
// vanilla resource, mirroring the Cave/Geode/Bog crafting-table seed chains, just
// transposed into the IF machine:
//
//   fluid:  100 mb industrialforegoing:latex   (melt a plastic Froglight in the PF Crucible)
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
    // Chain insertion (#79): glow_ink_sac was originally skipped, but the Ultimate
    // Singularity demands all forty resources. It slots in BEFORE redstone, which
    // stays the chapter capstone and the resource Geode's lapis bridges off (that
    // boundary is unchanged). Table chain (cave_slime_chain.js) and the cave_frogs
    // quests thread identically. (obsidian, the other stray, lives in the INFERNAL
    // block below - quested at Tier 5; PF reclasses it infernal in #142.)
    ['glow_ink_sac', 'minecraft:coal'],
    // PF 1.13.0 (#161): breeze_rod slots before redstone, which stays the capstone
    // and the Geode bridge per the #79 insertion precedent. (water + lava are Cave
    // variants too, but the maintainer keeps the FLUID pair OUT of the seed chain -
    // they live as self-keyed rows below, like the modded variants.)
    ['breeze_rod',   'minecraft:glow_ink_sac'],
    ['redstone',     'minecraft:breeze_rod']
  ]],
  ['GEODE', 'minecraft:gravel', [
    ['lapis',    'minecraft:redstone'],      // bridges from Cave's last
    ['tuff',     'minecraft:lapis_lazuli'],
    ['calcite',  'minecraft:tuff'],
    ['amethyst', 'minecraft:calcite'],
    ['emerald',  'minecraft:amethyst_shard'],
    ['diamond',  'minecraft:emerald']
  ]],
  // BOG canonical lane (organics + Industrial Foregoing tail) - the spine to Tide.
  // The eight mob-drop variants are NO LONGER threaded here; they live in their own
  // terminal sub-chain at the END of this array (see "BOG mob-drop lane" below).
  // plastic re-threads off lily_pad so this lane stands alone; pink_slime stays the
  // capstone and the Tide bridge.
  ['BOG', 'minecraft:mossy_cobblestone', [
    ['dirt',       'minecraft:diamond'],            // bridges from Geode's last
    ['mud',        'minecraft:dirt'],
    ['clay_ball',  'minecraft:mud'],
    ['moss',       'minecraft:clay_ball'],
    ['mycelium',   'minecraft:moss_block'],
    ['lily_pad',   'minecraft:mycelium'],
    ['plastic',    'minecraft:lily_pad'],           // re-threaded off lily_pad (mob drops removed from this lane)
    ['pink_slime', 'industrialforegoing:plastic']   // capstone + the Tide bridge
  ]],
  ['TIDE', 'minecraft:mycelium', [
    ['prismarine',          'industrialforegoing:pink_slime'],  // bridges from Bog's last
    ['prismarine_crystals', 'minecraft:prismarine_shard'],
    ['sponge',              'minecraft:prismarine_crystals'],
    ['ink_sac',             'minecraft:sponge'],
    ['sea_pickle',          'minecraft:ink_sac'],
    // PF 1.12.0 (#155): the frozen family slots before the capstone so
    // nautilus_shell keeps the Tide->Infernal bridge. (water lived here for one
    // pin, then re-homed to Cave in PF 1.13 - the Crucible's fluids are day-one
    // business.) turtle_scute joins in 1.13.
    ['ice',                 'minecraft:sea_pickle'],
    ['snow',                'minecraft:ice'],
    ['turtle_scute',        'minecraft:snow_block'],
    ['nautilus_shell',      'minecraft:turtle_scute']
  ]],
  ['INFERNAL', 'minecraft:prismarine', [
    ['netherrack',      'minecraft:nautilus_shell'],   // bridges from Tide's last; filler is prismarine (Tide, mass-renewable - netherrack would be circular)
    // Chain insertion (#79): obsidian pairs with netherrack as the portal stones,
    // quested in infernal_frogs right after it. Chamber-only (Tier 5 has no
    // crafting-table chain). netherite_scrap stays the capstone and the resource
    // Void's ender_pearl bridges off (that boundary is unchanged). Requires PF with
    // obsidian reclassed cave -> infernal (productive-frogs#142) - the pin bump
    // lands in this same PR.
    ['obsidian',        'minecraft:netherrack'],
    ['quartz',          'minecraft:obsidian'],
    ['glowstone_dust',  'minecraft:quartz'],
    ['soul_sand',       'minecraft:glowstone_dust'],
    ['soul_soil',       'minecraft:soul_sand'],
    ['blaze',           'minecraft:soul_soil'],
    // PF 1.11.0 (#148): the Blaze resource is the ROD (primer + smelt output).
    // PF 1.13.0 (#161): ghast_tear slots before the capstone; netherite_scrap
    // stays the capstone and the Void bridge.
    ['ghast_tear',      'minecraft:blaze_rod'],
    // PF 1.14.0: magma_cream slots before the capstone per the #161 precedent.
    // (The tier's BOSS resources - nether_star, wither_skeleton_skull - stay
    // OUT of the seed chain; they live as self-keyed rows below.)
    ['magma_cream',     'minecraft:ghast_tear'],
    ['netherite_scrap', 'minecraft:magma_cream']
  ]],
  ['VOID', 'minecraft:soul_soil', [
    ['ender_pearl',   'minecraft:netherite_scrap'],     // bridges from Infernal's last; filler is soul_soil (Infernal, mass-renewable - end_stone would be circular)
    ['end_stone',     'minecraft:ender_pearl'],
    ['chorus_fruit',  'minecraft:end_stone'],
    ['echo_shard',    'minecraft:chorus_fruit'],         // prior variant chorus_fruit's resource (raw, its primer_item)
    ['sculk',         'minecraft:echo_shard'],
    // PF 1.13.0 (#161): phantom_membrane slots before the capstone.
    ['phantom_membrane', 'minecraft:sculk'],
    ['shulker_shell', 'minecraft:phantom_membrane']
  ]],
  // BOG mob-drop lane (terminal). Placed LAST in SLIME_TIERS deliberately: the
  // threading validator tracks the prior tier's last variant sequentially, and Tide
  // bridges off Bog's pink_slime - so this second BOG block must NOT sit between the
  // canonical Bog block and Tide. Here at the end, nothing bridges off it.
  //
  // `bone` bootstraps off BONE MEAL (a THREADING_EXCEPTION, like iron<-bone_meal) -
  // abundant (composter, or one skeleton bone -> 3 meal). It can't seed off its own
  // `bone` resource, because the next link `gunpowder<-bone` already claims it and the
  // chamber can't tell two same-input recipes apart (same Bog filler) - hence bone
  // meal for the seed, bone for the second. The iron<-bone_meal collision is avoided
  // because iron is Cave (stone filler) vs Bog's mossy cobblestone. gunpowder then
  // threads off bone and the rest chain down, so the un-farmable drops (armadillo_scute
  // - no armadillos; honeycomb - no bees) come from the chain.
  ['BOG', 'minecraft:mossy_cobblestone', [
    ['bone',            'minecraft:bone_meal'],     // bootstrap off bone meal (THREADING_EXCEPTION; the bone resource is claimed by gunpowder below)
    ['gunpowder',       'minecraft:bone'],
    ['rotten_flesh',    'minecraft:gunpowder'],
    ['string',          'minecraft:rotten_flesh'],
    ['leather',         'minecraft:string'],
    ['feather',         'minecraft:leather'],
    ['armadillo_scute', 'minecraft:feather'],
    ['honeycomb',       'minecraft:armadillo_scute']
  ]]
]

// MODDED variants follow a DIFFERENT law (maintainer ruling 2026-06-06, PR #106):
// the chamber input is the variant's OWN resource - self-keyed, not threaded.
// The player must create the resource through the mod's native mechanic first
// (Energizing Orb, redstone dropped on obsidian) before the frog loop can take
// over; the chamber then turns one held resource into a dedicated slime instead
// of waiting on more Cave-pool split-discovery rolls. Tier fillers per the
// standing law. Every variant here has a craft path (PR #126): the ATO metals
// chain off osmium milk (ato_slime_chain.js), fluorite enriches from calcite
// (fluorite_enriching.js), and uraninite orb-crafts from chain-farmed uranium.
//
// [category stamp, tier filler, variant, the variant's own resource, owning mod]
const MODDED_SELF_KEYED = [
  // Two VANILLA exceptions live in the self-keyed table (maintainer ruling): the
  // fluid pair stays out of the Cave seed chain, and their inputs are the FLUID
  // BUCKETS - water from a barrel, lava from the Tier 0 cobble crucible, both
  // honestly obtainable day one (unlike kelp/dripstone, which only the frogs
  // make). The validator carries a matching documented exception. 'minecraft'
  // is always loaded, so the per-row guard is a no-op for these.
  ['CAVE',     'minecraft:stone',      'water',           'minecraft:water_bucket',    'minecraft'],
  ['CAVE',     'minecraft:stone',      'lava',            'minecraft:lava_bucket',     'minecraft'],
  // The PF 1.14 BOSS resources are vanilla but deliberately self-keyed, NOT
  // threaded: PF's own design demands you prime the first slime with the real
  // drop (kill the wither, spend the egg), and a self-keyed chamber row keeps
  // exactly those economics - one earned drop per slime. Threading them off a
  // farmable resource would let the chamber bypass the boss kill entirely.
  ['INFERNAL', 'minecraft:prismarine', 'wither_skeleton_skull', 'minecraft:wither_skeleton_skull', 'minecraft'],
  ['INFERNAL', 'minecraft:prismarine', 'nether_star',     'minecraft:nether_star',     'minecraft'],
  ['VOID',     'minecraft:soul_soil',  'dragon_egg',      'minecraft:dragon_egg',      'minecraft'],
  ['VOID',     'minecraft:soul_soil',  'dragon_breath',   'minecraft:dragon_breath',   'minecraft'],
  // experience is weight 0 (a Void frog never splits it), so it can't sit in the
  // threaded VOID chain above. Self-key it on its own primer, a plain book - the
  // same item PF's slime infusion takes to turn a Void Slime into an Experience
  // one. Input == primer_item, so the validator's self-keyed law passes with no
  // SELF_KEYED_EXCEPTIONS entry (unlike water/lava, which key on a bucket).
  ['VOID',     'minecraft:soul_soil',  'experience',      'minecraft:book',            'minecraft'],
  ['CAVE',     'minecraft:stone',      'uraninite',       'powah:uraninite',           'powah'],
  ['CAVE',     'minecraft:stone',      'energized_steel', 'powah:steel_energized',     'powah'],
  ['TIDE',     'minecraft:mycelium',   'dry_ice',         'powah:dry_ice',             'powah'],
  ['INFERNAL', 'minecraft:prismarine', 'blazing',         'powah:crystal_blazing',     'powah'],
  ['INFERNAL', 'minecraft:prismarine', 'flux_dust',       'fluxnetworks:flux_dust',    'fluxnetworks'],
  ['VOID',     'minecraft:soul_soil',  'niotic',          'powah:crystal_niotic',      'powah'],
  ['VOID',     'minecraft:soul_soil',  'spirited',        'powah:crystal_spirited',    'powah'],
  ['VOID',     'minecraft:soul_soil',  'nitro',           'powah:crystal_nitro',       'powah'],
  // The census sweep (#121): every quested modded variant gets its self-keyed
  // row. Tag-primed variants (PF primer_tag) take a '#tag' input - the chamber
  // accepts tag ingredients, mirroring PF's own priming exactly. Osmium joins
  // for chamber parity (review catch on PR #126): its BOOTSTRAP stays the table
  // recipe in osmium_slime_bucket.js (redstone milk), but it scales here like
  // every other census variant - the ATO chain's root frog included.
  ['CAVE',     'minecraft:stone',      'osmium',          '#c:ingots/osmium',          'alltheores'],
  ['CAVE',     'minecraft:stone',      'aluminum',        '#c:ingots/aluminum',        'alltheores'],
  ['CAVE',     'minecraft:stone',      'lead',            '#c:ingots/lead',            'alltheores'],
  ['CAVE',     'minecraft:stone',      'nickel',          '#c:ingots/nickel',          'alltheores'],
  ['CAVE',     'minecraft:stone',      'silver',          '#c:ingots/silver',          'alltheores'],
  ['CAVE',     'minecraft:stone',      'tin',             '#c:ingots/tin',             'alltheores'],
  ['CAVE',     'minecraft:stone',      'uranium',         '#c:ingots/uranium',         'alltheores'],
  ['CAVE',     'minecraft:stone',      'zinc',            '#c:ingots/zinc',            'alltheores'],
  // fluorite takes the Mekanism gem ITEM, not the #c:gems/fluorite TAG. ATO and
  // Mekanism both register a fluorite into that tag, but only mekanism:fluorite_gem
  // is obtainable here (PF's froglight smelts to it; calcite enriches to it; ATO's
  // needs ore-gen a void skyblock lacks). The concrete item makes the recipe
  // reverse-resolvable in JEI's "uses" page - a tag input there left the calcite
  // -> fluorite -> slime path looking absent (Discord, Dergib). Validator exempts
  // it via SELF_KEYED_EXCEPTIONS.
  ['GEODE',    'minecraft:gravel',     'fluorite',        'mekanism:fluorite_gem',     'mekanism'],
  // silicon is RS's base material (smelt nether quartz -> refinedstorage:silicon).
  // Self-keyed on the concrete item, NOT its #c:silicon primer tag: the tag also
  // covers ae2:silicon, which this pack never ships (no AE2), so a tag input would
  // half-resolve and leave the smelt-quartz path looking absent in JEI's "uses"
  // page - the same fix fluorite got. Validator exempts it via SELF_KEYED_EXCEPTIONS.
  ['GEODE',    'minecraft:gravel',     'silicon',         'refinedstorage:silicon',    'refinedstorage'],
  ['GEODE',    'minecraft:gravel',     'basic_processor', 'refinedstorage:basic_processor', 'refinedstorage'],
  ['GEODE',    'minecraft:gravel',     'improved_processor', 'refinedstorage:improved_processor', 'refinedstorage'],
  ['GEODE',    'minecraft:gravel',     'advanced_processor', 'refinedstorage:advanced_processor', 'refinedstorage'],
  ['INFERNAL', 'minecraft:prismarine', 'refined_obsidian', '#c:ingots/refined_obsidian', 'mekanism'],
  ['INFERNAL', 'minecraft:prismarine', 'refined_glowstone', '#c:ingots/refined_glowstone', 'mekanism'],
  ['INFERNAL', 'minecraft:prismarine', 'quartz_enriched_iron', 'refinedstorage:quartz_enriched_iron', 'refinedstorage'],
  // Just Dire Things (PF 1.15, #188): four materials + three Crucible fuels.
  // Materials are tag-primed (ferricore/blazegold/eclipsealloy) or item-primed
  // (celestigem); the fuels prime off JDT's coal tiers (coal_t2/t3/t4) - the
  // Froglight melts in the Crucible straight to the refined fuel, skipping
  // JDT's own coal-refining chain. Self-keyed per the make-it-first law.
  ['CAVE',     'minecraft:stone',      'ferricore',     '#c:ingots/ferricore',     'justdirethings'],
  ['INFERNAL', 'minecraft:prismarine', 'blazegold',     '#c:ingots/blazegold',     'justdirethings'],
  ['INFERNAL', 'minecraft:prismarine', 'celestigem',    'justdirethings:celestigem', 'justdirethings'],
  ['INFERNAL', 'minecraft:prismarine', 'blaze_ember',   'justdirethings:coal_t2',  'justdirethings'],
  ['VOID',     'minecraft:soul_soil',  'eclipsealloy',  '#c:ingots/eclipsealloy',  'justdirethings'],
  ['VOID',     'minecraft:soul_soil',  'voidflame',     'justdirethings:coal_t3',  'justdirethings'],
  ['VOID',     'minecraft:soul_soil',  'eclipse_ember', 'justdirethings:coal_t4',  'justdirethings']
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

  // The modded self-keyed rows (see MODDED_SELF_KEYED above). Same chamber shape,
  // each additionally guarded on its owning mod so an absent mod leaves no recipe
  // referencing missing ids.
  MODDED_SELF_KEYED.forEach(row => {
    const category = row[0]
    const filler = row[1]
    const variant = row[2]
    const ownResource = row[3]
    const ownerMod = row[4]
    if (!Platform.isLoaded(ownerMod)) {
      return
    }

    // '#'-prefixed inputs are TAGS (tag-primed variants); plain ids are items.
    const inputIng = ownResource.startsWith('#')
      ? { tag: ownResource.substring(1) }
      : { item: ownResource }
    event.custom({
      type: 'industrialforegoing:dissolution_chamber',
      input: [
        inputIng,
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
        components: { 'minecraft:bucket_entity_data': { Variant: `productivefrogs:${variant}`, Category: category } }
      },
      processingTime: 200
    }).id(`kubejs:dissolution_slime/${category.toLowerCase()}_${variant}`)
  })
})
