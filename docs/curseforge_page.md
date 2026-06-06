# CurseForge Project Page

> **The single source of truth for the live CF listing.** Edit here, then push to
> CurseForge **only when the matching release is tagged** (the live listing should
> match what downloaders get). Written in the pack voice (see
> [`voice_and_tone.md`](./voice_and_tone.md)); ship-ready bar: "would a player
> decide to install based on this in 60 seconds?"
>
> Everything **below the PASTE MARKER** is the CF **Description** field, verbatim -
> no meta labels to strip. The few dashboard fields that live OUTSIDE the
> description are right here above the marker.

**Tagline** (the ~120-char short-description field):

> A skyblock where frogs do the mining. Breed Resource Frogs, feed them slimes, and watch the ore, gems, and ender pearls fall out.

**Gallery screenshots** (TBD - capture order, 1920x1080, see [`branding.md`](./branding.md) + [`cf_submission_checklist.md`](./cf_submission_checklist.md)):

1. Hero shot: the void starter island, a frog in frame.
2. Tier 1: a Cave Frog eating Iron Slimes, Froglights stacking in a hopper.
3. A multi-species enclosure scene a few tiers in.
4. The endgame singularity setup.
5. The questbook open to a species chapter.
6. A Nether or End set piece (Tier 5/6).

---

<!-- PASTE MARKER: everything below this comment goes into the CF Description field verbatim. -->

# Sky Frogs

> A void-skyblock NeoForge 1.21.1 modpack built around [Productive Frogs](https://www.curseforge.com/minecraft/mc-mods/productive-frogs).

**Status: beta, content-complete.** All six tiers (Cave / Geode / Bog / Tide / Infernal / Void) are built and playable end-to-end - frogs for ores, gems, organics, the ocean, the Nether, and the End - finishing with a real dragon expedition and a singularity-powered endgame that caps off in the **Sky Frogs Master Frog** trophy. What remains is balance, polish, and art. Feedback welcome on the [community Discord](https://discord.gg/r6MhZ73nsM) or via [GitHub Issues](https://github.com/Flatts3000/sky-frogs/issues).

---

You spawn on a speck of land over the void. No ore to mine, no Nether to raid, no mountain to dig into. What you've got is **frogs** - and out here, that turns out to be the same thing as a mine.

Everything from your first iron to the endgame comes through **Resource Frogs**: six species of breedable frog, each one eating its matching slimes and handing back **Froglights** you smelt into the real thing. Sky Frogs wraps that core mod in an FTB Quests campaign that walks you from a single dark-room slime farm to a frog for every resource in the game.

## Features

- **Species-gated progression.** Six frog species, unlocked in order - **Cave, Geode, Bog, Tide, Infernal, Void** - each one a whole new family of resources. Finish one species' chapter to bootstrap the next.
- **You already know the controls.** Every interaction is a vanilla right-click: glass bottles, slimeballs, water buckets, frogspawn. No custom UIs to learn.
- **No mining shortcuts.** Laser drills, quarries, digital miners - recipe-stripped or hidden. The frogs are the path, and the pack enforces it. (Builders get one curated exception: a string-mesh sieve over dirt and moss that drops saplings and garden flora - decor only, never resources.)
- **Cross-mod by JSON.** Any modded resource can be made frog-farmable with a single `slime_variant` JSON file, so the whole modded-resource ecosystem plugs into the same loop. No Java, no source-fork.
- **A questbook that actually guides you.** FTB Quests walks every tier: a chapter per species, plus side chapters for the tech mods. If you're lost, the answer's in the book.
- **Built from player feedback.** Most updates start as somebody's Discord message or CurseForge comment - the welcome chapter hands you the invite (or click Join the Pond in-game).

## How to Play (your first hour)

1. **Spawn** on your island with a starter kit: saplings, a water bucket, a lava bucket. The questbook opens itself.
2. **Make cobblestone the old-fashioned way:** water next to lava, infinite cobble. (Enjoy the pickaxe while it lasts.)
3. **Get a second water source.** An Ex Deorum barrel catches rain; bottle it onto your island for an infinite water square.
4. **Wall off a dark room** - at least 5x5 and 3 tall. **Cave Slimes** spawn in the dark here; they're your first ore source, and bigger rooms fill faster.
5. **Farm them** for slimeballs, and keep an eye out for the occasional Iron Slime.
6. **Finish the Welcome chapter** and you're handed a **Bottle of Cave Frog Frogspawn** (a breeding pair's worth).
7. **Pour it on water.** Cave Frogs hatch. Feed one an Iron Slime, an **Iron Froglight** drops, smelt it: your first iron.

By the end of a session, iron is a frog's problem, not yours. The book drives the rest.

## The Six Frog Species

| Tier | Species  | What it gives you                                                                  |
|------|----------|-------------------------------------------------------------------------------------|
| 1    | Cave     | The ores: iron, copper, gold, coal, glow ink, redstone                             |
| 2    | Geode    | Gems and crystals: lapis, tuff, calcite, amethyst, emerald, diamond                |
| 3    | Bog      | Organics: dirt, moss, clay, mycelium, leather, feather, plus plastic and pink slime |
| 4    | Tide     | The ocean's haul: prismarine, sponge, ink, sea pickles, nautilus shells (and jetpacks) |
| 5    | Infernal | The Nether, earned by one real fortress trip: obsidian, quartz, glowstone, blaze, netherite |
| 6    | Void     | The End and endgame: ender pearls, end stone, chorus, echo shards, sculk, shulker shells (earned by a real dragon expedition) |

Each tier extends with modded resources as those mods ship in the pack. The endgame: compress a thousand of each of the frogs' forty resources into its own Singularity (a proof you automated every farm), fold all forty into the Ultimate Singularity, and craft the **Sky Frogs Master Frog**, a trophy that says you out-frogged the game.

## Mod Highlights

The full mod list is in the repo at [`docs/mod_list.md`](https://github.com/Flatts3000/sky-frogs/blob/main/docs/mod_list.md). The load-bearing picks:

- **Productive Frogs** - the core mod. Six frog species, hand-operated appliances, datapack-driven slime variants.
- **Skyblock Builder** - void worldgen, the starter island, per-player island UI.
- **Ex Deorum** - crucibles, the porcelain bucket, rain-collection barrels (your second water source), and the End Cake (your ticket to the dragon). Resource sieving is disabled in this pack - Tier 0 runs on a dark-room slime farm - but a small builders' sieve lane drops decor flora and starter food seeds.
- **FTB Quests + Library + Teams + Chunks + Ranks + Essentials** - questbook, claims, party support, server admin, `/home` / `/spawn`.
- **JEI + Jade** - recipe browser and in-world block info. Standard quality-of-life.
- **Sodium + Lithium + FerriteCore + ModernFix** - the standard performance stack.
- **Mekanism** (Tier 2 verb) - power, Metallurgic Infuser, Enrichment Chamber.
- **Powah! + Flux Networks** (the power-scaling arc) - Furnator to Reactor, wireless energy everywhere - and every Powah material plus Flux Dust is frog-farmable. On a void skyblock, the frog is the uranium mine.
- **Just Dire Things + Building Gadgets 2** (Tier 3 verb) - utility / automation toys; the JDT goo and gadget chain.
- **Industrial Foregoing + IF Souls** (Tier 4 gateway) - the Dissolution Chamber is the pack's slime engine; resource-threaded chamber recipes for every tier. Souls adds an optional Tier 6 flex: summon and farm the Warden, entirely from frog-farmed sculk.
- **Iron Jetpacks** (Tier 4 verb) - FE-charged flight; what makes the void-Nether fortress run feasible.
- **Refined Storage** (Tier 5 verb) - the digital storage + autocrafting network, gated on nether quartz.
- **Extended Crafting** (Tier 6 verb + endgame) - the tiered crafting tables and the Quantum Compressor that turns froglights into singularities, ending in the Master Frog trophy.
- **Quality of life, the modern set** - GraveStone (your items wait for you), Inventory Essentials (bulk ctrl-shift-click moves), Cable Facades (hide pipes in any block), Extreme Sound Muffler (silence the plap plaps, per sound), Botany Pots + Botany Trees (toolless self-tending planters - trees included).

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

- **Community Discord:** [discord.gg/r6MhZ73nsM](https://discord.gg/r6MhZ73nsM) - chat, support, suggestions, and release announcements
- **Source code:** [github.com/Flatts3000/sky-frogs](https://github.com/Flatts3000/sky-frogs)
- **Bug reports:** [GitHub Issues](https://github.com/Flatts3000/sky-frogs/issues)
- **The underlying mod:** [Productive Frogs on CurseForge](https://www.curseforge.com/minecraft/mc-mods/productive-frogs)

## License

MIT for the pack-authored content (KubeJS scripts, configs, datapacks, questbook, branding, docs). Each bundled mod retains its own license; refer to each mod's CurseForge page for terms.
