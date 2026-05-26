// Sky Frogs - Pillar 1: disable mining/sieving shortcuts.
//
// Sky Frogs' identity is "frogs are the resource path." Anything that lets a player
// generate resources by another route gets removed. Tier 0 is a dark-room slime farm,
// NOT sieving, so Ex Deorum's sieve mechanic is disabled wholesale here. Ex Deorum
// stays in the pack for crucibles + barrels (the second-water-source mechanic) and the
// porcelain bucket - we only kill sieving.
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
  // 1. Kill the sieving MECHANIC. Removing these two recipe types disables every
  //    sieve variant at once - manual, compressed, and the Mechanical Sieve all
  //    consume the same `sieve` / `compressed_sieve` recipe types.
  event.remove({ type: 'exdeorum:sieve' })
  event.remove({ type: 'exdeorum:compressed_sieve' })

  // 2. Strip the sieve BLOCK crafting recipes so players can't craft an inert sieve.
  //    Ex Deorum generates one per wood material (oak_sieve, acacia_compressed_sieve,
  //    mechanical_sieve, ...); the regex catches all of them, including modded woods
  //    and any added via config, without enumerating. Process recipe ids contain
  //    slashes and don't match. Digits are allowed in the wood segment because some
  //    modded wood registry names contain them.
  event.remove({ id: /^exdeorum:[a-z0-9_]+_sieve$/ })

  // 3. Strip mesh crafting. Meshes only feed sieves, so they're dead weight now.
  //    The `#exdeorum:sieve_meshes` tag covers all six (string/flint/iron/golden/
  //    diamond/netherite) and auto-extends if the mod adds more.
  event.remove({ output: '#exdeorum:sieve_meshes' })

  // --- Scaffold: uncomment per mod as automated-mining mods are added to the pack.
  //     (Kept inert until the mods exist so KubeJS doesn't log unmatched-recipe noise.)
  // event.remove({ type: 'actuallyadditions:mining_lens' })       // Actually Additions
  // event.remove({ type: 'industrialforegoing:laser_drill_ore' }) // Industrial Foregoing
  // event.remove({ output: 'mekanism:digital_miner' })            // Mekanism
})

// Flag the meshes in JEI/tooltips so the omission reads as intentional, not a bug.
// Per-ID (not tag) because that's the verified-working modifyTooltips signature.
ItemEvents.modifyTooltips(event => {
  const meshes = [
    'exdeorum:string_mesh',
    'exdeorum:flint_mesh',
    'exdeorum:iron_mesh',
    'exdeorum:golden_mesh',
    'exdeorum:diamond_mesh',
    'exdeorum:netherite_mesh'
  ]
  meshes.forEach(id => event.add(id, [
    Text.red('⚠ Disabled in Sky Frogs'),
    Text.gray('No sieving here - the frogs handle resources.'),
    Text.gray('Build a dark-room slime farm instead.')
  ]))
})
