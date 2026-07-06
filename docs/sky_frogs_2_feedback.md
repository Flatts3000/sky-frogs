# Sky Frogs 2 - player feedback capture

**Status: HOLD, don't build.** This is a captured body of player feedback kept as design input **for a possible Sky Frogs 2**, not a to-do list for the current pack. Nothing here is a committed change. If SF2 happens, this is a primary input; until then it just sits here. Do not file these as GitHub issues against the shipped pack (issues track live state on the current pack; this is future-vision material).

## Source

- **Author:** Eebag (Discord `@Eebag`, id `145697265011523584`), a player who offered to give more feedback / clarification.
- **Playtest basis:** majority of the run on **v1.4.1 / MC 1.21.1**.
- **Credibility signal:** says he wrote the same kind of document for the **Star Technology** pack in its infancy and watched it grow; genuinely wants Productive Frogs / Sky Frogs to succeed ("all love from another frog lover"). Had considered making a Productive-Frogs-style mod himself (started as a Ribbits expansion). Framed everything as "this pack is your personal vision, deny anything that doesn't fit."
- **Original file:** `Sky Frogs Suggestions.pdf` (maintainer's local Downloads, received 2026-07-05).

## The core thesis (the one that matters)

The pack collapses to a single loop and gives **no reason to stay in the world**: get past basic Ex Nihilo, AFK for the first slime, grow the first frogs/slimes, breed-chain them until you need a second frog type or the Dissolution Chamber, breed-chain to endgame, set up a few frogs, AFK. Most of the run is the breeding chain; the end is just waiting. He started building a base to house his frogs and stopped because there was nothing to stay for.

His single biggest request: **more gates and reasons to expand horizontally**, instead of blitzing one vertical breed chain with the same minimal infrastructure the whole way (he ran "a room with water and a diamond barrel for 90% of the run").

He hit **almost no bugs** - a few random frog deaths (attributed to the wall/drowning bugs, already patched). Called out the churn/milker textures and quest descriptions as needing work (both since addressed - see below).

## Pack suggestions (player's own table, preserved)

| Suggestion | Reasoning |
|---|---|
| Revamp of early game | No sieving, but the "twerk + tree" combo feels off; move toward something more immediately frog-related. Cites Project Sacrifice's early game. |
| Change to early cave slimes | Making a mini mob farm and waiting for the first slime feels jank; the quest book implies a milk + barrel slime route that isn't the actual path. |
| Make the pack peaceful, or a reason not to be | No real need to be off peaceful for the vast majority of the run. The upcoming 'predator' frogs may moot this, but it stands for now. |
| Way to obtain dripstone without Villagers | Tried the Functional Storage Dripping Upgrade but a basic vanilla dripstone block is nearly impossible to get. Blackstone has the same problem. |
| Hide unnecessary items in JEI | A lot of Ex Deorum items/crafting pages show even when unobtainable. |
| Gate frog tiers | You go from first breed to endgame with little infrastructure. If reaching Bog or Infernal *swapped the process* to something needing infrastructure, it would force base/production expansion. Needing the Dissolution Chamber is a start, but you get a free wind generator and never expand power. |
| Change to frog order / craft things earlier | Too many materials too fast; things you'd want are gated too late, forcing you to blitz the tree. Glowstone/pearls are needed for recipes that would make sense earlier (magnet/void upgrades, elevators, ender chests, feral flare lanterns, Modular Routers upgrades). Likes gating Refined Storage, but didn't need it by the time he got it. |
| Expansion / need to use potion froglights | Great mechanic; would be nice to make it necessary for a one-off craft or something useful. |
| Consistency in quest requirements | Some quests require froglights, others take the slime; feels inconsistent. (May be changed in the newer version he hadn't played.) |
| Expansion of Princess's Kiss | Loves it, wants it more useful. The dragon fight feels out of place. |
| Upgrade paths for different machines | Milker/spawnery/churn/terrarium are just a step between things with no gameplay but waiting. Slow them at first, or make them long with new types; add a powered version or byproduct extraction that leads to new frog types. |
| Sweet slime is a panacea | One item for making slimes, breeding frogs, and the base for all catalysts. Split it so catalysts gate better - maybe different slimes drop different items needed for catalysts or new frog types. |
| Better resource production | No good sweet-slime source beyond slaughtering random slimes and growing sugar cane. Add a dedicated slime+sugar path - a "sweet frog," or change most slime drops off plain slime balls. |
| Change to Extended Crafting | Vanilla Extended Crafting is tedious and useless without changes. Maybe frogs crafted with different tiers, or gate QoL items (jetpack, botany, etc.) behind it. |
| More lateral quests or mods | You go straight from breed-chain start to endgame with little friction. Add side stops/distractions - quests pointing at Mob Grinding Utils, Powah, jetpacks. |
| Power | Mekanism and Powah are in the pack but there's no need for power production. |
| Frog Dimension | Usually dislikes generic custom dimensions, but sees potential for a swampy place with new frog types and blocks. Large in scope. |
| Magic frogs? | A magic chain of frogs to breed - Malum (corrupted frogs) or Spectrum (colored frogs) - for fun challenges and QoL. Disregard if magic isn't wanted. |

## Personal suggestions (mod-list + wishlist)

| Suggestion | Reasoning |
|---|---|
| AE2 | Keep **either RS or AE2, not both** - too much scope for a small pack. Personally prefers AE2. |
| Hotkey cleanup | Deconflict keybinds at the start. |
| Too many / not enough decoration mods | Chisel + Chisel Reborn + Rechiseled + Chipped + Macaw's suite + Connected Glass + Glassential is a lot. Prefers a more limited palette per material ("width over depth"). Would add **Xtones** (covers a different style). |
| Need for food mods | Farmer's Delight, Cooking for Blockheads, Mama's Herb & Harvest, Spice of Life all feel unnecessary without a hunger/health need. Boss fights and Apotheosis feel like they're in the pack without much reason. |
| Shaders | Include one if it doesn't cause issues. |
| Endgame revamp | Likes the quantum-compressor/singularity endgame as a concept, but not as a pure AFK game. Idea: a frog shrine with each maxed type on lilypads around a pedestal, sacrifice the Ultimate Singularity for "ultimate frog dominance." |
| Frog sounds and types | Wants more frogs - different models, deeper croaks, mating noises, horned infernal frogs, small ones. |

## Already addressed since v1.4.1 (as of capture, 2026-07-05)

Filter these out when using this doc - they were live when he played but are fixed now:

- **Random frog deaths** (wall / drowning) - patched upstream: PF **1.24.4** (tadpole wall-suffocation) and **1.24.5** (Resource Frogs/tadpoles drowning).
- **Quest descriptions need help** - the **v1.4.2 + v1.4.3** editorial rewrite covered the whole book.
- **Froglight-vs-slime quest inconsistency** - largely deliberate: per-tier resource quests check the variant **Froglight** on purpose (the froglight-check law), with the iron-ingot quest as the intentional exception. Worth re-checking his specific cases, but it's mostly by-design, not a bug.
- **Churn/milker textures** - PF **1.24.6 "Fresh Coat"** refreshed bucket/Slime Milk art; the churn/milker block textures may still be a candidate.

## How to use this for SF2

Treat the **core thesis** (vertical AFK breed-chain, no reason to stay, wants horizontal gates) as the headline design problem, not the individual tickets. Most of the table entries are instances of it: unused power/food/combat mods, passive machines, sweet-slime-as-panacea, too-fast pacing, AFK endgame. The individual mod-list opinions (RS-or-AE2, decoration trimming, Xtones) are cheap and worth revisiting at SF2 scoping. The big-scope wishes (Frog Dimension, magic frogs, new models/sounds) are content-team decisions.
