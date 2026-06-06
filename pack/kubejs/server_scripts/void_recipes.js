// Sky Frogs - Tier 6 (Void) recipes: the End Cake (the way in) + the Master Frog trophy.
//
// 1) END CAKE (Ex Deorum). A void skyblock generates no stronghold, so there is no vanilla
//    End portal to find. The gate used to be a hand-built 12-frame portal ring, which proved
//    a trap in practice - frames must face inward, and a wrong-facing ring silently never
//    lights (CF report #8041724) - so the gate is now Ex Deorum's End Cake: place it, take
//    a bite, arrive in the End. One cake has 6 slices = 6 trips. Ex Deorum's default recipe
//    needs crushed end stone, a chicken-and-egg on this skyblock (end stone comes from the
//    Void frog you don't have yet), so we override it with a vanilla-cake-shaped recipe:
//    milk on top (plain milk OR any Slime Milk - the frog-native path), eyes of ender where
//    the sugar goes, wheat base. The eyes (pearl + Infernal blaze powder) keep it Tier 5+
//    gated. The #productivefrogs:slime_milk_buckets tag is built in slime_milk_tags.js.
//    KNOWN ASYMMETRY (intentional): plain milk buckets return their empty bucket, but
//    Slime Milk buckets are consumed whole - milk_bucket_no_remainder.js clears their
//    crafting remainder pack-wide (the slime-chain bucket-dupe fix; selftest asserts it),
//    and vanilla crafting has no per-recipe remainder override. Quest text says so.
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
  // End Cake - the End gate (Infernal-gated by its eyes of ender).
  if (Platform.isLoaded('exdeorum')) {
    event.remove({ id: 'exdeorum:end_cake' })
    event.shaped(
      'exdeorum:end_cake',
      [
        'MMM',
        'PEP',
        'WWW'
      ],
      {
        M: ['minecraft:milk_bucket', '#productivefrogs:slime_milk_buckets'],
        P: 'minecraft:ender_eye',
        E: '#c:eggs',
        W: 'minecraft:wheat'
      }
    ).id('kubejs:void/end_cake')
  }

  // Sculk Shrieker - the missing link in the Warden chain (#82, credit to a Discord
  // member's correction). Ex Deorum's Sculk Core (4 echo shards + ender pearl, all
  // Void frog resources) makes a placed shrieker Warden-summon-capable, but the
  // mod's only shrieker SOURCE is its netherite-mesh sieve drop, which Pillar 1
  // disables. This recipe restores the link from frog-farmed materials: sculk ring,
  // echo-shard prongs, a bone block for the ribs. Three shrieks and the Warden
  // answers - which is what Industrial Foregoing Souls' Soul Laser wants.
  event.shaped(
    'minecraft:sculk_shrieker',
    [
      'SES',
      'EBE',
      'SES'
    ],
    {
      S: 'minecraft:sculk',
      E: 'minecraft:echo_shard',
      B: 'minecraft:bone_block'
    }
  ).id('kubejs:void/sculk_shrieker')

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
