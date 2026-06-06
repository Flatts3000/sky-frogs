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
  // 1. Kill the DEFAULT sieving drop tables (ores, gems, seeds - the progression
  //    bypass). id-anchored to ^exdeorum: so the curated kubejs:builder_sieve/*
  //    lane (added in builder_sieve.js) is untouchable by these filters.
  event.remove({ type: 'exdeorum:sieve', id: /^exdeorum:/ })
  event.remove({ type: 'exdeorum:compressed_sieve', id: /^exdeorum:/ })

  // 2. Strip the sieve BLOCK crafting recipes. Ex Deorum generates one per wood
  //    material (oak_sieve, acacia_compressed_sieve, mechanical_sieve, ...); the
  //    regex catches all of them without enumerating. builder_sieve.js re-adds
  //    ONLY the oak sieve, under a kubejs id this regex cannot match. The
  //    Mechanical Sieve stays uncraftable - the builders' lane is manual-only.
  event.remove({ id: /^exdeorum:[a-z0-9_]+_sieve$/ })

  // 3. Strip mesh crafting (id-anchored as above). builder_sieve.js re-adds the
  //    STRING mesh only; the other five stay dead weight and keep their tooltip.
  event.remove({ output: '#exdeorum:sieve_meshes', id: /^exdeorum:/ })

  // 4. Mining shortcuts from tech mods. The Mekanism Digital Miner is an automated ore
  //    miner - a direct bypass of the frog loop - so strip its recipe now that Mekanism
  //    is in the pack. (Inert in the void overworld, but live once the player reaches
  //    the Nether/End, so disable it outright per Pillar 1.)
  event.remove({ output: 'mekanism:digital_miner' })

  // --- Scaffold: uncomment per mod as more automated-mining mods land.
  //     (Kept inert until the mods exist so KubeJS doesn't log unmatched-recipe noise.)
  // event.remove({ type: 'actuallyadditions:mining_lens' })       // Actually Additions
  // event.remove({ type: 'industrialforegoing:laser_drill_ore' }) // Industrial Foregoing
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
    Text.gray('No resource sieving here - the frogs handle resources.'),
    Text.gray('Build a dark-room slime farm instead.')
  ]))

  event.add('exdeorum:string_mesh', [
    Text.green('The Builders\' Sieve'),
    Text.gray('Sift dirt and moss for saplings, bamboo, and garden flora.'),
    Text.gray('Decor only - resources still come from the frogs.')
  ])

  event.add('exdeorum:oak_sieve', [
    Text.green('The Builders\' Sieve'),
    Text.gray('String mesh + dirt or moss = building plants.'),
    Text.gray('Manual only; resource sieving stays disabled.')
  ])

  event.add('exdeorum:mechanical_sieve', [
    Text.red('⚠ Disabled in Sky Frogs'),
    Text.gray('The builders\' sieve lane is manual-only.')
  ])

  event.add('mekanism:digital_miner', [
    Text.red('⚠ Disabled in Sky Frogs'),
    Text.gray('Automated mining bypasses the frogs - not in this pack.')
  ])
})
