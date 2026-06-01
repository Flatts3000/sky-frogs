// Sky Frogs - Tier 6 (Void) recipes: the End-portal enabler + the Master Frog trophy.
//
// 1) END PORTAL FRAME. A void skyblock generates no stronghold, so there is no vanilla
//    End portal to find. road_to_void's "Frame the Void" quest asks for 12 frames; this
//    recipe is how you get them. It is NOT gated by a condition - it is gated by its
//    ingredients: glowstone + soul_sand are Infernal-frog resources (nether roster), so
//    the recipe is unreachable until Tier 5 is running, which is exactly the Void gate.
//    Frames carry no eye (you still craft 12 loose eyes of ender to activate the ring).
//    Yields 4 per craft (3 crafts = a full 12-frame ring) to keep the grind sane.
//
// 2) MASTER FROG. The campaign capstone, crafted in the Extended Crafting ULTIMATE table
//    (tier 4) from the Ultimate Singularity - which itself demands one singularity per
//    frog species (config/extendedcrafting/singularities/*.json), so the whole pack is
//    compressed into that one input - ringed by six Froglights (the six species' light)
//    with sweetslime accents. The "one per species" rule is enforced upstream in the
//    Ultimate Singularity, so plain froglight ingredients here are intentional (robust,
//    no per-variant component matcher needed). Output is the KubeJS trophy item
//    (kubejs:master_frog, registered in startup_scripts/master_frog_item.js).
ServerEvents.recipes(event => {
  // End portal frame - skyblock enabler (Infernal-gated by ingredients).
  event.shaped(
    Item.of('minecraft:end_portal_frame', 4),
    [
      'GGG',
      'SOS',
      'SSS'
    ],
    {
      G: 'minecraft:glowstone',
      S: 'minecraft:soul_sand',
      O: 'minecraft:obsidian'
    }
  ).id('kubejs:void/end_portal_frame')

  // Master Frog - Ultimate Crafting Table (tier 4) capstone craft.
  if (Platform.isLoaded('extendedcrafting')) {
    event.custom({
      type: 'extendedcrafting:shaped_table',
      tier: 4,
      pattern: [
        'FFF',
        'FUF',
        'sFs'
      ],
      key: {
        F: { item: 'productivefrogs:configurable_froglight' },
        U: { item: 'extendedcrafting:ultimate_singularity' },
        s: { item: 'productivefrogs:sweetslime' }
      },
      result: { id: 'kubejs:master_frog', count: 1 }
    }).id('kubejs:void/master_frog')
  }
})
