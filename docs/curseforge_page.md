# CurseForge Project Page

> **Status:** DRAFT — first pass at the public-facing copy for the CurseForge listing. Sections map to the standard CurseForge modpack page layout. Edits welcome; ship-ready bar is "would a player decide to install based on this in 60 seconds?"

This is the copy that lives on `curseforge.com/minecraft/modpacks/sky-frogs`. Paste each section into the corresponding CF page region at submission time. Keep this file in sync with the live page — edit here first, push to CF.

---

## Tagline (short description, ~120 chars)

> Skyblock where frogs replace mining. Breed Resource Frogs, feed them matching Resource Slimes, collect every metal, gem, and ender shard the pack ships.

---

## Hook (first paragraph on the page)

Sky Frogs is a void-skyblock modpack for NeoForge 1.21.1. You spawn on a 3×3 dirt island with one tree and one chest. There's no overworld to mine. There's no Nether to raid for ancient debris. The only way to iron — and to everything past iron — is through **Resource Frogs**: six categories of breedable frogs that each eat category-matching slimes and produce Configurable Froglights you smelt into ingots.

It's built around [Productive Frogs](https://www.curseforge.com/minecraft/mc-mods/productive-frogs) (the underlying mod) and shaped by the FTB Quests questbook into a 50–80 hour campaign from first iron to the endgame creative trophy.

---

## Features (5-bullet scannable list)

- **Category-based progression, deep slime ecosystem.** Six clear tiers — Metallic, Mineral, Gem, Aquatic, Infernal, Arcane — with many slime variants inside each. The frog roster grows over time; the tier structure stays legible.
- **Vanilla-feeling mechanics.** Every interaction is right-click on a block: glass bottles, slimeballs, water buckets, frogspawn. No custom UIs to learn.
- **Mining shortcuts disabled by design.** Laser drills, mining lenses, digital miners, and quarry cards are recipe-stripped or hidden from JEI. The frog tree is the path; the pack enforces it.
- **Cross-mod resources, one JSON each.** Every modded resource you want frog-farmable is a single `slime_variant/*.json` drop — Mekanism, AE2, Industrial Foregoing, Powah, EnderIO, all hook into the same loop.
- **~750 quests across 22 chapters** at v1.0, with FTB Quests as the canonical guide. Six tier chapters + a per-mod side chapter for every significant tech mod.

---

## How to Play (Tier 0 walkthrough)

Your first hour:

1. **Spawn** on a 3×3 dirt island. Your starter chest has the bare essentials — sapling, a water source, an Ex Deorum porcelain bucket, the first frogspawn.
2. **Set up the sieve loop.** Crush dirt → pebbles → cobble. Sieve crushed netherrack/stone with the right mesh until you have a few iron nuggets.
3. **Smelt your first iron ingot** in a vanilla furnace.
4. **Make a glass bottle.** Sieving gives you sand → smelt to glass → craft.
5. **Hatch your first Resource Frog.** Right-click your starter frogspawn with the glass bottle → Frog Egg item. Place on water. Prime with the iron ingot. Wait for hatch.
6. **Feed it slimes.** The questbook will walk you through getting your first Iron Slime — the Tier 1 "Metallic Mastery" chapter is your guide from here.

Within two hours of starting, you should have your first **Iron Configurable Froglight** dropping. Within a play session, your iron problem is solved forever.

The questbook drives everything. If you're not sure what's next, open it.

---

## The Six Frog Tiers (preview table)

| Tier | Category   | Unlocks                                                        |
|------|------------|----------------------------------------------------------------|
| 1    | Metallic   | Iron, copper, gold, plus modded metals (osmium, tin, aluminum…) |
| 2    | Mineral    | Redstone, lapis, coal, quartz, amethyst, certus, fluix          |
| 3    | Gem        | Diamond, emerald, fluorite, peridot, ruby, sapphire             |
| 4    | Aquatic    | Prismarine, kelp, nautilus, pink slime, latex                   |
| 5    | Infernal   | Blaze rods, quartz, magma, glowstone, netherite line            |
| 6    | Arcane     | Ender pearls, chorus, draconic, dimensional shards, end-tier    |

Endgame: combine late-Arcane Configurable Froglights into singularities, then into the **Sky Frogs Master Frog** creative trophy.

---

## Mod Highlights

The full mod list lives in the repo's [`docs/mod_list.md`](https://github.com/Flatts3000/sky-frogs/blob/main/docs/mod_list.md). The load-bearing picks:

- **Productive Frogs** — the core mod. Six frog categories, hand-operated appliances, datapack-driven slime variants.
- **Skyblock Builder** — void worldgen, starter island, per-player island UI.
- **Ex Deorum** — sieve / hammer / crucible bootstrap loop. The only way out of Tier 0.
- **FTB Quests + Library + Teams + Chunks + Ranks + Essentials** — questbook, claims, party support, server admin, `/home`/`/spawn`.
- **JEI + Jade** — recipe browser and in-world block info. Standard QoL.
- **Mekanism, AE2, Industrial Foregoing, Powah, EnderIO** — the tech mods that supply resource categories and post-bootstrap automation.

Every mod retains its own license. Refer to each mod's CurseForge page for license terms. The pack's own content (configs, KubeJS, datapack overrides, questbook, branding) is MIT.

---

## FAQ

**Why frogs?**
Productive Frogs leans hard on vanilla idioms — frogspawn, water bottles, slimeballs, lead-based transport. Every interaction is something a vanilla player already knows how to do, and the category-based progression gives the questbook a clean tier-by-tier structure that scales as the frog roster grows.

**Can I add my own modded resource as a frog target?**
Yes — that's the design center. Drop a single JSON at `data/<namespace>/productivefrogs/slime_variant/<name>.json` with the standard schema (see the repo `docs/kubejs_overrides.md`), wrap in `neoforge:conditions → mod_loaded` for your mod, and the matching-category frog will eat it. No Java change, no PR required to the underlying mod.

**Is automation possible?**
Yes, but not required. Productive Frogs V1 ships hand-operated appliances only. The pack is completable with hoppers, water streams, and patience. Tech-mod automation (Mekanism, AE2, Industrial Foregoing) makes things faster, but the progression doesn't gate behind it.

**Server-friendly?**
Yes. Each release ships a server pack zip alongside the client. Skyblock party support via FTB Teams, claims via FTB Chunks, `/home` / `/tpa` via FTB Essentials. Server balance is single-player-tuned at v1.0 — multiplayer-specific tuning is a v1.x stretch goal.

**Will my world break on updates?**
Pre-1.0: maybe. We're in active development; world wipes are signaled in the changelog. Post-1.0: world-breaking changes bump the major version and are called out in **bold** at the top of the release notes. Hotfixes and content additions never break worlds.

---

## Screenshots (TBD)

Gallery slots to fill before launch:

1. Hero shot: void skyblock with one tree + starter chest, frog visible.
2. Tier 1 enclosure: Metallic Frog eating Iron Slimes, Froglights stacking in a hopper.
3. Tier 3 multi-enclosure scene: several Gem Frog setups in a row.
4. Endgame singularity altar.
5. The questbook UI open to a tier chapter.
6. Tier 5/6 Nether or End set piece.

Capture order: Tier 1 first (it's reachable in the v0.1 alpha); the rest as later tiers go live.

---

## Links

- **Source code:** [github.com/Flatts3000/sky-frogs](https://github.com/Flatts3000/sky-frogs)
- **Bug reports:** [GitHub Issues](https://github.com/Flatts3000/sky-frogs/issues)
- **Questions / suggestions:** [GitHub Discussions](https://github.com/Flatts3000/sky-frogs/discussions)
- **The underlying mod:** [Productive Frogs on CurseForge](https://www.curseforge.com/minecraft/mc-mods/productive-frogs)

---

## License

MIT for the pack-authored content (KubeJS, configs, datapacks, questbook, branding, docs). Each bundled mod retains its own license. Refer to each mod's CurseForge page for license terms.
