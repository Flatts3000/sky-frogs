// Sky Frogs - a third anvil for the Flux Dust ritual (#120, maintainer ruling).
//
// Flux Networks hardcodes its anvil check (EventHandler bytecode): LEFT-CLICK
// obsidian resting on BEDROCK or a FLUX BLOCK and the redstone items sitting on
// top compress into flux dust - no tag, no config, and its JEI category shows
// exactly those two arrangements. The pack adds a third: obsidian resting on
// OBSIDIAN (both Infernal-frog-farmable), trigger-compatible with the mod's own
// flow ("Left click the Obsidian"). New islands also carry one bedrock at their
// heart for the FN-native arrangement.
//
// Click-triggered like FN's - no tick polling. FN ignores obsidian-on-obsidian,
// so the two handlers can't double-fire. JEI can't be taught FN's custom
// category from a script, so discoverability lives in an information page on
// flux dust (client_scripts/flux_jei_info.js) and the Powered Up quest.
BlockEvents.leftClicked(event => {
  if (!Platform.isLoaded('fluxnetworks')) {
    return
  }
  const { block, level } = event
  if (String(block.id) !== 'minecraft:obsidian') {
    return
  }
  if (String(level.getBlock(block.x, block.y - 1, block.z).id) !== 'minecraft:obsidian') {
    return
  }
  let converted = 0
  level.entities.forEach(entity => {
    if (entity.type !== 'minecraft:item') {
      return
    }
    const stack = entity.item
    if (!stack || stack.id !== 'minecraft:redstone') {
      return
    }
    // only the items sitting in the column directly above the clicked obsidian
    if (Math.floor(entity.x) !== block.x || Math.floor(entity.z) !== block.z) {
      return
    }
    if (Math.floor(entity.y) !== block.y + 1) {
      return
    }
    entity.item = Item.of('fluxnetworks:flux_dust', stack.count)
    converted += stack.count
  })
  if (converted > 0) {
    level.runCommandSilent(`particle minecraft:portal ${block.x + 0.5} ${block.y + 1.3} ${block.z + 0.5} 0.2 0.2 0.2 0.5 24`)
    level.runCommandSilent(`playsound minecraft:block.respawn_anchor.charge block @a ${block.x} ${block.y} ${block.z} 0.6 1.4`)
  }
})
