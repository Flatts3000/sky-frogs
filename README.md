# Sky Frogs

A void-skyblock modpack for **NeoForge 1.21.1** built around [Productive Frogs](https://github.com/Flatts3000/productive-frogs).

You spawn on a 3×3 dirt island. There's no overworld to mine. The only way past iron is through **Resource Frogs**: six categories of breedable frogs that each eat category-matching slimes and produce Configurable Froglights you smelt into ingots.

## Concept

```
Find frogspawn → bottle it → prime the egg with a category material →
hatch into a Resource Frog → feed it a matching Resource Slime →
collect Configurable Froglight → smelt or crush for ingots
```

Six frog categories define the tier progression:

| Tier | Category   | Unlocks                                                        |
|------|------------|----------------------------------------------------------------|
| 1    | Bog        | Iron, copper, gold, plus modded metals (osmium, tin, aluminum…) |
| 2    | Cave       | Redstone, lapis, coal, quartz, amethyst, certus, fluix          |
| 3    | Geode      | Diamond, emerald, fluorite, peridot, ruby, sapphire             |
| 4    | Tide       | Prismarine, kelp, nautilus, pink slime, latex                   |
| 5    | Infernal   | Blaze rods, quartz, magma, glowstone, netherite line            |
| 6    | Void       | Ender pearls, chorus, draconic, dimensional shards, end-tier    |

Slime species supply the variety inside each tier — adding a new modded resource is a single `slime_variant/*.json` drop, never a Java change.

## Design pillars

- **Vanilla-feeling mechanics.** Productive Frogs leans on vanilla idioms — frogspawn, slimeballs, water bottles, lead-based mob transport. Every interaction is right-click on a block; no custom UIs.
- **Category-based progression.** Six clear tiers (Bog / Cave / Geode / Tide / Infernal / Void) anchor the questbook in a structure that stays legible as more frog and slime variants ship.
- **Cross-mod compat is the design center.** Drop a JSON, get a frog-eats-that-thing variant. Community PRs adding new modded resources need zero Java work.
- **Mining shortcuts disabled by design.** Laser drills, mining lenses, digital miners, and quarry cards are recipe-stripped or hidden from JEI. The frog tree is the path; the pack enforces it.

## Status

**Early development.** The repo scaffold, packwiz tree, FTB utility stack, JEI, Jade, KubeJS, and Productive Frogs v1.0.1 (from CurseForge) are in place. The first Tier 0 KubeJS scripts have landed (first-join grant, sieving disable). Remaining content (FTB Quests chapters, slime variant JSONs, the rest of the KubeJS overrides) is in progress.

Every doc in [`docs/`](./docs/) is marked DRAFT and explicitly non-canonical. The pack is still finding its identity; design decisions are up for revision.

## Quick navigation

For players:
- [Concept and core loop](./docs/design_overview.md)
- [Tier-by-tier journey](./docs/progression.md)
- [Mod list and selection criteria](./docs/mod_list.md)
- [The CurseForge listing copy](./docs/curseforge_page.md)

For contributors:
- [Repo layout and packwiz workflow](./docs/repo_layout.md)
- [KubeJS overrides (the four pillars)](./docs/kubejs_overrides.md)
- [FTB Quests chapter outline](./docs/quest_book.md)
- [Distribution + release workflow](./docs/distribution.md)
- [Open questions and known risks](./docs/backlog.md)
- [How to contribute](./CONTRIBUTING.md)

## Building locally

`pack/` is initialized with packwiz. From inside `pack/`:

```sh
packwiz refresh                # regenerate index after editing a .pw.toml
packwiz cf add <slug>          # add a CurseForge mod
packwiz update --all           # bump every mod to its latest 1.21.1 NeoForge release
packwiz curseforge export      # build the CF zip
```

Install packwiz with `go install github.com/packwiz/packwiz@latest` — packwiz has no GitHub releases or winget package; Go install is the only path.

## Distribution

**CurseForge only.** The FTB utility stack (FTB Library / Quests / Teams / Chunks / Ranks / Essentials) is CurseForge-only, and Modrinth's policy rejects packs that inline CF jars as overrides. Since FTB Quests is the canonical questbook for this kind of pack, Modrinth isn't viable. GitHub Releases mirrors each tag's artifacts for transparency; players install from CurseForge.

The pack page copy lives in [`docs/curseforge_page.md`](./docs/curseforge_page.md) — edit there first, push to CurseForge.

## License

[MIT](./LICENSE) for the pack-authored content (KubeJS scripts, configs, datapacks, questbook, branding, docs). Each bundled mod retains its own license — see [`NOTICE.md`](./NOTICE.md) for scope details.
