# Sky Frogs

A Minecraft modpack for **NeoForge 1.21.1** where **frogs replace mining** as the primary source of all materials. Skyblock progression, ~22 questbook chapters, 100+ mods.

## Concept

Sky Frogs is the [Productive Frogs](../productive-frogs) analog of [Sky Bees Reborn](https://www.curseforge.com/minecraft/modpacks/sky-bees-reborn) — a void skyblock where the only viable path to iron, gold, diamonds, and beyond is through breeding, hatching, and farming **resource frogs**. Sieving exists as a manual bootstrap; automated mining is disabled.

**Core loop:**

```
Find frogspawn → bottle it → prime the egg with a category material →
hatch into a Resource Frog → feed it a matching Resource Slime →
collect Configurable Froglight → smelt or crush for ingots
```

The six frog categories (Metallic, Mineral, Gem, Aquatic, Infernal, Arcane) define the tier progression. Slime species supply variety inside each tier.

## Status

**Planning phase.** Repo skeleton + design docs only — no pack contents yet. See [docs/](./docs/) for the full design spec.

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
