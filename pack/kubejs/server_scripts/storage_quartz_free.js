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

  // Functional Storage - controllers + extensions, plain and framed. All share the
  // IBI/CDC/IBI shape. Stock keeps each pair distinct two ways: the CORNER (stones for
  // the plain blocks, iron nuggets for the framed pair) AND the CENTER (comparator for
  // the controllers, repeater for the extensions). quartz_block -> redstone_block in the
  // B slot. The comparator needs nether quartz, so the quartz-free controller takes a
  // redstone_block center instead - denser than the extension's repeater, preserving the
  // stock "controller is the costlier craft" hierarchy. The repeater is already quartz-
  // free, so the extensions keep it. Keeping the center distinct per role is load-bearing:
  // collapsing both onto repeater made controller + extension byte-for-byte identical
  // recipes with two different outputs, an ambiguous-craft bug (#186). The drawer slot
  // keeps its component-stripping type so any drawer (with upgrades) still works.
  const drawer = { type: 'functionalstorage:tag_without_component', tag: 'functionalstorage:drawer' }
  const functionalControllers = [
    { id: 'functionalstorage:storage_controller', corner: 'c:stones', center: 'minecraft:redstone_block' },
    { id: 'functionalstorage:controller_extension', corner: 'c:stones', center: 'minecraft:repeater' },
    { id: 'functionalstorage:framed_storage_controller', corner: 'c:nuggets/iron', center: 'minecraft:redstone_block' },
    { id: 'functionalstorage:framed_controller_extension', corner: 'c:nuggets/iron', center: 'minecraft:repeater' }
  ]
  functionalControllers.forEach(recipe => {
    event.remove({ id: recipe.id })
    event.custom({
      type: 'minecraft:crafting_shaped',
      category: 'misc',
      pattern: ['IBI', 'CDC', 'IBI'],
      key: {
        B: { item: 'minecraft:redstone_block' },
        C: drawer,
        D: { item: recipe.center },
        I: { tag: recipe.corner }
      },
      result: { count: 1, id: recipe.id }
    })
  })
})
