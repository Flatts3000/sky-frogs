// Sky Frogs - quartz-free storage networking.
//
// Sky Frogs gates nether quartz behind the Infernal tier, but the worst storage
// tedium hits early. So the Sophisticated + Functional Storage controllers are
// re-issued WITHOUT quartz, making the analog (no-power) storage network a
// Cave-era stopgap. Refined Storage at Infernal stays the real upgrade
// (autocrafting, wireless terminals, disk-scale storage) over this hand-built net.
//
// Quartz hides in two forms in the stock recipes:
//   - direct: minecraft:quartz_block  -> minecraft:redstone_block (9 redstone, a Cave resource)
//   - hidden: minecraft:comparator    -> minecraft:repeater       (its quartz-free redstone-logic twin)
//             (a comparator needs 1 nether quartz to craft)
//
// Ender-pearl parts (Storage Link, Storage Tool, ender drawer) are left intact -
// pearls are farmable from the Tier 0 dark room.

ServerEvents.recipes(event => {
  // Sophisticated Storage - Storage Controller (comparator -> repeater).
  event.remove({ id: 'sophisticatedstorage:controller' })
  event.custom({
    type: 'minecraft:crafting_shaped',
    category: 'misc',
    pattern: ['SCS', 'PBP', 'SCS'],
    key: {
      B: { type: 'sophisticatedstorage:base_tier_wooden_storage' },
      C: { item: 'minecraft:repeater' },
      P: { tag: 'minecraft:planks' },
      S: { tag: 'c:stones' }
    },
    result: { count: 1, id: 'sophisticatedstorage:controller' }
  })

  // Functional Storage - controllers + extensions.
  // quartz_block -> redstone_block; comparator -> repeater. The drawer slot keeps
  // its component-stripping ingredient type so any drawer (with upgrades) still works.
  const drawer = { type: 'functionalstorage:tag_without_component', tag: 'functionalstorage:drawer' }

  event.remove({ id: 'functionalstorage:storage_controller' })
  event.custom({
    type: 'minecraft:crafting_shaped',
    category: 'misc',
    pattern: ['IBI', 'CDC', 'IBI'],
    key: {
      B: { item: 'minecraft:redstone_block' },
      C: drawer,
      D: { item: 'minecraft:repeater' },
      I: { tag: 'c:stones' }
    },
    result: { count: 1, id: 'functionalstorage:storage_controller' }
  })

  event.remove({ id: 'functionalstorage:controller_extension' })
  event.custom({
    type: 'minecraft:crafting_shaped',
    category: 'misc',
    pattern: ['IBI', 'CDC', 'IBI'],
    key: {
      B: { item: 'minecraft:redstone_block' },
      C: drawer,
      D: { item: 'minecraft:repeater' },
      I: { tag: 'c:stones' }
    },
    result: { count: 1, id: 'functionalstorage:controller_extension' }
  })

  event.remove({ id: 'functionalstorage:framed_storage_controller' })
  event.custom({
    type: 'minecraft:crafting_shaped',
    category: 'misc',
    pattern: ['IBI', 'CDC', 'IBI'],
    key: {
      B: { item: 'minecraft:redstone_block' },
      C: drawer,
      D: { item: 'minecraft:repeater' },
      I: { tag: 'c:nuggets/iron' }
    },
    result: { count: 1, id: 'functionalstorage:framed_storage_controller' }
  })

  event.remove({ id: 'functionalstorage:framed_controller_extension' })
  event.custom({
    type: 'minecraft:crafting_shaped',
    category: 'misc',
    pattern: ['IBI', 'CDC', 'IBI'],
    key: {
      B: { item: 'minecraft:redstone_block' },
      C: drawer,
      D: { item: 'minecraft:repeater' },
      I: { tag: 'c:nuggets/iron' }
    },
    result: { count: 1, id: 'functionalstorage:framed_controller_extension' }
  })
})
