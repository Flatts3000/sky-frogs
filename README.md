# Sky Frogs

A void-skyblock modpack for **NeoForge 1.21.1** built around [Productive Frogs](https://github.com/Flatts3000/productive-frogs).

You spawn on a 3×3 dirt island. There's no overworld to mine. The only way past iron is through **Resource Frogs**: six categories of breedable frogs that each eat category-matching slimes and produce Froglights you smelt into ingots.

## Concept

```
Find frogspawn → bottle it → prime the egg with a category material →
hatch into a Resource Frog → feed it a matching Resource Slime →
collect Froglight → smelt or crush for ingots
```

Six frog categories define the tier progression:

| Tier | Category   | Unlocks                                                        |
|------|------------|----------------------------------------------------------------|
| 1    | Cave       | Iron, copper, gold, coal, redstone, plus modded metals (osmium, tin, aluminum…) |
| 2    | Geode      | Lapis, amethyst, calcite, emerald, diamond, plus AE2/processor gems |
| 3    | Bog        | Dirt, mud, clay, moss, leather, the mob drops (bone, string, gunpowder…), plastic, pink slime |
| 4    | Tide       | Prismarine, sponge, ink, sea pickle, ice/snow, nautilus shell   |
| 5    | Infernal   | Quartz, glowstone, blaze, soul sand, netherite scrap, the boss trophies |
| 6    | Void       | End stone, chorus, echo shard, sculk, shulker, dragon egg/breath |

Slime species supply the variety inside each tier — adding a new modded resource is a single `slime_variant/*.json` drop, never a Java change.

## Design pillars

- **Vanilla-feeling mechanics.** Productive Frogs leans on vanilla idioms — frogspawn, slimeballs, water bottles, lead-based mob transport. Every interaction is right-click on a block; no custom UIs.
- **Category-based progression.** Six clear tiers (Cave / Geode / Bog / Tide / Infernal / Void) anchor the questbook in a structure that stays legible as more frog and slime variants ship.
- **Cross-mod compat is the design center.** Drop a JSON, get a frog-eats-that-thing variant. Community PRs adding new modded resources need zero Java work.
- **Mining shortcuts disabled by design.** Laser drills, mining lenses, digital miners, and quarry cards are recipe-stripped or hidden from JEI. The frog tree is the path; the pack enforces it.

## Status

**Out of beta - the complete campaign is live on [CurseForge](https://www.curseforge.com/minecraft/modpacks/sky-frogs) (v1.4.4).** All six species tiers (Cave, Geode, Bog, Tide, Infernal, Void) are built and playable end-to-end - 27 FTB Quests chapters / ~343 quests, the per-tier slime chains, the dragon expedition and singularity endgame capped by the Master Frog trophy, the Trophy Pond boss campaign, the Terrarium automation multiblock, and the Completionist census. Releases are tag-driven and ship to GitHub + CurseForge automatically (client + dedicated-server packs); balance, polish, and art are still in motion, driven by player feedback (CurseForge comments and the community Discord).

Docs in [`docs/`](./docs/) describe the built campaign; [`CHANGELOG.md`](./CHANGELOG.md) tracks every release.

## Quick navigation

For players:
- [Play it: Sky Frogs on CurseForge](https://www.curseforge.com/minecraft/modpacks/sky-frogs)
- [Community Discord](https://discord.gg/r6MhZ73nsM) - chat, support, suggestions, release announcements
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

> **No bounties.** This project doesn't offer bounties or use Opire/Algora; bounty-platform commands are ignored, and unsolicited bot PRs are closed unreviewed. See [CONTRIBUTING](./CONTRIBUTING.md#no-bounties-no-automated-prs).

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
