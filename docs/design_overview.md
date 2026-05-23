# Design Overview

## Inspiration

Two pieces of existing Minecraft content seeded this pack:

1. **Sky Bees Reborn** (NeoForge 1.21.1, by Anderzz) — a void skyblock where [Productive Bees](https://www.curseforge.com/minecraft/mc-mods/productive-bees) is the only viable resource generator. Automated mining alternatives (laser drills, mining lenses) are disabled, forcing the player through the bee-breeding tree.
2. **Productive Frogs** — a content mod by the same author as this pack that generalizes the vanilla `frog-eats-magma-cube-drops-froglight` mechanic into a Productive-Bees-shaped loop. Frogs of one of six categories eat slimes of matching categories and drop tier-specific Configurable Froglights.

Sky Frogs is what you get when you swap the Productive Bees pillar of Sky Bees Reborn for Productive Frogs and rebuild the surrounding scaffolding around the category model.

## Core Concept

A **void skyblock** where the player must bootstrap from a 3×3 dirt island and the only path past iron is through the **Resource Frog** breeding tree. Each tier unlocks a new frog category, which in turn unlocks a new family of resources via category-matching Resource Slimes.

```
Tier 0: Vanilla bootstrap   → glass bottle + slimeballs + an iron primer
Tier 1: Metallic            → iron, copper, gold (and modded metals via tag)
Tier 2: Mineral             → redstone, lapis, coal, (modded minerals)
Tier 3: Gem                 → diamond, emerald, amethyst, fluorite, certus
Tier 4: Aquatic             → prismarine, nautilus, sea-themed resources
Tier 5: Infernal            → blaze, quartz, magma, netherite line
Tier 6: Arcane              → ender, draconic, end-tier and modded magic
```

Each tier corresponds to one or two questbook chapters and to one category in the [Productive Frogs Category enum](../../productive-frogs/src/main/java/com/flatts/productivefrogs/data/Category.java).

## Why Sky Frogs and not just play Sky Bees Reborn?

Three differences justify a distinct pack:

1. **Frog mechanics are more vanilla-feeling.** Productive Frogs leans on existing vanilla idioms (frogspawn, slimeballs, water buckets, glass bottles) for nearly every interaction. There is no custom UI for breeding; everything is right-click on a block. Sky Bees Reborn inherits Productive Bees' (excellent but) heavier UX of bottler, centrifuge, honey treats, honey gen, etc.
2. **Smaller frog roster, deeper slime roster.** Six frogs, dozens of slime species. Players never have a giant unmemorable bee zoo; instead, they have six well-loved frogs and a sprawling slime ecosystem. This makes questbook design cleaner — six top-level chapters for the frog tiers, and per-resource side quests for slime variants.
3. **Data-driven extensibility is the design center.** Adding a modded resource to the pack is a single JSON file (`slime_variant/<name>.json`) plus a tag entry, never a Java change. Sky Frogs leans into this hard: pack-side KubeJS scripts generate dozens of `slime_variant` JSONs from the mods we ship, and a community-PR pattern is "drop a JSON, get a frog-eats-that-thing variant."

## What this pack is NOT

- **Not a kitchen-sink pack.** Mods are chosen to either (a) supply a tier of resources that frogs farm, (b) provide automation and logistics for the post-bootstrap economy, or (c) round out the skyblock fundamentals (water/lava sources, leaves→sticks, etc.). Random "I like this mod" inclusions get rejected; if a mod doesn't slot into a chapter, it doesn't ship.
- **Not a balance-it-yourself pack.** KubeJS scripts make load-bearing changes to recipes and spawn rules. The pack defines a single intended progression and enforces it; a player who wants a different balance should fork the pack rather than fight the configs.
- **Not a Java mod's home.** Sky Frogs ships only KubeJS, configs, datapack overrides, and the FTB Quests book. If a feature would require Java code, it goes upstream into Productive Frogs.

## Target Audience

- Players who like Productive Bees / Sky Bees Reborn and want a fresh take on the genre.
- Players who like skyblock challenges with a strong narrative arc and progression gates.
- Modpack authors using Sky Frogs as a reference for building Productive-Frogs-centric packs.

## Success Criteria for v0.1

1. A new player can install the pack from Modrinth, create a world, and see a 3×3 dirt island with a single tree.
2. By following the questbook, they can produce their first Iron Froglight within ~2 hours of play.
3. KubeJS-disabled mining shortcuts (laser drill, mining lens) are absent from JEI or tooltipped as DISABLED.
4. The pack loads cleanly on both Modrinth and CurseForge launchers with no error toasts.
5. All six frog tiers are reachable through quests, even if late-tier balance is rough.

## Success Criteria for v1.0

1. ~750 quests across ~22 chapters (parity with Sky Bees Reborn).
2. All six PF categories have at least 5 slime variants each, including 2+ cross-mod variants.
3. Endgame creative item is reachable through pure frog-farming with no exploit shortcut.
4. CurseForge and Modrinth pages both live, with stable release cadence.

## Open design questions

See [`backlog.md`](./backlog.md). Highlights:

- How do we handle the absence of Slime Milker automation in Productive Frogs V1?
- Do we ship our own custom slime species or rely on PF's six parent species?
- Do we include Create / Mekanism / both? (They duplicate roles in places.)
- How do we render Sky Bees Reborn-style branding without confusing players that this is the same pack?
