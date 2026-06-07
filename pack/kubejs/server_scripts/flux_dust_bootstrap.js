// Sky Frogs - the Flux Dust bootstrap recipe (#120, reported by Dergib on Discord).
//
// Flux Networks' native dust ritual (enableFluxRecipe) compresses thrown redstone
// against OBSIDIAN SITTING ON BEDROCK - and a void skyblock generates no bedrock,
// so the first dust is unobtainable (a flux block works as the anvil too, but you
// need dust to make one: chicken and egg). Same missing-link class as the End Cake
// and the sculk shrieker; same fix: a KubeJS recipe.
//
// Economics mirror the ritual: 1 redstone -> 1 dust, with the obsidian consumed
// here (the ritual keeps its anvil, but obsidian is Infernal-frog-farmable, so
// four-for-one is a rounding error). Once you own a flux block, the mod's real
// ritual works on it and this recipe is just the JEI-discoverable on-ramp.
ServerEvents.recipes(event => {
  if (!Platform.isLoaded('fluxnetworks')) {
    return
  }
  event.shapeless(
    Item.of('fluxnetworks:flux_dust', 4),
    [
      'minecraft:obsidian',
      'minecraft:redstone',
      'minecraft:redstone',
      'minecraft:redstone',
      'minecraft:redstone'
    ]
  ).id('kubejs:flux/dust_bootstrap')
})
