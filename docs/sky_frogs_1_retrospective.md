# Sky Frogs 1: what the Discord taught us

**Status: input for Sky Frogs 2 (MC 26.x).** This is a retrospective on the shipped pack, distilled from the community Discord. It is not a design document and nothing in it is a decision. It is the evidence base the SF2 design should argue with.

Companion docs: [`sky_frogs_2_feedback.md`](./sky_frogs_2_feedback.md) is one player's structured end-of-run writeup (Eebag) and stands on its own. This document is the other 430 people. [`known_issues.md`](./known_issues.md) holds the bug ledger; this holds the design lessons.

---

## Method

Every readable channel of the community Discord was exported in full and read: **4,885 messages across 19 channels**, 2026-06-06 (server opened) to 2026-08-07. The tool is [`tools/export_discord.py`](../../sky-frogs-community/tools/export_discord.py) in the community repo (paginating full-history exporter, incremental on re-run; output is gitignored).

Excluded from the analysis: `#github-feed` (1,328 bot embeds, redundant with GitHub), `#changelog` and `#announcements` (bot release posts), and the Trashlands / Ribbit channels (different packs). That leaves **3,216 human messages from 430 distinct participants** across `#sky-frogs-general`, `#sky-frogs-support`, `#suggestions`, `#sky-frogs-showcase` and `#general`.

Two things to hold in mind when reading counts below:

- **The audience changed halfway.** Server joins ran in ones and twos until 2026-07-19, then jumped to 8 to 28 per day for the rest of the window, on the back of the CyberFuel Studios series (from 2026-06-29) and the CaptainSparklez stream (2026-07-18). Roughly 250 of the 430 participants arrived in that second wave. Everything the pack was tuned against before mid-July came from skyblock veterans (Dergib, dlswimmer, RayRayZCB, Hullah, Gargish). The mainstream audience arrived after the design was frozen.
- **Silence is not approval.** People who bounce do not post. One of the few who narrated it is worth quoting in full because he is the visible part of an invisible number, below in finding 1.

---

## The findings

Ranked by weight of evidence, not by how hard they are to fix.

### 1. The Tier 0 spawn bootstrap is the single biggest failure point in the pack

**34 distinct people** posted messages about mobs or slimes failing to spawn (158 spawn-related messages overall, 57 of them trouble reports). It is the number one topic in `#sky-frogs-support` by a wide margin, and it got *worse* per-message after the streamer wave: 15 people over the first 1,794 channel messages, 20 people over the next 1,149.

The pack's first real task is "build a dark room and wait." That task sits on vanilla hostile spawning, which is the least legible system in Minecraft. Every one of its failure conditions is invisible:

- the 24-block player distance rule
- the light level, including light the player cannot see
- the world spawn protection radius (Skyblock Builder's, which the pack had to override to 0; see `known_issues.md`)
- the hostile mob cap, which on a server is **shared with every other player**
- being in peaceful without realising it (this happened repeatedly, including to experienced players)
- and one the maintainer only discovered on 2026-07-24: **slimes do not spawn in the blocks adjacent to walls**, so a 3x3 room has exactly one valid spawn column

The maintainer's own read, 2026-07-22: *"This is a problem that a lot of people have and IDK if its an actual issue or not. One thing I can say is that I wish it were more obvious why things aren't spawning."*

The response was to **write a diagnostic mod**. Spawn Detective exists because a core mechanic is unreadable. That is worth sitting with: the pack shipped a tool to explain a mechanic rather than replacing the mechanic with a legible one. And the tool then inherited the same problem, because it only covers *natural* spawns and not milk spawns, which is itself a recurring confusion (Korkoa, 2026-07-25; Zeroshion, 2026-07-24).

The cost is real. Gaymer Mike, 2026-07-27:

> I really want to like this modpack, but i cant help but dislike it, im really stuck at this cave slime spawn room quest to get slime balls [...] there is a world spawn limit cap to 140, its sitting at 156 mobs now in the world and im the only one on the server [...] so how am i suppose to go further now?

And Tacos16x20, who spent an evening on it across two nights and left:

> ill just go play more elden ring, i cant deal with this lol [...] its something on my computer surely, ill just watch sparklez play it

**For SF2:** the first ten minutes cannot depend on vanilla hostile spawning. This is the highest-leverage change available, and it is upstream of finding 2.

### 2. Entity-based resource generation is the pack's structural tax

Everything downstream of Tier 0 is also entities: slimes spawn, frogs eat them, froglights drop. Players worked this out on their own and named it.

Hunyol, 2026-07-28, on why the game freezes: *"one of the downsides of the entire resource generation being based on entities."* Sam Gomez, 2026-07-27, on why the shared server broke: *"It's what happens when the whole mod is built around mobs."*

It shows up as four separate symptoms that all have one cause:

- **Lag.** 17 distinct people on lag, FPS, TPS, freezing or stuttering. Crown Of Thorns fought it for a week across peaceful and non-peaceful, more RAM, and different launchers, and never fixed it.
- **Mob cap contention.** 8 people. In singleplayer it throttles your own farms (Anubis: amethyst and lapis stopped spawning until other pens were switched off). On a shared server it is a commons problem with no fix available to the player: other people's chunk-loaded spawn rooms consume the cap and you simply cannot progress.
- **Self-throttling farms.** The proximity spawn cap inside Slime Milk is correct engineering and completely opaque in play. Korkoa built five identical chambers and one silently refused to work.
- **Design pressure everywhere else.** "Cull the slimes as fast as possible" became the pack's actual optimisation target. Angel asked for it directly, 2026-07-04: *"terrarium should be a multiblock that doesnt use entities directly [...] TPS and FPS friendly."*

**For SF2:** either the resource loop stops being entity-count-bound, or entity budget becomes a first-class, visible resource the player manages on purpose. The Virtual Terrarium (PF 1.25.0) is the shape of the first answer and it arrived in the last month of the pack's life.

### 3. Every appliance arrives after the problem it solves is already solved

This is the sharpest single observation anyone made about the pack, and three unrelated players reached it independently.

Hunyol, 2026-07-28:

> almost every quest that introduces a mechanic/machine from the progressive frogs book opens up *after* they're no longer relevant. Slime churn to mass produce slime milk? Opens up after you can make endless catalysts. Terrarium and sweetslime lily pads? By that point youre already able to keep a frog stationary while feeding it tons of slimes.

Korkoa, 2026-08-05, hitting the Terrarium chapter: *"It feels unnecessary. I have habitats for each frog/slime variant I've needed, fully upgraded slime milk pools that are infinite, item vacuums, and a central storage system. It just kind of feels redundant?"* Hullah, on the Incubator: *"I never ended up using the incubator because I was already at 10/10/10 for about all but one of my frogs."* Sam Gomez on the Casting Mold: *"The casting mold is so useless."* Hunyol on the Crucible: *"i ended up just abandoning it."*

The Endless Catalyst at the Geode diamond gate is the specific culprit. It solves milk permanence so completely that the Churn (Bog), the Terrarium (Infernal), the lily pad, the Basin and the Milker upgrades are all answers to a question the player stopped asking two tiers earlier. This was filed as [#234] during the pack's life and never structurally addressed.

The same shape hits the boss altars: the altars exist so you do not have to kill the dragon seven times, but **the altar quests unlock after the catalyst quests that make you kill the dragon seven times** (Hunyol, 2026-07-28). Players hit the grind, complained, and only afterwards found the thing built to spare them. rtggaming, on finishing: *"Dragon fights were tedious and not fun killing the dragon 7 times without any methode to oneshot."* Hullah: *"I didn't know about the altars until afterwards."*

**For SF2:** a mechanic must ship on the tier where its problem is live. If the fix arrives after the workaround, the mechanic is decoration.

### 4. Breeding is the longest activity in the pack and the maintainer's own poll says it is not fun

On 2026-06-13 the maintainer ran a poll: **"Is breeding frogs fun?"** Result: **7 of 13 votes for "No, its tedious."** That poll is the single hardest data point in this document, and the mechanic shipped unchanged.

46 messages from 22 distinct people are about the 10/10/10 grind. It is also, by player report, the pack's real length: Drewski, 2026-08-07, *"Breeding has felt like the longest part of the pack."* Incline agreed in the same conversation: *"breeding frogs is probably the only thing that actually takes time and effort."*

The community split on it, and the split is informative. The people who liked it liked it *as a breeding minigame* with prior art they enjoyed (OldManLeroy: *"Your whole mod centers around the frogs being productive....so shouldn't it be a challenge to actually get them to be productive?"*; flatts: *"I really liked breeding crops in Agricraft"*). The people who disliked it disliked the **waiting**: a 3-minute frogspawn, 3-minute tadpole, 5-minute cooldown loop with a per-stat improvement roll, run 15+ generations. Azana, 2026-07-26: *"I am often finding myself just waiting on the 6 minutes of frog breeding to continue progressing."*

Two aggravating factors made it worse than designed:

- **No accelerant exists.** Nothing in the pack speeds breeding. The answers people got were "breed more pairs in parallel" or "edit the config," and several took the config (which Sam Gomez then called cheating, correctly reading it as a design escape hatch).
- **Losses are unrecoverable and arbitrary.** Lightning killed a sealed pen of 10/10/10 cave frogs (UnIimitedVortex, 2026-07-23). Tadpoles suffocated in walls, frogs drowned, frogs suffocated in Slime Milk. Each of those was individually patched upstream during the pack's life, but the shape stayed: hours of investment destroyed by something the player could not have anticipated.

**For SF2:** decide deliberately whether stat breeding is a *feature* or a *timer*. If it stays, it needs an accelerant, a safety net, and a reason to engage beyond a number going up. Note the maintainer's own instinct from 2026-06-09, which the rest of the pack honours and breeding does not: *"I want it to be hard for just a little while until you get something to make it easy."*

### 5. Progression collapses after Bog

Incline, 2026-08-07, after finishing most of the pack:

> im going to be 100% honest... the pack progression is a little wack [...] the problem more honestly isnt even how the pack progression works its the speed of the modpack past the Bog Tier, from tide and onward you can just speed run everything

> It stops becoming a necessity and starts being a way to quickly farm infinite resources

The tier verbs were the pack's anti-repetition design (each tier layers one new verb: crafting, automation, tools, mobility, storage, singularities). By player report, the later verbs do not bind:

- **Storage (Infernal / Refined Storage).** Incline: *"by the time you get to refined crafting in the infernal tier its kind of like a sidequest [...] a couple netherite barrels will just completely bypass the need for a storage system because there just isnt enough stuff in the pack for it to really matter."* The pack does not have enough distinct items to need a network.
- **Power (Geode / Mekanism, plus Powah).** Nothing in the pack demands meaningful power. Dergib: *"unless flatts adds something that requires lots of power you are really just crafting powah reactor blocks for a quest."* Eebag reached the same conclusion. Hullah beat the pack on two upgraded Powah magmators. OshLeWater built the Mekanism quest machines and then skipped to Powah.
- **Mobility (Tide / jetpacks).** Works, and is load-bearing for the Nether crossing, but it also removes the reason for the Void-tier elevators and similar QoL that arrives later (Incline: *"you will get jetpacks before you can consistently get ender pearls so might as well just use an open layout so you can just fly to everything"*).

Meanwhile the **Cave tier is overloaded**. Incline: *"now why are cave frogs so broken, they are hogging so many resources."* Roughly 20 of the pack's resources hang off one species, and OldManLeroy's spreadsheet of the whole roster reads 7 cave / 6 geode / 14 bog / 9 tide / 12 infernal / 9 void.

**For SF2:** Eebag's core thesis and this finding are the same finding, arrived at from opposite ends. The pack is one vertical breed-chain with a flat infrastructure requirement, and the tier verbs are decoration on top of it rather than gates through it.

### 6. The pack is finished in about three days, and the audience noticed

Dergib had every quest done on 2026-06-11, five days after the Discord opened: *"3-4 days. but I am counting breeding 10/10/10 and the last quest line as endgame."* Hullah's completion post reports **2.98 days played**. The very first suggestion thread on the server, 2026-06-06, was someone asking for it to be longer: *"it should be a lot longer to finish even if u have exp with sky block."*

Reported completions cluster tight: Dr (2026-06-11), Dergib, rtggaming (06-14), Hullah (06-29), Gargish (07-02), Supposable (07-12), ozuox (07-21), Harthness (07-28), RastoMast (07-30), Jake (08-02), FluffyAdept and Vulu (08-07).

This is not automatically a fault. The pack's stated goal was *"an intro into Productive Frogs [...] I wanted to have a low barrier of entry"* (flatts, 2026-07-06), and by that measure it worked (see finding 10). But the audience that arrived post-CaptainSparklez is a modpack audience, and a modpack audience treats three days as short.

**For SF2:** length must be an explicit target, and it must come from somewhere other than the breeding timer, which is where SF1's length actually came from.

### 7. Froglights are component items, and component items break in third-party mods

**28 messages from 17 distinct people** about Iron Furnaces. The single largest recurring bug in the pack's life, and it is not the pack's bug.

Froglights are one item id carrying a `slime_variant` component. Iron Furnaces is component-blind, which produced three distinct failures: froglights refusing to enter the furnace at all (fixed by restarting the game, which players had to be told individually, over and over, for a month), froglights being converted to the furnace's current variant, and an outright duplication exploit. Filed as [#220] and [#225], reported upstream, never fixed there.

The support cost was enormous and entirely repetitive. The same exchange happens in the transcript at least eight times: player reports it, someone says restart, it works.

This is a general lesson, not an Iron Furnaces one. It is already in the repo memory as a rule: screen mods for component-blind slot handling. SF2 inherits the same item model.

**For SF2:** either the resource item stops being component-keyed (a real item split upstream in Productive Frogs), or every mod that touches item slots gets screened before it ships. The pack chose to ship a known-broken interaction with a popular convenience mod, and paid for it in support all summer.

### 8. Most support load was discoverability, not difficulty

A large share of `#sky-frogs-support` is people unable to find something that exists:

- **The field guide.** Productive Frogs ships a Patchouli book with build previews that project the multiblocks into the world. Players hit the boss altars, could not build them, and did not know the book existed. Wolley: *"im bad at reading and go off of pictures and there arent any."* Harthness, after being told: *"oh yaaa theres a book lol, havent used that once."* Fixed in v1.6.0 by a quest that names it.
- **Mushrooms.** Widely believed impossible. You shear a Bogged. Seeker: *"took me 3 days to remember you can get mushrooms in this pack."*
- **Honey.** Believed impossible. Reachable the whole time. Fixed in v1.6.0.
- **Eggs and chickens.** No signposted passive-mob path. Needed for the End Cake, which is the gate to the End. Hunyol: *"the fact that it never recommends making a passive mob platform early game or give some other way to make eggs is... not ideal."* Still being asked on 2026-08-07, the last day of the corpus.
- **A frog-to-resource index.** Asked for repeatedly in different words ("does anyone have a diagram of which frogs do which slimes?", "how can i get a full list of every resourse each frog produces"). The Completionist census chapter exists and answers this; players did not find it.
- **The catalysts.** Several players nearly quit at the manual-milking stage without knowing infinite milk was two tiers away. OldManLeroy, 2026-06-09: *"tbh I think I'm done. This was really fun up til now but I don't have the mental fortitude to figure out how to automate."* He was told the Endless Catalyst exists and immediately carried on. FloweringWillows asked for exactly this signpost: *"I think putting it in the quest description that this happens later would be perfect."*

**For SF2:** the quest book is the pack's only teaching surface and it teaches the critical path only. Every one of the above is a case where the pack knew something the player did not and had no channel to say it.

### 9. Multiplayer was a second-class citizen

The pack shipped to servers (Benbenlaw's network hosted it from 2026-06-08) and multiplayer surfaced problems singleplayer never does:

- **Shared mob cap.** Finding 1 and 2. There is no player-side fix.
- **Server files were hard to get.** Repeatedly stuck in CurseForge moderation, so the community hand-delivered GitHub release links. Pierce alone did this three times to three different people. At least six separate people asked where server files were.
- **A dedicated server would generate the wrong world**, because the skyblock world type lives in `server.properties` and hosting panels rewrite that file. Fixed in v1.6.0 by making every world type generate the skyblock.
- **Frogs vanished from Slime Milk pens after a server rejoin** ([#362]).
- **Breeding appeared broken on a specific server** for two days across several players, was never fully root-caused, and the working theory landed on server config.
- Sam Gomez's summary to a stuck new player, 2026-07-27: *"The server is cooked, it's best to play offline or host your own."*

**For SF2:** decide up front whether multiplayer is supported or tolerated. If supported, the entity budget question (finding 2) becomes a hard constraint rather than a performance note.

### 10. What actually worked, and must survive the rewrite

The pack has real fans and specific strengths. Do not regress these while fixing the above.

- **The core hook lands instantly.** "Frogs instead of mining" sells itself. StephJ2Fan: *"I love frogs IRL. they are my spirit animal."* Multiple people cited nostalgia for a specific ancestor: Chickens, Bonsai Trees, SkyFactory 4. Incline: *"it reminds me of my favorite modpack that I never finished, sky factory 4."* KBizzle: *"Takes me back to the chickens mod days. My favorite resource mod."*
- **It is a genuinely good first tech pack.** This was an explicit design goal and it is the best feedback the pack received. Crown Of Thorns, 2026-07-28: *"this is one of my first ever technical modpacks and I've been really enjoying it. very much a pack with a low barrier of entry that does a good job guiding me through all the different mods without being too overwhelming. there's been a really good balance between trusting the player to figure it out and handholding at key moments [...] its eased me into mods I'd be too intimidated to pursue getting into on my own."*
- **The showcase culture is strong and self-teaching.** `#sky-frogs-showcase` produced real design evolution: dlswimmer's slime-filter trick (using the filter block so slimes can only spawn on one column) got adopted, then improved by OldManLeroy, then improved again by $lunchoncrack, then copied onward. That is a healthy pack. Compact 1x1 frog pens spread the same way. Build the sequel to keep producing shareable setups.
- **Update cadence bought enormous goodwill.** 20+ releases in the first two weeks. Dergib: *"You keep moving the goal post on me. lol. Seriously tho, this pack started great and just keeps getting better."* bizarr0 and RayRayZCB both thanked the maintainer specifically for shipping suggestions fast.
- **The maintainer is present in the channel**, answering support directly. A meaningful share of the goodwill in this corpus is that.
- **The "hard briefly, then easy" curve is right where it exists.** The Endless Catalyst moment is the pack's best beat: several people described it as the thing that saved their run. The problem in finding 3 is that nothing after it lands as hard, not that it lands too hard.

---

## Cross-cutting observations

Smaller than the findings above, but they recur and they are cheap to get right.

- **Unobtainable content stayed visible.** Apotheosis needs Warden tendrils and the Warden was believed unsummonable; ATM ore recipes ghost in JEI; Ex Deorum items show for things that cannot be made; Iron Furnaces ATM recipes have empty tags; the Midas frog is disabled but its lane is still readable in the guide. Every one of these cost someone an hour. Eebag asked for a JEI hide pass directly.
- **Food and combat mods are unused.** Hullah: *"I never had to craft food with all the given food rewards."* Quest rewards feed you for the whole run, so Farmer's Delight, Cooking for Blockheads, Mama's Herbs and Spice of Life have no job. Eebag flagged the same for Apotheosis and the boss content.
- **The wandering trader is an unintended escape hatch.** RastoMast obtained a Totem of Undying from trades and noted it was rarer than the Ultimate Singularity. Trader trades bypass the closed economy the whole pack is built to enforce.
- **Players want a stats readout.** Asked for in several forms: an item or sign that shows a frog's stats, a full singularity list in the quest book, a resource-to-frog index. All three are "the pack knows, the player cannot see."
- **Quest text errors were caught by players, repeatedly and accurately.** The Ultimate Catalyst contradiction was found independently by Hunyol, Jake and Korkoa. The Experience Singularity book-vs-bottle error, the Take Flight coil ladder, the void slime that does not exist. This community will proofread the pack if given a channel to do it in. All four were fixed, but they were shipped first.
- **`/skyblock create` as folk medicine.** Several people were told to create a fresh island to fix spawn problems, because islands generated thousands of blocks out escape world-spawn protection. That worked, and it means some players never used the starter island the pack designed.

---

## What this implies for Sky Frogs 2

Not decisions. The questions the design should answer, in priority order:

1. **What replaces the dark room?** Tier 0 cannot be vanilla hostile spawning. This is the highest-value change in the document and it unblocks findings 1, 2 and 9 at once.
2. **Is the resource loop still entity-bound?** If yes, entity budget becomes a designed, visible mechanic. If no, most of the lag, mob cap and multiplayer findings evaporate. PF 2.x's Virtual Terrarium and the predator/Apex frog line suggest upstream is already moving.
3. **Where does length come from?** SF1's length was the breeding timer. If breeding stops being the clock, something must replace it, and "more tiers of the same chain" is the thing Eebag explicitly asked not to get.
4. **Does a mechanic ship on the tier where its problem is live?** Adopt this as a rule with teeth. Finding 3 is mostly one scheduling error repeated eight times.
5. **What does each tier verb actually gate?** Storage and power were optional in SF1. A verb the player can skip is a mod in the list, not a tier.
6. **Is multiplayer supported or tolerated?** Answer before the mod list, not after.
7. **How does the pack teach things off the critical path?** The quest book was the only channel and it only carries the main line. PF now ships an extensible Patchouli guide; that is a second channel SF1 barely used.

Two things worth stating plainly because they cut against the grain of the list above:

- **SF1's "low barrier of entry" goal was met**, and it is the pack's best-loved property. Several of the fixes above (longer, more gates, more infrastructure, harder Tier 0) point away from it. That tension is a real design decision for the user to make, not something to resolve by taking every suggestion.
- **The loudest feedback comes from completionists.** Eebag, Hunyol, Incline, Dergib and Hullah between them account for a large fraction of the sharpest critique in this corpus, and all of them finished the pack. The people who bounced at the dark room left roughly no text behind. Weight finding 1 accordingly: it is under-represented in the transcript relative to how many players it cost.

---

## Corpus notes

- Raw export lives outside git at `sky-frogs-community/export/` (gitignored). Re-run `python tools/export_discord.py` in that repo to refresh; it is incremental.
- Edits and deletions are invisible to the export. Quotes are as-exported.
- Message counts in this document were computed over the five human channels listed under Method; `--full` re-export would supersede them.
- Screenshots and videos are referenced in the transcripts as `[attachment]` and were not downloaded for this pass. `read_discord.py --download` can fetch them, but CDN links expire, so it must run against a fresh listing.
