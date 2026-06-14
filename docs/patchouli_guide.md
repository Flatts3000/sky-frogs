# Patchouli guide: extending Productive Frogs' book

Productive Frogs (v1.21+) ships its own in-game Patchouli field guide, book id
**`productivefrogs:guide`** (granted on join by `pack/kubejs/server_scripts/first_join.js`,
also craftable as a vanilla book + slime ball). The pack does **not** ship its own book - it
**extends PF's** with a pack-specific category, so there is one guide, not two.

## How the extension works

PF's `book.json` sets `use_resource_pack: true` and `i18n: false`. As of Patchouli 1.20+,
"extension books" are obsolete: a pack adds content by dropping files into the **original
book's namespace** via the resource-pack system. KubeJS serves `pack/kubejs/assets/` as a
resource pack, so the pack's entries live at:

```
pack/kubejs/assets/productivefrogs/patchouli_books/guide/en_us/categories/sky_frogs.json
pack/kubejs/assets/productivefrogs/patchouli_books/guide/en_us/entries/sky_frogs/*.json
```

They merge into `productivefrogs:guide` at load. Because the book is `i18n: false`, text is
written **inline** in each JSON (literal strings, not lang keys) and lives under `en_us/` -
mirror PF's own entry format (see the jar's `assets/productivefrogs/patchouli_books/guide/`).

The pack content is the **`productivefrogs:sky_frogs`** category (`sortnum 1000`, so it sorts
after PF's own categories which top out at 500), with entries referencing
`"category": "productivefrogs:sky_frogs"`.

## Limitations (Patchouli 1.20+ resource-pack extension)

- You can add **new categories and new entries** only. You **cannot add pages to an existing
  PF entry** - if PF later wants a page added, that is an upstream change, not a pack one.
- Keep entries to **new** files. If PF renames a category id, our `category` references must
  follow.
- Keep it a focused supplement: the **quest book owns linear progression**; the guide is
  reference. Do not re-document quest steps here (two sources of truth drift - the lesson from
  the issue #169 editorial pass). Cover what quests do poorly and what stock PF cannot know:
  the void-skyblock framing, the Dissolution Chamber slime engine, pack recipe swaps, the
  singularity endgame.

## Dev caveat: assets are NOT junctioned

The dev instance junctions `kubejs/server_scripts`, `kubejs/data`, and
`config/ftbquests/quests` - but **NOT** `kubejs/assets`. So unlike the live quest-edit loop
(edit + `/reload` or rejoin), **Patchouli book edits do not appear in the dev instance by
editing the repo alone.** To test book changes in-game, sync the asset into the instance
(copy `pack/kubejs/assets/...` into `<instance>/kubejs/assets/...`, or run a pack export). The
JSON is plain data, so a JSON-lint (`python -c "import json; json.load(open(f))"`) catches
syntax errors without launching the game.

There is no automated validator for the book (the `validate_quests.py` gate is FTB Quests
only). Ground-truth every mechanic claim against the mod (recipes/overrides), ASCII only.
