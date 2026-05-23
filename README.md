# Sky Frogs

A Minecraft modpack for **NeoForge 1.21.11** built around [Productive Frogs](../productive-frogs). Early planning — pack scaffold landed; content TBD.

## Concept

Sky Frogs is a skyblock modpack with **resource frogs** at the center: breed them, hatch them, feed them matching slimes, collect what they produce. The pack is finding its own identity — early thinking leans on a void skyblock with mining shortcuts disabled, but that's a starting point, not a thesis.

[Sky Bees Reborn](https://www.curseforge.com/minecraft/modpacks/sky-bees-reborn) is a reference for the genre and ships in this directory tree as a study object. Sky Frogs is **not** a port of it.

**Core loop:**

```
Find frogspawn → bottle it → prime the egg with a category material →
hatch into a Resource Frog → feed it a matching Resource Slime →
collect Configurable Froglight → smelt or crush for ingots
```

The six frog categories (Metallic, Mineral, Gem, Aquatic, Infernal, Arcane) define the tier progression. Slime species supply variety inside each tier.

## Status

**Early planning phase.** Repo skeleton + exploratory design docs only — no pack contents yet, and **no design choices are canonical yet**. Every doc in [docs/](./docs/) is marked DRAFT. The pack is looking for its own voice; treat everything written as a starting point to argue with.

## Quick navigation

- [docs/design_overview.md](./docs/design_overview.md) — concept and core loop
- [docs/progression.md](./docs/progression.md) — tier-by-tier player journey
- [docs/mod_list.md](./docs/mod_list.md) — what mods we ship and why
- [docs/quest_book.md](./docs/quest_book.md) — chapter outline
- [docs/kubejs_overrides.md](./docs/kubejs_overrides.md) — what we disable and force
- [docs/repo_layout.md](./docs/repo_layout.md) — how the pack is built
- [docs/distribution.md](./docs/distribution.md) — how it ships
- [docs/backlog.md](./docs/backlog.md) — open questions

## Building

TBD — see [docs/repo_layout.md](./docs/repo_layout.md). Target tool: `packwiz` producing both `.mrpack` (Modrinth) and CurseForge zip outputs.

## License

MIT for the pack-authored content (KubeJS, configs, datapacks, branding, docs). Each bundled mod retains its own license. See [LICENSE](./LICENSE).
