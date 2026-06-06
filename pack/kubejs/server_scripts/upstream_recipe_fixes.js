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
})
