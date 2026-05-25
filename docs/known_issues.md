# Known Issues

Living tracker of Sky Frogs playtest bugs, limitations, and accepted-for-now quirks. Open *design questions* and deferred features live in [backlog.md](./backlog.md); this doc is for things observed in-game.

## Status legend

| Symbol | Meaning |
|---|---|
| 🔴 | Open. Fix pending. |
| 🟡 | Open. Workaround available. |
| 🔵 | Accepted for now. Low priority; may revisit. |
| 🟢 | Resolved. |

---

## Open

### 🔵 Starter island spawns with a chest
SkyblockBuilder's built-in default island template (`skyblockbuilder-template.nbt`) places a chest on the starter island. Sky Frogs grants the first-launch kit via KubeJS (`kubejs/server_scripts/first_join.js`), not a chest, so the chest is redundant. **Accepted for now** - it's harmless. Removing it requires shipping a custom chestless starter-island template (a [`worldgen.md`](./worldgen.md) deliverable); deferred until we author the island.

> Related and already fixed: the extra hotbar starter items (torch, bucket) were SkyblockBuilder's *default starter inventory* stacking on top of our grant. Emptied via `config/skyblockbuilder/starter_inventory.json5`.
