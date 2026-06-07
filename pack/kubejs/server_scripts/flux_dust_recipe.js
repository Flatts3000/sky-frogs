// Sky Frogs - the Flux Dust crafting recipe (#120, maintainer design).
//
// Flux Networks' native ritual (toss redstone onto obsidian-on-bedrock, punch
// the obsidian) works on the island's bedrock heart - this recipe is the
// anywhere-else path, shaped like the ritual it mirrors: redstone compressed
// between obsidian. One dust per press, same 1:1 redstone economics as the
// ritual; the obsidian is consumed here but both blocks are Infernal-frog
// change by the tier that wants flux.
ServerEvents.recipes(event => {
  if (!Platform.isLoaded('fluxnetworks')) {
    return
  }
  event.shaped(
    'fluxnetworks:flux_dust',
    [
      'O',
      'R',
      'O'
    ],
    {
      O: 'minecraft:obsidian',
      R: 'minecraft:redstone'
    }
  ).id('kubejs:flux/dust_press')
})
