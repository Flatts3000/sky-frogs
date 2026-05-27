// Sky Frogs - logs-direct convenience recipes.
//
// Early-game QoL: craft sticks (and a few staples) straight from logs, skipping the
// plank step, which feels clunky on a tree-farm skyblock. Keyed off the #minecraft:logs
// item tag so it works for every wood, vanilla or modded. Ratios are break-even with
// going through planks (no free material) - just fewer crafting steps.
//
// 1 log = 4 planks (vanilla). So: 2 logs = 8 planks = 16 sticks; 8 logs = 32 planks = 4 chests.

ServerEvents.recipes(event => {
  // 2 logs -> 16 sticks (shapeless; vanilla 1-log->planks still works, it needs exactly one log)
  event.shapeless('16x minecraft:stick', ['#minecraft:logs', '#minecraft:logs'])

  // 8 logs in the chest ring -> 4 chests
  event.shaped('4x minecraft:chest', ['LLL', 'L L', 'LLL'], { L: '#minecraft:logs' })
})
