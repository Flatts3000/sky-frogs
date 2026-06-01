<!--
Paste-ready CurseForge project description (markdown). Copy everything below
this comment into the CF dashboard's Description field at project creation
(or via Edit Project later).

Source: derived from curseforge_page.md (the meta-doc with sectioning).
This file is the actual page body without the meta labels.
Status: covers the content-complete alpha (Welcome through Void + the Master Pond endgame). Refresh at v1.0. Push to the live CF page only when the matching release is tagged (the live listing should match what downloaders get).
-->

# Sky Frogs

> A void-skyblock NeoForge 1.21.1 modpack built around [Productive Frogs](https://www.curseforge.com/minecraft/mc-mods/productive-frogs).

**Status: alpha, content-complete.** All six tiers (Welcome / Cave / Geode / Bog / Tide / Infernal / Void) are built and playable end-to-end - frogs for ores, gems, organics, the ocean, the Nether, and the End - finishing with a real dragon expedition and a singularity-powered endgame that caps off in the **Sky Frogs Master Frog** trophy. What remains is balance, polish, and art. Feedback welcome via [GitHub Issues](https://github.com/Flatts3000/sky-frogs/issues).

---

You spawn on a speck of land over the void. No ore to mine, no Nether to raid, no mountain to dig into. What you've got is **frogs** - and out here, that turns out to be the same thing as a mine.

Everything from your first iron to the endgame comes through **Resource Frogs**: six species of breedable frog, each one eating its matching slimes and handing back **Froglights** you smelt into the real thing. Sky Frogs wraps that core mod in an FTB Quests campaign that walks you from a single dark-room slime farm to a frog for every resource in the game.

## Features

- **Species-gated progression.** Six frog species, unlocked in order - **Cave, Geode, Bog, Tide, Infernal, Void** - each one a whole new family of resources. Finish one species' chapter to bootstrap the next.
- **You already know the controls.** Every interaction is a vanilla right-click: glass bottles, slimeballs, water buckets, frogspawn. No custom UIs to learn.
- **No mining shortcuts.** Laser drills, quarries, digital miners - recipe-stripped or hidden. The frogs are the path, and the pack enforces it.
- **Cross-mod by JSON.** Any modded resource can be made frog-farmable with a single `slime_variant` JSON file, so the whole modded-resource ecosystem plugs into the same loop. No Java, no source-fork.
- **A questbook that actually guides you.** FTB Quests walks every tier: a chapter per species, plus side chapters for the tech mods. If you're lost, the answer's in the book.

## How to Play (your first hour)

1. **Spawn** on your island with a starter kit: saplings, a water bucket, a lava bucket. The questbook opens itself.
2. **Make cobblestone the old-fashioned way:** water next to lava, infinite cobble. (Enjoy the pickaxe while it lasts.)
3. **Get a second water source.** An Ex Deorum barrel catches rain; bottle it onto your island for an infinite water square.
4. **Wall off a dark room.** **Cave Slimes** spawn in the dark here - they're your first ore source.
5. **Farm them** for slimeballs, and keep an eye out for the occasional Iron Slime.
6. **Finish the Welcome chapter** and you're handed a **Bottle of Cave Frog Frogspawn** (a breeding pair's worth).
7. **Pour it on water.** Cave Frogs hatch. Feed one an Iron Slime, an **Iron Froglight** drops, smelt it: your first iron.

By the end of a session, iron is a frog's problem, not yours. The book drives the rest.

## The Six Frog Species

| Tier | Species  | What it gives you                                                                  | State |
|------|----------|-------------------------------------------------------------------------------------|-------|
| 1    | Cave     | The ores: iron, copper, gold, coal, redstone                                       | Playable |
| 2    | Geode    | Gems and crystals: lapis, tuff, calcite, amethyst, emerald, diamond                | Playable |
| 3    | Bog      | Organics: dirt, moss, clay, mycelium, leather, feather, plus plastic and pink slime | Playable |
| 4    | Tide     | The ocean's haul: prismarine, sponge, sea pickles, nautilus shells (and jetpacks)  | Playable |
| 5    | Infernal | The Nether, earned by one real fortress trip: quartz, glowstone, blaze, netherite  | Playable |
| 6    | Void     | The End and endgame: ender pearls, end stone, chorus, echo shards, sculk, shulker shells | Playable |

Each tier extends with modded resources as those mods ship in the pack. The endgame: compress a thousand froglights into a Froglight Singularity (a proof you automated your farm), refine it into the Ultimate Singularity, and craft the **Sky Frogs Master Frog**, a trophy that says you out-frogged the game.

## Mod Highlights

The full mod list is in the repo at [`docs/mod_list.md`](https://github.com/Flatts3000/sky-frogs/blob/main/docs/mod_list.md). The load-bearing picks:

- **Productive Frogs** - the core mod. Six frog species, hand-operated appliances, datapack-driven slime variants.
- **Skyblock Builder** - void worldgen, the starter island, per-player island UI.
- **Ex Deorum** - crucibles, the porcelain bucket, and rain-collection barrels (your second water source). Sieving is disabled in this pack; Tier 0 runs on a dark-room slime farm instead.
- **FTB Quests + Library + Teams + Chunks + Ranks + Essentials** - questbook, claims, party support, server admin, `/home` / `/spawn`.
- **JEI + Jade** - recipe browser and in-world block info. Standard quality-of-life.
- **Mekanism** (Tier 2 verb) - power, Metallurgic Infuser, Enrichment Chamber.
- **Just Dire Things + Building Gadgets 2** (Tier 3 verb) - utility / automation toys; the JDT goo and gadget chain.
- **Industrial Foregoing** (Tier 4 gateway) - the Dissolution Chamber is the pack's slime engine; resource-threaded chamber recipes for every tier.
- **Refined Storage** (Tier 5 verb) - the digital storage + autocrafting network, gated on nether quartz.
- **Extended Crafting** (Tier 6 verb + endgame) - the tiered crafting tables and the Quantum Compressor that turns froglights into singularities, ending in the Master Frog trophy.

Every bundled mod keeps its own license; see each mod's CurseForge page. The pack's own content (configs, KubeJS, datapacks, questbook, branding) is MIT.

## FAQ

**Why frogs?**
Because "feed a slime to a frog, get an ingot" is a loop you can explain in one sentence and never tire of. It rides on vanilla idioms (frogspawn, water bottles, slimeballs) so there's almost nothing new to learn, and the six species give the campaign a clean tier-by-tier shape that keeps growing.

**Can I add my own modded resource as a frog target?**
Yes; that's the whole design. Drop a single JSON at `data/<namespace>/productivefrogs/slime_variant/<name>.json`, wrap it in `neoforge:conditions` for `mod_loaded`, and the matching-species frog will eat it. No Java, no PR to the underlying mod.

**Is automation possible?**
Yes, but never required. Productive Frogs is hand-operated by design; the pack is completable with hoppers, water streams, and patience. Tech mods make it faster, not mandatory.

**Server-friendly?**
Yes. Each release ships a server pack alongside the client. Party support via FTB Teams, claims via FTB Chunks, `/home` and `/tpa` via FTB Essentials. Balance is single-player-tuned for now; multiplayer tuning is a later stretch goal.

**Will my world break on updates?**
Pre-1.0: possibly. Any world wipe is called out in the changelog. Post-1.0: world-breaking changes bump the major version and get flagged in **bold** at the top of the release notes. Hotfixes and content additions never break worlds.

**Modrinth release?**
Not planned. The FTB utility stack and Productive Frogs are CurseForge-only, and Modrinth forbids inlining CF mods as overrides. FTB Quests is load-bearing for the campaign, so CF stays the sole channel.

## Links

- **Source code:** [github.com/Flatts3000/sky-frogs](https://github.com/Flatts3000/sky-frogs)
- **Bug reports:** [GitHub Issues](https://github.com/Flatts3000/sky-frogs/issues)
- **Questions and suggestions:** [GitHub Discussions](https://github.com/Flatts3000/sky-frogs/discussions)
- **The underlying mod:** [Productive Frogs on CurseForge](https://www.curseforge.com/minecraft/mc-mods/productive-frogs)

## License

MIT for the pack-authored content (KubeJS scripts, configs, datapacks, questbook, branding, docs). Each bundled mod retains its own license; refer to each mod's CurseForge page for terms.
