// Sky Frogs - the Mossy Cobblestone gate (reported by Dergib on Discord, #137-adjacent).
//
// Mossy cobblestone is the BOG tier's filler block: every Bog slime-chain step
// (bog_slime_chain.js, and the BOG rows in dissolution_slime_recipes.js) consumes
// 4x mossy cobblestone. The intended way to make it is the Mekanism Metallurgic
// Infuser (cobblestone + Bio), which the "Mossy Cobblestone" quest (70B0000000000011)
// explicitly teaches - a Geode-tier, Mekanism-gated path. That gate is the point:
// mossy cobblestone marks the mineral -> organic crossover into the swamp.
//
// Vanilla and a couple of mods hand out mossy cobblestone (or its moss-block
// ingredient) for free, bypassing that gate:
//   - vanilla crafting: cobblestone + vine, and cobblestone + moss_block
//   - Ex Deorum: 4x grass_seeds -> moss_block (grass seeds are Tier 0 from the
//     builders' sieve, so this mints moss block without the Bog moss frog)
//   - Rechiseled chiseling: cobblestone -> mossy_cobblestone (handled separately by
//     the datapack override at data/rechiseled/chiseling_recipes/cobblestone.json,
//     which strips every mossy entry from the cobblestone group; a self-contained
//     mossy_cobblestone group keeps cosmetic chiseling for players who already hold
//     real mossy cobblestone). BOTH override files set "overwrite": true - with the
//     mod's default "overwrite": false, Rechiseled MERGES same-id recipes and the
//     stripped mossy entry comes right back; overwrite:true makes ours replace it.
//
// Chipped is deliberately left alone: its mason-table recipe takes mossy cobblestone
// to make mossy cobblestone variants (gated behind already having the real block),
// so it is not a bypass.
//
// This script removes the recipe-manager paths. It does NOT touch the Mekanism
// Metallurgic Infuser recipe (output mossy_cobblestone, input cobblestone + Bio) -
// removals are anchored on the bypass INPUTS (vine / moss_block), never a blanket
// output removal, so the intended infusing path survives.

ServerEvents.recipes(event => {
  // Vanilla: cobblestone + vine -> mossy cobblestone, and cobblestone + moss_block
  // -> mossy cobblestone. Anchored on the input so the Metallurgic Infuser recipe
  // (cobblestone + Bio) is left intact.
  event.remove({ output: 'minecraft:mossy_cobblestone', input: 'minecraft:vine' })
  event.remove({ output: 'minecraft:mossy_cobblestone', input: 'minecraft:moss_block' })

  // Ex Deorum: 4x grass_seeds -> moss_block. Moss block is a Bog frog resource (the
  // moss variant); this craft would mint it from Tier 0 sieve seeds. Guarded so it
  // is a no-op if Ex Deorum is ever removed.
  if (Platform.isLoaded('exdeorum')) {
    event.remove({ id: 'exdeorum:moss_block' })
  }
})
