// Sky Frogs - JEI discoverability for the pack's third flux ritual anvil (#120).
//
// Flux Networks' "Creating Flux" JEI category is the mod's own custom plugin
// with two hardcoded entries (obsidian-on-bedrock, obsidian-on-flux-block); a
// script can't add a third entry to it. The pack's obsidian-on-obsidian anvil
// (server_scripts/flux_ritual_obsidian.js) is documented here instead, as an
// information page on flux dust itself - visible wherever the player inspects
// the item in JEI.
RecipeViewerEvents.addInformation('item', event => {
  if (!Platform.isLoaded('fluxnetworks')) {
    return
  }
  event.add('fluxnetworks:flux_dust', [
    Text.of('Sky Frogs extra: the ritual also works with obsidian stacked on obsidian.'),
    Text.of('Toss redstone on top, left-click the obsidian - same as the bedrock version.'),
    Text.of('Your starter island hides one bedrock at its bottom-center, if you prefer the classic.')
  ])
})
