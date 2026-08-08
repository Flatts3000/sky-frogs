# Sky Frogs 2: settled decisions

**Status: live decision log for the MC 26.x sequel.** Everything here is decided and may be built against. Contrast with [`sky_frogs_2_feedback.md`](./sky_frogs_2_feedback.md) (one player's input, held) and [`sky_frogs_1_retrospective.md`](./sky_frogs_1_retrospective.md) (the evidence base). When a decision here supersedes something in those, this file wins.

Target: **Minecraft 26.1.2 / Productive Frogs 2.x.** All source references below were verified against `productive-frogs@main` at `mod_version=2.0.0-alpha.4` on 2026-08-08.

---

## D-1: Slime Milk and Mob Slurry never run dry

**Decided 2026-08-08.**

Milk and slurry sources spawn indefinitely. The **Bountiful** (`count`) and **Endless** (`infinite`) catalysts are disabled in the pack. **Rapid** (`speed`) and **Teeming** (`quantity`) stay.

The mod keeps all four catalysts and the depletion system implemented and config-gated, so other packs and other lines can still use them. This is a pack-configuration decision, not a mod amputation.

### Why

The whole count line exists to manage a burden the player should not have. In SF1 the sequence was: milk runs dry, so you re-milk slimes by hand, so you want the Bountiful catalyst, so you want the Endless catalyst, and the moment you have Endless the entire mechanic is over. Everything built to serve it becomes dead weight.

The retrospective calls this finding 3, and it is the single most-repeated structural complaint in the corpus. Three unrelated players reached it independently. Hunyol, 2026-07-28:

> almost every quest that introduces a mechanic/machine from the progressive frogs book opens up *after* they're no longer relevant. Slime churn to mass produce slime milk? Opens up after you can make endless catalysts.

The Endless Catalyst sits at the Geode diamond gate, which is early. So roughly two thirds of SF1 was played with the mechanic already invalidated, while the pack kept introducing appliances that answered it.

Making permanence the baseline deletes the burden and the catalyst that trivialises it in one move, and it removes a whole class of "why does my farm not work" support traffic (a placed source silently draining is indistinguishable from a spawn failure, which is finding 1's problem wearing a different hat).

### How it lands

**No mod work required.** The lever already exists and shipped. Pack config only:

```toml
[slime_milk]
    # Sources spawn indefinitely. PF's own comment on this key:
    # "better for creative play or packs that want low-friction production."
    depletionEnabled = false

[slime_milk_catalysts]
    count = false       # Bountiful: nothing left to extend
    infinite = false    # Endless: this is now the baseline
    # speed (Rapid) and quantity (Teeming) stay at their defaults
```

Three things make this clean rather than a hack:

- `PFConfig.DEPLETION_ENABLED` is a real first-class flag, read by `SlimeMilkSourceBlockEntity`, `SprinklerBlockEntity`, `SlimeChurnBlockEntity`, `MimicMilkSourceBlock` and the Jade plugin. Turning it off is a supported mode, not an edge case.
- **Mob slurry is covered by the same flag.** There is no placed slurry source block; slurry only exists through the Mob Slurry Basin, and `MobSlurryBasinBlockEntity` inherits its depletion check from `AbstractBasinBlockEntity`, which reads `DEPLETION_ENABLED`. One key covers both. `depletionCount` becomes irrelevant.
- Per-catalyst disables already exist (PF #201). A disabled catalyst is "uncraftable, hidden from JEI + the creative tab, and inert if dropped in," so Bountiful and Endless leave no ghost recipes behind, which was a recurring SF1 annoyance in its own right.

### Consequences to design around

Not objections. These are things that change and need a decision of their own.

- **The Slime Milk Basin loses its stated purpose.** Its selling point is literally the depletion behaviour: *"Unlike a placed source it stays put when it runs dry, so you can pipe milk into it and leave it."* Nothing runs dry now. It retains two real jobs (it contains the milk, so frogs cannot suffocate standing in a source, and it is waterloggable and pipeable), so it needs re-pitching rather than cutting.
- **The Slime Churn is dead on arrival.** It produces slime buckets on the milk budget. With a permanent source you can just place milk. It was already judged obsolete in SF1 (PF #234); now it is obsolete from minute one. Needs a new job or it should not be quested.
- **The Geode diamond gate loses its reward branch.** In SF1 the catalyst chain hung off the diamond capstone. Rapid and Teeming survive and can still hang there, but the branch is much thinner. Tier 2 needs something else.
- **Sprinklers never need refilling.** Terrarium plumbing simplifies. Probably good, worth checking it does not make the Terrarium even more skippable than finding 3 already says it is.
- **The entity-throughput dial survives.** Teeming raises slimes per spawn, which is the axis that raises standing entity count, and that is the retrospective's finding 2 tax. Keeping it is the deliberate call here; it means SF2 does not fully close finding 2 by this decision alone and the entity-budget question stays open on its own merits.
- **SF1's Teeming recipe override still applies.** The pack rewrote the Quantity catalyst recipe from glowstone to redstone because glowstone is Infernal-gated. Teeming survives, so that override (or a replacement gate) carries forward.

---

## D-2: Cave Slimes do not spawn in a dark room

**Decided 2026-08-08.**

The pack does not add Cave Slime to natural spawning. Tier 0 gets the player their first slimes some other way. The replacement is **not yet designed**.

### Why

This is retrospective finding 1, the biggest single failure point in SF1. 34 distinct people reported spawn trouble, it was the number one topic in support, and the rate roughly doubled once the mainstream audience arrived. The dark room sits on vanilla hostile spawning, whose every failure condition is invisible to the player: the 24-block rule, light level, world-spawn protection radius, the hostile mob cap (shared with every other player on a server), peaceful mode, and the fact that slimes will not spawn in blocks adjacent to walls.

It cost real players. Gaymer Mike: *"I really want to like this modpack, but i cant help but dislike it, im really stuck at this cave slime spawn room quest."* And the people who bounced here mostly left no message at all.

### What the dark room actually bootstraps

Worth being precise, because it is more than "the first slime." In SF1 the dark room is the root of the entire Tier 0 economy and it feeds two separate lines:

1. **Slime balls.** The Spawnery is *"fueled by slime balls (one ball per bottle)"* plus a species primer (this pack overrides Cave's primer to cobblestone, since PF's default is an iron ingot and iron is frog-gated here). No slime balls means no bottled frogspawn means no frogs at all. Slime balls are also the base of Sweetslime, which is the breeding food.
2. **The first slime entity**, which you bucket, run through the Milker, and turn into the first Slime Milk.

So removing the dark room removes the frog bootstrap and the milk bootstrap at once. Any replacement has to serve both.

### D-1 makes this much smaller than it looks

The two decisions interlock, and the interaction is the useful part.

Under permanent milk, **one seed closes the loop forever**:

```
one Cave Slime  ->  bucket  ->  Milker  ->  Cave Slime Milk
                                              |
                                    placed, never depletes
                                              |
                            permanent Cave Slime source
                                        /            \
                          slime balls (killed)    food for frogs
                                       |
                                   Spawnery
                                       |
                            bottled Cave frogspawn -> frogs
```

Resource Slimes drop slime balls when a player kills them, and a frog eating the wrong slime also yields slime balls. So the replacement mechanic does not need to be a sustained spawner, a farm, or anything that runs over time. **It needs to hand over exactly one slime, or one bucket of milk, exactly once.** In SF1 that was impossible to make a one-time grant, because the source drained and you would strand the player; D-1 removes that risk.

That reframes the design problem from "replace the dark room" to "pick a good one-time seed," which is a far easier problem and one with no ongoing entity, spawn-rule or mob-cap surface at all.

### Constraints the replacement must satisfy

Derived from the retrospective, non-negotiable:

- **Legible.** The player can tell why it is or is not working, without a diagnostic mod.
- **Independent of vanilla spawning.** No light level, no player distance, no mob cap, no difficulty setting, no world-spawn protection radius, no peaceful check.
- **Identical in singleplayer and on a shared server.** No commons problem, nothing another player can consume.
- **Reachable from the starter island with no prior resources**, and not circular: it cannot require slime balls, iron, or anything downstream of frogs.
- **Recoverable.** If the player destroys their only seed, there is a defined way back. SF1's emergency-items quest is the existing pattern and it was used (players threw away lava buckets and asked for exactly this).
- **Teaches the loop.** The first ten minutes should introduce milk, the Milker and frogs, not delay them.

### Resolved

The seed is settled in **D-3** below: slime balls come off the Builders' Sieve, and SF1's existing `iron_slime_bucket.js` recipe turns them into the first slime. Wild slime spawning is off entirely; the pack adds nothing back to natural spawning.

---

## D-3: Slime balls come from sieving dirt

**Decided 2026-08-08.** Resolves the open item in D-2.

The Builders' Sieve gains a **slime ball** drop on the dirt lane. That is the whole change. Wild Cave Slime spawning is deleted (`add_cave_slime_island.json` goes; the pack adds nothing back to natural spawning).

### Why this is smaller than it looks

Tracing SF1's actual Tier 0 turned up something useful: **the dark room's only unique output was slime balls.** Everything downstream is already crafted rather than spawned.

`iron_slime_bucket.js` already conjures the first slime straight into a bucket, from a Cave frog egg, slime balls, string, bone meal and an empty bucket. The frog egg is a Welcome-chapter reward, the bucket comes off the Slime Milker quest, bone meal comes off a composter. Only the slime balls came from the dark room. So the existing bootstrap recipe **is** the seed; it just needed a non-spawning input.

That means D-2 costs one deleted biome modifier and one added sieve line, not a redesign.

### The opening, end to end, with no vanilla spawning anywhere

```
starter tree
  -> Crook on leaves        -> Silkworm
  -> infest tree, harvest   -> String
  -> String Mesh + Oak Sieve
  -> sieve DIRT             -> Slime Ball          <- the change
  -> + Cave frog egg (Welcome reward)
    + empty bucket (Milker quest)
    + bone meal (composter)
  -> Iron Slime in a Bucket (existing recipe, unchanged)
  -> Slime Milker           -> Iron Slime Milk
  -> place it               -> never runs dry (D-1)
  -> Iron Slimes forever    -> frogs eat them -> Iron Froglights
                            -> killed for more slime balls
```

Dirt is composter-cheap at Tier 0, so the input is renewable from the starter tree. Nothing in this chain reads light level, player distance, mob cap, difficulty or spawn protection, and it behaves identically on a shared server.

### The silkworm is now load-bearing, and it is 1 in 100

The one thing to get right. Ex Deorum's silkworm is *"a 1 in 100 chance to drop from leaves harvested with a Crook."* In SF1 nobody noticed, because spiders in the dark room gave string. Remove the dark room and the string mesh becomes the real gate, at a worse drop rate than anything we are adding.

**The Welcome chapter hands out a Silkworm (or the String Mesh outright).** This is the established pattern, not a special case: the chapter already grants saplings, the second water source, lava for the cobble generator, food, and the empty bucket. One more line removes a 1-in-100 wall from minute one. The crook and the silkworm stay craftable so the path is still discoverable and repeatable.

### Drop rate

Proposed **0.25 on dirt, string mesh**, well above the lane's existing 0.03 to 0.125.

It should be generous, because it is a gate rather than an economy: within minutes of the first slime the player is killing slimes for slime balls and the sieve stops mattering. At 0.25 the expected wait is about four sieve actions and 95% of players are through in eleven. Tuning it down later is cheap; a slow gate at minute one is exactly the failure the retrospective is about.

Sieved slime balls bypass nothing. Slime balls were already unlimited in SF1 via the dark room, and the frog spine is froglights, not slime balls.

### Accepted tradeoffs

Both were weighed and taken deliberately.

- **RNG at minute one** is the friction retrospective finding 1 is about. The mitigation is the drop rate and the granted silkworm; the recovery story is genuinely better than the alternatives, since "sieve again" needs no cooldown quest and cannot be lost.
- **The sieve is no longer decoration-only.** SF1 scoped the Builders' Sieve to cosmetic and building flora on purpose (`builder_sieve.js` header, `anti.js` pillar 1). That scoping is hereby amended, not violated: the lane now carries exactly one progression item, the Tier 0 bootstrap, and nothing else. Ores, gems and mob drops stay off it.

### To build

1. `builder_sieve.js`: add `['minecraft:slime_ball', 0.25]` to the dirt lane. Update the file header, which currently promises no progression materials.
2. Delete `pack/kubejs/data/skyfrogs/neoforge/biome_modifier/add_cave_slime_island.json`.
3. Welcome chapter: add the Silkworm (or String Mesh) reward, and a quest that teaches crook to silkworm to string.
4. `anti.js`: update the pillar 1 comment, which states Tier 0 is a dark-room slime farm and not sieving. It is now the opposite.
5. Quest text: every mention of the dark room goes. SF1 had a whole `A Dark Room` quest (PF #198 was about it under-explaining the 24-block rule); it is deleted, not reworded.

---

## Open questions this log has not answered

Carried from the retrospective's implications list, still undecided:

1. Is the resource loop still entity-bound? D-1 helps, keeping Teeming does not. Finding 2 stays open.
2. Where does pack length come from, now that SF1's length was mostly the breeding timer?
3. Does stat breeding survive, and in what form? The maintainer's own poll went 7 of 13 for "No, its tedious," and D-1 makes frog stats a more load-bearing throughput lever, not less.
4. What does each tier verb gate, given storage and power were both optional in SF1?
5. Is multiplayer supported or tolerated?

## Blockers found while scoping, not yet decided

- **Skyblock Builder has no 26.x build.** Newest is 1.21.1 (21.1.34, 2026-08-06). Ex Deorum (4.0 for 26.1.2, 5.x for 26.2), FTB Quests (26.1.2.3) and KubeJS (8.0.4, 26.1.2 beta) have all made the jump; Skyblock Builder has not. This is the same mod that forced SF1's rollback from 1.21.11 to 1.21.1, and it is the one dependency with no substitute in the current list. The fallback is a datapack void world preset plus a structure-placed starter island, which drops the dependency but also drops `/skyblock create` team islands. Needs a decision.
- **26.1.2 is the only version the whole stack shares.** KubeJS and FTB Quests have nothing for 26.2, and PF 2.x targets 26.1.2. So 26.2 is off the table until that changes, whatever happens with worldgen.
