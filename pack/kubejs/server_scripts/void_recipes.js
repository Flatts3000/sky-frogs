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
// 2) MASTER FROG. The campaign capstone, crafted in a regular crafting table from the
//    Ultimate Singularity - which itself demands one singularity for every vanilla froglight
//    resource (all 40; config/extendedcrafting/singularities/*.json), so
//    the whole pack is compressed into that one input - ringed by six Froglights (the species'
//    light) with sweetslime accents. The "every resource" rule is enforced upstream in the
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

  // Master Frog - regular crafting table capstone craft. The Ultimate Singularity is already
  // the gated endgame item, so the final trophy just needs a vanilla 3x3 grid (no EC table).
  // Guarded on EC only because the Ultimate Singularity (the U key) is an Extended Crafting item.
  if (Platform.isLoaded('extendedcrafting')) {
    event.shaped(
      'kubejs:master_frog',
      [
        'FFF',
        'FUF',
        'sFs'
      ],
      {
        F: 'productivefrogs:configurable_froglight',
        U: 'extendedcrafting:ultimate_singularity',
        s: 'productivefrogs:sweetslime'
      }
    ).id('kubejs:void/master_frog')
  }
})
