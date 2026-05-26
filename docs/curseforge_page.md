# CurseForge Project Page

> **Status:** DRAFT — public-facing copy for the CurseForge listing, written in the pack voice (see [`voice_and_tone.md`](./voice_and_tone.md)). Sections map to the standard CF modpack page layout. Ship-ready bar: "would a player decide to install based on this in 60 seconds?"

This is the copy that lives on `curseforge.com/minecraft/modpacks/sky-frogs`. Paste each section into the matching CF page region at submission. Edit here first, then push to CF.

---

## Tagline (short description, ~120 chars)

> A skyblock where frogs do the mining. Breed Resource Frogs, feed them slimes, and watch the ore, gems, and ender pearls fall out.

---

## Hook (first paragraph on the page)

You spawn on a speck of land over the void. No ore to mine, no Nether to raid, no mountain to dig into. What you've got is frogs - and out here, that turns out to be the same thing as a mine.

Everything from your first iron to the endgame comes through **Resource Frogs**: six species of breedable frog, each one eating its matching slimes and handing back **Froglights** you smelt into the real thing. Sky Frogs is built on [Productive Frogs](https://www.curseforge.com/minecraft/mc-mods/productive-frogs) for NeoForge 1.21.1, and wrapped in an FTB Quests campaign that walks you from a single dark-room slime farm to a frog for every resource in the game.

---

## Features (5-bullet scannable list)

- **Species-gated progression.** Six frog species, unlocked in order - **Cave, Geode, Bog, Tide, Infernal, Void** - each one a whole new family of resources. Finish one species' chapter to bootstrap the next.
- **You already know the controls.** Every interaction is a vanilla right-click: glass bottles, slimeballs, water buckets, frogspawn. No custom UIs to learn.
- **No mining shortcuts.** Laser drills, quarries, digital miners - recipe-stripped or hidden. The frogs are the path, and the pack enforces it.
- **Cross-mod by JSON.** Any modded resource can be made frog-farmable with a single `slime_variant` file, so the whole modded-resource ecosystem plugs into the same loop.
- **A questbook that actually guides you.** FTB Quests walks every tier - a chapter per species, plus side chapters for the tech mods. If you're lost, the answer's in the book.

---

## How to Play (Tier 0 walkthrough)

Your first hour, roughly:

1. **Spawn** on your island with a starter kit - saplings, a water bucket, a lava bucket. The questbook opens itself.
2. **Make cobblestone the old-fashioned way:** water next to lava, infinite cobble. (Enjoy the pickaxe while it lasts.)
3. **Get a second water source.** An Ex Deorum barrel catches rain; bottle it onto your island for an infinite water square.
4. **Wall off a dark room.** **Cave Slimes** spawn in the dark here - they're your first ore source.
5. **Farm them** for slimeballs, and keep an eye out for the occasional Iron Slime.
6. **Finish the Welcome chapter** → you're handed a **Bottle of Cave Frog Frogspawn** (a breeding pair's worth).
7. **Pour it on water** → Cave Frogs hatch. Feed one an Iron Slime → an **Iron Froglight** drops → smelt it → your first iron.

By the end of a session, iron is a frog's problem, not yours. The book drives the rest.

---

## The Six Frog Species (preview table)

| Tier | Species  | What it gives you                                                  |
|------|----------|---------------------------------------------------------------------|
| 1    | Cave     | The ores: iron, copper, gold, coal, lapis, redstone, diamond        |
| 2    | Geode    | Gems & crystals: emerald, amethyst (and modded crystals)            |
| 3    | Bog      | Organics & mob-drops: bone, string, leather, gunpowder, slime       |
| 4    | Tide     | The ocean's haul: prismarine, sponge, ink                           |
| 5    | Infernal | The Nether: blaze, quartz, glowstone, netherite                     |
| 6    | Void     | The End & endgame: ender pearls, chorus, shulker shells             |

Each tier extends with modded resources as those mods ship in the pack. Endgame: stack up your late-game Froglights into singularities, then into the **Sky Frogs Master Frog** - a creative trophy that says you out-frogged the game.

---

## Mod Highlights

The full mod list lives in the repo's [`docs/mod_list.md`](https://github.com/Flatts3000/sky-frogs/blob/main/docs/mod_list.md). The load-bearing picks:

- **Productive Frogs** - the core mod. Six frog species, hand-operated appliances, datapack-driven slime variants.
- **Skyblock Builder** - void worldgen, the starter island, per-player island UI.
- **Ex Deorum** - crucibles, the porcelain bucket, and rain-collection barrels (your second water source). Sieving is disabled here; Tier 0 runs on a dark-room slime farm instead.
- **FTB Quests + Library + Teams + Chunks + Ranks + Essentials** - questbook, claims, party support, server admin, `/home` / `/spawn`.
- **JEI + Jade** - recipe browser and in-world block info. Standard quality-of-life.
- **Tech mods** (added through the mid-game tiers) extend the resource pools and offer optional automation - never required to progress.

Every bundled mod keeps its own license; see each mod's CurseForge page. The pack's own content (configs, KubeJS, datapacks, questbook, branding) is MIT.

---

## FAQ

**Why frogs?**
Because "feed a slime to a frog, get an ingot" is a loop you can explain in one sentence and never tire of. It rides on vanilla idioms - frogspawn, water bottles, slimeballs - so there's almost nothing new to learn, and the six species give the campaign a clean tier-by-tier shape that keeps growing.

**Can I add my own modded resource as a frog target?**
Yes - that's the whole design. Drop a single JSON at `data/<namespace>/productivefrogs/slime_variant/<name>.json`, wrap it in `neoforge:conditions → mod_loaded`, and the matching-species frog will eat it. No Java, no PR to the underlying mod.

**Is automation possible?**
Yes, but never required. Productive Frogs is hand-operated by design; the pack is completable with hoppers, water streams, and patience. Tech mods make it faster, not mandatory.

**Server-friendly?**
Yes. Each release ships a server pack alongside the client - party support via FTB Teams, claims via FTB Chunks, `/home` and `/tpa` via FTB Essentials. Balance is single-player-tuned for now; multiplayer tuning is a later stretch goal.

**Will my world break on updates?**
Pre-1.0: possibly - we're in active development, and any world wipe is called out in the changelog. Post-1.0: world-breaking changes bump the major version and get flagged in **bold** at the top of the release notes. Hotfixes and content additions never break worlds.

---

## Screenshots (TBD)

Gallery slots to fill before launch:

1. Hero shot: the void starter island, a frog in frame.
2. Tier 1: a Cave Frog eating Iron Slimes, Froglights stacking in a hopper.
3. A multi-species enclosure scene a few tiers in.
4. The endgame singularity setup.
5. The questbook open to a species chapter.
6. A Nether or End set piece (Tier 5/6).

Capture order: Tier 1 first (reachable in the alpha); the rest as later tiers go live.

---

## Links

- **Source code:** [github.com/Flatts3000/sky-frogs](https://github.com/Flatts3000/sky-frogs)
- **Bug reports:** [GitHub Issues](https://github.com/Flatts3000/sky-frogs/issues)
- **Questions / suggestions:** [GitHub Discussions](https://github.com/Flatts3000/sky-frogs/discussions)
- **The underlying mod:** [Productive Frogs on CurseForge](https://www.curseforge.com/minecraft/mc-mods/productive-frogs)

---

## License

MIT for the pack-authored content (KubeJS, configs, datapacks, questbook, branding, docs). Each bundled mod retains its own license; refer to each mod's CurseForge page for terms.
