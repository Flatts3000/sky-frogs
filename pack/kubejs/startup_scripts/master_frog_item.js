// Sky Frogs - the Master Frog trophy item (Tier 6 / Void endgame capstone).
//
// The campaign's final reward: a creative trophy you craft from the Ultimate Singularity
// (which itself demands one singularity per frog species - the whole pack compressed into
// one item) plus a Froglight of each of the six species. It does nothing but sit on a shelf
// and say you out-frogged the game. master_pond.snbt's capstone hands out the recipe.
//
// Registered here (item registration must run at startup, not in ServerEvents); the
// Ultimate-Crafting-Table recipe lives in server_scripts/void_recipes.js. Texture is a
// placeholder (a PF froglight glyph) copied into assets/kubejs/textures/item/master_frog.png
// at build - final 3D art is a tracked backlog item, not a blocker for the mechanic.
StartupEvents.registry('item', event => {
  event.create('master_frog')
    .displayName('Sky Frogs Master Frog')
    .maxStackSize(1)
    .rarity('epic')
    .glow(true)
    .tooltip('You out-frogged the game.')
})
