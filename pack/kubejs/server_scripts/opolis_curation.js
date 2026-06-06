// Sky Frogs - Opolis Utilities (BBL Utility) curation (#85).
//
// The mod ships as a grab-bag; six maintainer rulings (recorded on #85) define
// exactly which pieces survive in this pack:
//
//   KEEP as shipped: Cloche, Drying/Soaking Tables, Item Repairer, Home/Death
//     Stones, Crook, Wooden Shears, Redstone Clock, Block Breaker/Placer,
//     Crafters, Clicker (ruling 6: automating PF appliances is acceptable),
//     Ender Ore (ruling 6: as shipped), animal summons EXCEPT the two below.
//   CURATE: Resource Generator (ruling 5) - defaults stripped, re-added as a
//     builders' STONE lane: only stone variants NO FROG PRODUCES. Re-screen
//     this list whenever PF adds variants (if PF ever frogs basalt, basalt
//     leaves this list).
//   STRIP: Fluid Generator entirely (ruling 4: fluid generation is a planned
//     FROG capability); Catalogue + B Bucks + Loot Boxes (ruling 3: no shop
//     currency economy); glow_squid + squid summons (ruling 1: their drops
//     are Cave/Tide frog resources and singularity inputs).
//
// Every removal is id-anchored to ^opolisutilities: per the anti.js rule, so
// the curated kubejs:* re-adds below are untouchable by these filters.

ServerEvents.recipes(event => {
  if (!Platform.isLoaded('opolisutilities')) {
    return
  }
  const OPOLIS_DEFAULTS = /^opolisutilities:/

  // Ruling 3: the Catalogue/B-Bucks economy. Strip the shop's entries (recipe
  // type) AND the crafting recipes for the shop block + book; B Bucks and the
  // Loot Boxes have no crafting recipes of their own - they only flow FROM the
  // catalogue, so this severs the whole economy.
  event.remove({ type: 'opolisutilities:catalogue', id: OPOLIS_DEFAULTS })
  event.remove({ output: 'opolisutilities:catalogue', id: OPOLIS_DEFAULTS })
  event.remove({ output: 'opolisutilities:catalogue_book', id: OPOLIS_DEFAULTS })

  // Ruling 4: no fluid generation outside the (planned) frog loop. Block
  // crafting + both fluid recipes go.
  event.remove({ type: 'opolisutilities:fluid_generator', id: OPOLIS_DEFAULTS })
  event.remove({ output: 'opolisutilities:fluid_generator', id: OPOLIS_DEFAULTS })

  // Ruling 1: summons whose drops are frog resources (glow ink = Cave,
  // ink sac = Tide; both singularity inputs). The other animal summons stay.
  event.remove({ id: 'opolisutilities:summoning_block/glow_squid' })
  event.remove({ id: 'opolisutilities:summoning_block/squid' })

  // Ruling 5: Resource Generator becomes the builders' STONE lane. Strip the
  // mod's defaults (cobblestone tag + stones tag)...
  event.remove({ type: 'opolisutilities:resource_generator', id: OPOLIS_DEFAULTS })

  // ...and re-add exactly the stone variants no frog produces. Excluded on
  // purpose: tuff + calcite (Geode frog), end stone (Void), netherrack /
  // obsidian / soul sand / soul soil (Infernal), prismarine (Tide), sculk
  // (Void), and the Bog ground blocks (dirt / mud / clay / moss / mycelium).
  const STONE_LANE = [
    'minecraft:stone',
    'minecraft:cobblestone',
    'minecraft:granite',
    'minecraft:diorite',
    'minecraft:andesite',
    'minecraft:deepslate',
    'minecraft:cobbled_deepslate',
    'minecraft:blackstone',
    'minecraft:basalt',
    'minecraft:smooth_basalt',
    'minecraft:dripstone_block',
    'minecraft:sandstone',
    'minecraft:red_sandstone'
  ]
  STONE_LANE.forEach(stone => {
    event.custom({
      type: 'opolisutilities:resource_generator',
      input: { item: stone }
    }).id(`kubejs:opolis_stone_lane/${stone.split(':')[1]}`)
  })
})

// Flag the severed economy in tooltips so the omission reads as intentional.
// Guarded like the recipes event: tooltip registration resolves item ids
// EAGERLY, so an absent mod throws "Item with ID ... does not exist" on
// /reload (seen live when the junctioned script ran before the jar synced).
ItemEvents.modifyTooltips(event => {
  if (!Platform.isLoaded('opolisutilities')) {
    return
  }
  // 4.11.10's jar is full of STALE assets - models and lang keys for items the
  // mod no longer registers (wallet, advanced_loot_box, ...), so a hardcoded
  // id list keeps erroring as the roster drifts. CRITICAL API NOTE: Item.of()
  // on an unknown id does not throw a catchable exception - KubeJS's parser
  // LOGS the error to the console screen itself, so try/catch around it still
  // leaves a red error on /reload (proven in playtest rounds 3-5). The only
  // silent probe is Item.exists(), a direct registry lookup with no stack
  // parsing (method verified present in kubejs-2101.7.2 ItemWrapper).
  const itemExists = id => {
    try {
      return Item.exists(id)
    } catch (e) {
      return false
    }
  }
  const severed = [
    'opolisutilities:catalogue',
    'opolisutilities:catalogue_book',
    'opolisutilities:b_bucks',
    'opolisutilities:basic_loot_box',
    'opolisutilities:advanced_loot_box',
    'opolisutilities:elite_loot_box',
    'opolisutilities:wallet'
  ]
  severed.filter(itemExists).forEach(id => {
    event.add(id, [
      Text.red('⚠ Disabled in Sky Frogs'),
      Text.gray('No shop economy here - quests and frogs provide.')
    ])
  })

  if (itemExists('opolisutilities:fluid_generator')) {
    event.add('opolisutilities:fluid_generator', [
      Text.red('⚠ Disabled in Sky Frogs'),
      Text.gray('Fluids are frog business (coming to Productive Frogs).')
    ])
  }

  if (itemExists('opolisutilities:resource_generator')) {
    event.add('opolisutilities:resource_generator', [
      Text.green('The Builders\' Stone Lane'),
      Text.gray('Generates the stone variants no frog produces.'),
      Text.gray('Granite to red sandstone - decor supply, not an economy.')
    ])
  }
})
