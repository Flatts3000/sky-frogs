// Sky Frogs - Pillar 1: disable mining/sieving shortcuts.
//
// Sky Frogs' identity is "frogs are the resource path." Anything that lets a player
// generate resources by another route gets removed. Tier 0 is a dark-room slime farm,
// NOT sieving, so Ex Deorum's DEFAULT sieve recipes are disabled here. Ex Deorum
// stays in the pack for crucibles + barrels (the second-water-source mechanic) and the
// porcelain bucket.
//
// ONE deliberate exception (#76): builder_sieve.js re-adds a curated string-mesh
// lane over dirt/moss dropping cosmetic flora only (saplings, bamboo, flowers) -
// decor variety, zero progression resources. Every removal below is id-anchored to
// ^exdeorum: so it can only ever strip the mod's DEFAULTS, never that curated lane.
//
// All IDs/recipe-types below were verified against Ex Deorum's 1.21.1 source.

// Blocks whose right-click we cancel for fake players (prevents automation cheese on
// the Ex Deorum blocks we keep - barrels/crucibles). Extend as automation mods land.
const fake_player_block_mods = ['exdeorum']

BlockEvents.rightClicked(event => {
  const { player, block } = event
  const modId = String(block.id).split(':')[0]
  if (player.fake && fake_player_block_mods.includes(modId)) {
    event.cancel()
  }
})

ServerEvents.recipes(event => {
  // RULE FOR EVERY REMOVAL IN THIS BLOCK: anchor it to the source mod's id space.
  // Unanchored removals also eat curated kubejs:* re-adds (builder_sieve.js) -
  // silently, with no error. Use these constants; do not inline a bare filter.
  const EXDEORUM_DEFAULTS = /^exdeorum:/
  const MEKANISM_DEFAULTS = /^mekanism:/

  // 1. Kill the DEFAULT sieving drop tables (ores, gems, seeds - the progression
  //    bypass). The curated kubejs:builder_sieve/* lane is untouchable by these.
  event.remove({ type: 'exdeorum:sieve', id: EXDEORUM_DEFAULTS })
  event.remove({ type: 'exdeorum:compressed_sieve', id: EXDEORUM_DEFAULTS })

  // 2. Strip the sieve BLOCK crafting recipes. Ex Deorum generates one per wood
  //    material (oak_sieve, acacia_compressed_sieve, mechanical_sieve, ...); the
  //    regex catches all of them without enumerating. builder_sieve.js re-adds
  //    ONLY the oak sieve, under a kubejs id this regex cannot match. The
  //    Mechanical Sieve stays uncraftable - the builders' lane is manual-only.
  event.remove({ id: /^exdeorum:[a-z0-9_]+_sieve$/ })

  // 3. Strip mesh crafting. builder_sieve.js re-adds the STRING mesh only; the
  //    other five stay dead weight and keep their tooltip.
  event.remove({ output: '#exdeorum:sieve_meshes', id: EXDEORUM_DEFAULTS })

  // 4. Mining shortcuts from tech mods. The Mekanism Digital Miner is an automated ore
  //    miner - a direct bypass of the frog loop - so strip its recipe now that Mekanism
  //    is in the pack. (Inert in the void overworld, but live once the player reaches
  //    the Nether/End, so disable it outright per Pillar 1.)
  event.remove({ output: 'mekanism:digital_miner', id: MEKANISM_DEFAULTS })

  // 5. The IF Laser Drill family (playtest catch 2026-06-06: the scaffold note
  //    below claimed this content was absent, but IF ships it and JEI showed the
  //    Ore Laser Base live). Double Pillar 1 violation: laser_drill_ore is 46
  //    recipes of ores/gems/resources from thin air, and laser_drill_fluid
  //    produces LAVA and ether (fluid generation is planned FROG business, the
  //    #85 ruling-4 screen). Strip the production recipe types AND the three
  //    machine crafts. Laser lenses stay craftable - inert glass decor without
  //    a base to socket into.
  const IF_DEFAULTS = /^industrialforegoing:/
  event.remove({ type: 'industrialforegoing:laser_drill_ore', id: IF_DEFAULTS })
  event.remove({ type: 'industrialforegoing:laser_drill_fluid', id: IF_DEFAULTS })
  event.remove({ id: 'industrialforegoing:laser_drill' })
  event.remove({ id: 'industrialforegoing:ore_laser_base' })
  event.remove({ id: 'industrialforegoing:fluid_laser_base' })

  // --- Scaffold: uncomment per mod as more automated-mining mods land.
  //     (Kept inert until the mods exist so KubeJS doesn't log unmatched-recipe noise.)
  // event.remove({ type: 'actuallyadditions:mining_lens' })       // Actually Additions
})

// Flag the meshes in JEI/tooltips so the omission reads as intentional, not a bug.
// Per-ID (not tag) because that's the verified-working modifyTooltips signature.
// The STRING mesh is the one live mesh (the builders' lane) and gets its own text.
ItemEvents.modifyTooltips(event => {
  const meshes = [
    'exdeorum:flint_mesh',
    'exdeorum:iron_mesh',
    'exdeorum:golden_mesh',
    'exdeorum:diamond_mesh',
    'exdeorum:netherite_mesh'
  ]
  meshes.forEach(id => event.add(id, [
    Text.red('⚠ Disabled in Sky Frogs'),
    Text.gray('Only the String Mesh sifts here (decor flora).'),
    Text.gray('Resources come from the frogs - build a slime farm.')
  ]))

  // Shared header for the two live builders'-lane items so the copy can't drift.
  const builderSieveTooltip = [
    Text.green('The Builders\' Sieve'),
    Text.gray('Sift dirt or moss for saplings, bamboo, and garden flora.'),
    Text.gray('Decor only, manual only - resources still come from the frogs.')
  ]
  event.add('exdeorum:string_mesh', builderSieveTooltip)
  event.add('exdeorum:oak_sieve', builderSieveTooltip)

  event.add('exdeorum:mechanical_sieve', [
    Text.red('⚠ Disabled in Sky Frogs'),
    Text.gray('The builders\' sieve lane is manual-only.')
  ])

  event.add('mekanism:digital_miner', [
    Text.red('⚠ Disabled in Sky Frogs'),
    Text.gray('Automated mining bypasses the frogs - not in this pack.')
  ])

  // The IF laser drill family (see the recipes block). Same eager-resolution
  // caveat as opolis_curation.js: guard on the mod before naming its ids in
  // event.add. RHINO QUIRK (seen live on /reload): a const declared INSIDE the
  // if-block throws "TypeError: redeclaration of var" - KubeJS's Rhino scopes
  // const to the function, so block-level consts collide with their own hoisted
  // binding. Declare at callback top level like every other const in this file.
  const laserTooltip = [
    Text.red('⚠ Disabled in Sky Frogs'),
    Text.gray('Ores and fluids from a laser bypass the frogs - not in this pack.')
  ]
  if (Platform.isLoaded('industrialforegoing')) {
    event.add('industrialforegoing:laser_drill', laserTooltip)
    event.add('industrialforegoing:ore_laser_base', laserTooltip)
    event.add('industrialforegoing:fluid_laser_base', laserTooltip)
  }
})
