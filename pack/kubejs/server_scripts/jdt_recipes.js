// Sky Frogs - Just Dire Things recipe fit-ups for skyblock.
//
// Re-issues JDT's tier-1 Primogel Goo Block recipe so the central "soil" ingredient is
// MYCELIUM instead of plain dirt. Mycelium is a Bog Frogs chain variant (mid-Bog), so
// this gates the JDT entry into the Bog progression naturally - and "fungal substrate"
// reads as a more apt growth medium for the goo than dirt anyway.
//
// JDT's default is the shape `csc / fdf / csc` with c=clay_ball, s=sugar, f=rotten_flesh,
// d=dirt. The override preserves the corners and edges (clay + rotten_flesh + sugar in the
// same positions) and only swaps the centre from dirt to mycelium. JDT's stock dirt recipe
// is left intact for other packs - this is a pack-side override only.
//
// Preserves JDT's `group: "justdirethings"` so the re-issued recipe lands in the same JEI
// recipe group as the rest of JDT's t1 items.
//
// Last verified against Just Dire Things v1.5.7 (data/justdirethings/recipe/gooblock_tier1.json).
// Re-verify the shape and group on every JDT pin bump.
ServerEvents.recipes(event => {
  if (!Platform.isLoaded('justdirethings')) {
    return
  }
  // Remove JDT's default recipe (by id) and re-issue mycelium-centered, same group.
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
  ).group('justdirethings')
})
