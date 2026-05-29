// Sky Frogs - Just Dire Things recipe fit-ups for skyblock.
//
// Re-issues JDT's tier-1 Primogel Goo Block recipe so the central "soil" ingredient is
// MYCELIUM instead of plain dirt. Mycelium is a Bog Frogs chain variant (mid-Bog), so
// this gates the JDT entry into the Bog progression naturally - and "fungal substrate"
// reads as a more apt growth medium for the goo than dirt anyway.
//
// Same shape (csc / fmf / csc) and same other ingredients (clay balls + rotten flesh +
// sugar) as JDT's default; only the centre changes. JDT's stock dirt recipe is left
// intact for other packs - this is a pack-side override only.
ServerEvents.recipes(event => {
  if (!Platform.isLoaded('justdirethings')) {
    return
  }
  // Remove JDT's default recipe (by id) and re-issue mycelium-centered.
  event.remove({ id: 'justdirethings:gooblock_tier1' })
  event.shaped(
    'justdirethings:gooblock_tier1',
    [
      'CSC',
      'FMF',
      'CSC'
    ],
    {
      C: 'minecraft:clay_ball',
      S: 'minecraft:sugar',
      F: 'minecraft:rotten_flesh',
      M: 'minecraft:mycelium'
    }
  )
})
