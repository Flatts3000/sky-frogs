// Sky Frogs - a second surface for the Flux Dust ritual (#120, maintainer ruling).
//
// Flux Networks hardcodes its anvil check (EventHandler bytecode): thrown
// redstone transmutes only on obsidian that rests on BEDROCK or a FLUX BLOCK -
// no tag, no config. The pack adds a third arrangement: obsidian resting on
// OBSIDIAN. Both blocks are Infernal-frog-farmable, so the ritual works
// anywhere at the tier that owns it - new islands also carry one bedrock at
// their heart (the FN-native arrangement, and the one its JEI page shows).
//
// Implementation: a light poll. Every 10 ticks, redstone item entities resting
// on an obsidian-on-obsidian stack become flux dust 1:1 (stack-preserving),
// mirroring FN's own economics. FN ignores this arrangement entirely, so the
// two handlers can't double-fire on the same entity.
let sfFluxTick = 0

ServerEvents.tick(event => {
  if (!Platform.isLoaded('fluxnetworks')) {
    return
  }
  sfFluxTick++
  if (sfFluxTick % 10 !== 0) {
    return
  }
  event.server.levels.forEach(level => {
    level.entities.forEach(entity => {
      if (entity.type !== 'minecraft:item') {
        return
      }
      const stack = entity.item
      if (!stack || stack.id !== 'minecraft:redstone') {
        return
      }
      const bx = Math.floor(entity.x)
      const by = Math.floor(entity.y)
      const bz = Math.floor(entity.z)
      // a resting item floats just above the surface: floor(y) is the air cell,
      // one below is the block it sits on, two below is the anvil
      if (level.getBlock(bx, by - 1, bz).id !== 'minecraft:obsidian') {
        return
      }
      if (level.getBlock(bx, by - 2, bz).id !== 'minecraft:obsidian') {
        return
      }
      entity.item = Item.of('fluxnetworks:flux_dust', stack.count)
      level.runCommandSilent(`particle minecraft:portal ${entity.x} ${entity.y + 0.3} ${entity.z} 0.2 0.2 0.2 0.5 24`)
      level.runCommandSilent(`playsound minecraft:block.respawn_anchor.charge block @a ${bx} ${by} ${bz} 0.6 1.4`)
    })
  })
})
