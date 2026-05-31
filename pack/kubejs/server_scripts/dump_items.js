// Sky Frogs - build helper: /sf_dump_items (op level 2).
//
// KubeJS 2101.x dropped the old `/kubejs export` item-list dump (its `export`
// subcommands are only debug / pack-folders / pack-zips / recipe-schema-json), so this
// regenerates the item-id allowlist that the static validator's Q-ITEM-EXISTS check
// consumes (tools/data/item_ids.txt). Item.getTypeList() returns every registered item id.
//
// Usage: after a /reload, run /sf_dump_items. The ids are written to logs/kubejs/server.log
// in SF_ITEM_DUMP:: chunks; the repo picks them out and writes tools/data/item_ids.txt.
// Re-run whenever the mod list changes. Chunked (200/line) so no single log line is huge.

ServerEvents.commandRegistry(event => {
  const { commands: Commands } = event
  event.register(
    Commands.literal('sf_dump_items')
      .requires(src => src.hasPermission(2))
      .executes(ctx => {
        const ids = []
        Item.getTypeList().forEach(s => ids.push(String(s)))
        ids.sort()
        console.info('SF_ITEM_DUMP_BEGIN ' + ids.length)
        for (let i = 0; i < ids.length; i += 200) {
          console.info('SF_ITEM_DUMP::' + ids.slice(i, i + 200).join(','))
        }
        console.info('SF_ITEM_DUMP_END ' + ids.length)
        ctx.source.sendSystemMessage(Text.green('Sky Frogs: dumped ' + ids.length +
          ' item ids to logs/kubejs/server.log (search SF_ITEM_DUMP).'))
        return 1
      })
  )
})
