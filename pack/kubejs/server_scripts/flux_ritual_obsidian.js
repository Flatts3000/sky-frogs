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
// FN ignores obsidian-on-obsidian, so the two handlers can't double-fire. JEI
// can't be taught FN's custom category from a script, so discoverability lives
// in an information page on flux dust (client_scripts/flux_jei_info.js) and the
// Powered Up quest.
//
// API NOTE (first version failed live): the leftClicked EVENT exposes block /
// entity / item / facing - there is NO event.level (BlockLeftClickedKubeEvent
// bytecode). The level hangs off the BLOCK (LevelBlock.getLevel), neighbors are
// block.down/up, and the entity scan is the EntityGetterKJS duck
// getEntitiesWithin(AABB) - all verified in kubejs-2101.7.2 before this rewrite.
BlockEvents.leftClicked(event => {
  if (!Platform.isLoaded('fluxnetworks')) {
    return
  }
  const block = event.block
  if (String(block.id) !== 'minecraft:obsidian') {
    return
  }
  if (String(block.down.id) !== 'minecraft:obsidian') {
    return
  }
  // the column directly above the clicked obsidian, with a little slack for
  // items resting on the very edge
  const items = block.level.getEntitiesWithin([
    block.x - 0.1, block.y + 0.9, block.z - 0.1,
    block.x + 1.1, block.y + 2.0, block.z + 1.1
  ])
  let converted = 0
  items.forEach(entity => {
    if (entity.type !== 'minecraft:item') {
      return
    }
    const stack = entity.item
    if (!stack || String(stack.id) !== 'minecraft:redstone') {
      return
    }
    entity.item = Item.of('fluxnetworks:flux_dust', stack.count)
    converted += stack.count
  })
  if (converted > 0) {
    // effects are best-effort: never let feedback kill the conversion
    try {
      event.entity.runCommandSilent(`particle minecraft:portal ${block.x + 0.5} ${block.y + 1.3} ${block.z + 0.5} 0.2 0.2 0.2 0.5 24`)
      event.entity.runCommandSilent(`playsound minecraft:block.respawn_anchor.charge block @a ${block.x} ${block.y} ${block.z} 0.6 1.4`)
    } catch (e) {
    }
  }
})
