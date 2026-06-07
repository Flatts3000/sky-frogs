// Sky Frogs - removals of BROKEN upstream recipes (not design disables; those
// live in anti.js / the curation scripts).
//
// Iron Furnaces ships furnace-upgrade recipes for All The Mods metals
// (unobtainium, vibranium) whose optional ingredients resolve empty without
// the ATM mods - they fail KubeJS's recipe parse with "pattern
// <optional_ingredient> is not allowed to be empty" on every reload, and the
// upgrades are uncraftable here regardless (the metals don't exist in this
// pack). Removing them cleans JEI; the parse warning itself may still print
// once (KubeJS parses before filtering) - that part is cosmetic and upstream.
ServerEvents.recipes(event => {
  if (!Platform.isLoaded('ironfurnaces')) {
    return
  }
  event.remove({ id: 'ironfurnaces:upgrades/upgrade_unobtainium' })
  event.remove({ id: 'ironfurnaces:upgrades/upgrade_vibranium' })

  // The three ATM FURNACE recipes are a different upstream slip (#116, reported
  // by Dergib): unlike the upgrades/* recipes (mod_loaded-gated on allthemodium,
  // correctly dead here), furnaces/*_furnace.json ship UNCONDITIONED, so they
  // load with empty c:ingots/<atm-metal> tags - uncraftable ghosts that still
  // render in JEI (e.g. under "uses" for the netherite furnace). ATO ships no
  // ATM metals; nothing in this pack can ever satisfy them.
  event.remove({ id: 'ironfurnaces:furnaces/allthemodium_furnace' })
  event.remove({ id: 'ironfurnaces:furnaces/vibranium_furnace' })
  event.remove({ id: 'ironfurnaces:furnaces/unobtainium_furnace' })
  // ...and the conditioned-but-pointless upgrade for symmetry with the two above
  // (if a future Iron Furnaces build drops the condition, it dies here anyway).
  event.remove({ id: 'ironfurnaces:upgrades/upgrade_allthemodium' })
})
