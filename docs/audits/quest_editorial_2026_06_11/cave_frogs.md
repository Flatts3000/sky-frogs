# Audit: cave_frogs ("Cave Frogs" - Tier 1)

Mod(s) referenced: Productive Frogs (productivefrogs-1.20.0.jar), Dark Utilities (darkutils-neoforge-1.21.1-21.1.1.jar), Functional Storage (rewards only). Generated chapter: no.

## Mechanic-claims ledger

| Quest | Claim (paraphrase) | Source checked (jar path / pack override) | Verdict |
|-------|--------------------|-------------------------------------------|---------|
| Beyond Iron | Cave frog handles "copper, gold, coal, lapis, redstone, obsidian" | pack `cave_slime_chain.js` (chain) + variant `category` fields | WRONG (partial) - lapis is a GEODE-chapter resource and obsidian is an INFERNAL-category variant (chamber-only, quested in infernal_frogs). The Cave chapter's actual resources are copper, gold, coal, glow_ink_sac, breeze_rod, redstone. Listing lapis/obsidian as Cave overpromises. -- VERIFY: VERIFIED. PF jar `slime_variant/lapis.json` category="geode", `obsidian.json` category="infernal", `breeze_rod.json` category="cave". cave_slime_chain.js chain = iron->copper->gold->coal->glow_ink_sac->breeze_rod->redstone (lapis explicitly "moved to Geode", obsidian "Infernal-category, chamber-only" per script comment). AFTER edit is correct -- apply. |
| Copper | iron milk -> Copper Slime in a Bucket (4 stone, 3 sweetslime, Cave frogspawn) | `cave_slime_chain.js` step `['iron','copper']`, recipe = 1 prior milk + 4 stone + 3 sweetslime + 1 cave frog_egg | MATCHES |
| Copper | smelt Copper Froglight -> copper ingot | `configurable_froglight_copper_to_copper_ingot.json` (smelting -> minecraft:copper_ingot) | MATCHES |
| Gold | copper milk -> Gold Slime | `cave_slime_chain.js` step `['copper','gold']` | MATCHES |
| Gold | smelt Gold Froglight -> gold | `configurable_froglight_gold_to_gold_ingot.json` (-> minecraft:gold_ingot) | MATCHES |
| Coal | gold milk -> Coal Slime | `cave_slime_chain.js` step `['gold','coal']` | MATCHES |
| Coal | smelt Coal Froglight -> coal | `configurable_froglight_coal_to_coal.json` (-> minecraft:coal) | MATCHES |
| Glow Ink | coal milk -> Glow Ink Sac Slime | `cave_slime_chain.js` step `['coal','glow_ink_sac']` | MATCHES |
| Glow Ink | smelt Glow Ink Sac Froglight -> glow ink sacs | `configurable_froglight_glow_ink_sac_to_glow_ink_sac.json` (-> minecraft:glow_ink_sac) | MATCHES |
| Breeze Rod | Cave frog farms what the Breeze drops (breeze rods), "wind charges and all" | variant `breeze_rod.json` (primer_item minecraft:breeze_rod) + `configurable_froglight_breeze_rod_to_breeze_rod.json` | WRONG (partial) - frog produces the Breeze Rod Froglight, which smelts to a breeze_rod only. It does NOT farm wind charges (those are vanilla-crafted FROM breeze rods). "wind charges and all" is an inaccurate embellishment. -- VERIFY: VERIFIED. PF jar `configurable_froglight_breeze_rod_to_breeze_rod.json` smelts -> minecraft:breeze_rod ONLY; no breeze/wind_charge recipe exists in the PF datapack (grep confirmed single recipe). AFTER edit (cut "wind charges and all", add glow-ink-milk feeder note) is correct -- apply. |
| Redstone | "glow ink milk into a Redstone Slime" | `cave_slime_chain.js` step `['breeze_rod','redstone']` | **WRONG** - the Redstone Slime is crafted from **Breeze Rod** Slime Milk, not glow ink milk. Text predates the breeze_rod chain insertion (PF 1.13.0 / #161) and was never updated. -- VERIFY: VERIFIED. cave_slime_chain.js final chain step is `['breeze_rod','redstone']`: recipe input = `breeze_rod_slime_milk_bucket` (+ 4 stone, 3 sweetslime, cave frog_egg) -> redstone slime_bucket. Glow ink milk feeds breeze_rod, not redstone. AFTER edit (breeze rod milk -> Redstone Slime) is correct -- apply. |
| Redstone | smelt Redstone Froglight -> redstone | `configurable_froglight_redstone_to_redstone.json` (-> minecraft:redstone) | MATCHES |
| Players Only | Mob Filter, golden pickaxe in the center makes the Player variant | `darkutils filter_player.json`: pattern SFS/FIF/SFS, S=c:stones, F=fence_gates, I=golden_pickaxe, result count 4 | MATCHES (center item = golden pickaxe) |
| Players Only | Dark Utilities ships a Slime filter + Hostile/Animal/Undead etc., each built the same way around a different center item | `darkutils` filter recipes (filter_slime uses c:slime_balls center; all share SFS/FIF/SFS frame) | MATCHES |
| Players Only | Player filter lets only you through; seal a frog pen, no ledge-lead needed | `darkutils` lang tooltip.filter_player "A block only players can pass through." | MATCHES |

## Per-quest findings

### Beyond Iron (quest.7CA7E000C0DE0002)
- Disposition: EDIT
- Issues:
  - Factual: lists "lapis ... obsidian" as Cave-frog resources; lapis is Geode-chapter, obsidian is Infernal-category. Overpromises this chapter's scope.
  - Stale reference: `&7(Chapter stub - the per-resource quests land here.)&r` is a leftover dev placeholder; the per-resource quests now exist below it.
- BEFORE:
  quest.7CA7E000C0DE0002.quest_desc: [
  	"You've pulled iron out of a frog. The Cave frog handles everything else the pickaxe used to: copper, gold, coal, lapis, redstone, obsidian - and the modded metals besides."
  	""
  	"&7(Chapter stub - the per-resource quests land here.)&r"
  ]
- AFTER:
  quest.7CA7E000C0DE0002.quest_desc: [
  	"You've pulled iron out of a frog. The Cave frog covers the rest of the pickaxe's old job: copper, gold, coal, glow ink, breeze rods, and redstone."
  	""
  	"Each one is a quest below. Work down the chain - every step threads off the milk from the step before it."
  ]

### Copper (quest.7CA7E000C0DE0005)
- Disposition: CLEAN

### Gold (quest.7CA7E000C0DE0008)
- Disposition: CLEAN

### Players Only (quest.7CA7E000C0DE0020)
- Disposition: CLEAN
- (Accurate against the Dark Utilities recipe and tooltip; warm tone, in scope. The in-game name is "Mob Filter (Player)"; the quest's "Player filter"/"Mob Filter" usage reads fine.)

### Coal (quest.7CA7E000C0DE000B)
- Disposition: EDIT
- Issues:
  - Voice/verbosity: the closing clause repeats the subtitle nearly verbatim - "fuel you can make without a single coal ore in sight" then "fuel without an ore in sight." Trim the duplication.
- BEFORE:
  quest.7CA7E000C0DE000B.quest_desc: [
  	"&6Gold milk&r this time, for a &7Coal Slime&r - fuel you can make without a single coal ore in sight."
  	""
  	"Turn in the &bCoal Froglight&r the frog leaves you, then smelt it for coal - fuel without an ore in sight."
  ]
- AFTER:
  quest.7CA7E000C0DE000B.quest_desc: [
  	"&6Gold milk&r this time, for a &7Coal Slime&r - fuel without a single coal ore in sight."
  	""
  	"Turn in the &bCoal Froglight&r the frog leaves you, then smelt it for coal."
  ]

### Glow Ink (quest.7CA7E000C0DE0023)
- Disposition: CLEAN
- (Threading, smelt result, and "endgame will come asking" hook all check out. "the deep caves' glow squids, distilled" is flavor, not a mechanic claim.)

### Breeze Rod (quest.7CA7E000C0DE0026)
- Disposition: EDIT
- Issues:
  - Factual: "wind charges and all" implies the frog farms wind charges; it only produces the Breeze Rod Froglight (smelts to a breeze rod). Cut the inaccurate clause.
  - Consistency (minor): unlike its siblings, this quest never names the milk it threads off (glow ink milk). Optional to add, but it leaves the chain step implicit.
- BEFORE:
  quest.7CA7E000C0DE0026.quest_desc: [
  	"A &fbreeze rod&r without a trial chamber in sight - the Cave frog farms what the Breeze drops, wind charges and all."
  	""
  	"Turn in the &bBreeze Rod Froglight&r."
  ]
- AFTER:
  quest.7CA7E000C0DE0026.quest_desc: [
  	"A &fbreeze rod&r without a trial chamber in sight - the Cave frog farms what the Breeze drops."
  	""
  	"&bGlow ink milk&r makes the Breeze Rod Slime. Run the loop and turn in the &bBreeze Rod Froglight&r."
  ]

### Redstone (quest.7CA7E000C0DE000E)
- Disposition: EDIT
- Issues:
  - Factual (HIGHEST SEVERITY): text says "glow ink milk into a Redstone Slime." The Redstone Slime is crafted from **Breeze Rod** Slime Milk per `cave_slime_chain.js` (`['breeze_rod','redstone']`). Stale from before breeze_rod was inserted into the chain (PF 1.13.0 / #161).
- BEFORE:
  quest.7CA7E000C0DE000E.quest_desc: [
  	"Last of the Cave line: &bglow ink milk&r into a &cRedstone Slime&r."
  	""
  	"Redstone is the spark under everything mechanical, and now it drips out of a frog. Loop it, turn in the &bRedstone Froglight&r, and the Cave is yours top to bottom. Smelt the Froglight for redstone."
  ]
- AFTER:
  quest.7CA7E000C0DE000E.quest_desc: [
  	"Last of the Cave line: &bbreeze rod milk&r into a &cRedstone Slime&r."
  	""
  	"Redstone is the spark under everything mechanical, and now it drips out of a frog. Loop it, turn in the &bRedstone Froglight&r, and the Cave is yours top to bottom. Smelt the Froglight for redstone."
  ]

## Chapter summary
- Quests: 8 total, 4 EDIT, 4 CLEAN
- Accuracy bugs (WRONG ledger rows): 3
  1. Redstone (000E): claims "glow ink milk" makes the Redstone Slime - it's actually **breeze rod milk** (chain stale since breeze_rod was inserted, PF 1.13.0/#161). Highest severity.
  2. Beyond Iron (0002): lists lapis + obsidian as Cave-frog resources - lapis is Geode-chapter, obsidian is Infernal-category. Overpromises chapter scope.
  3. Breeze Rod (0026): "wind charges and all" - the frog produces the Breeze Rod Froglight (smelts to a breeze rod), not wind charges.
- Highest-severity finding: Redstone quest names the wrong feeder milk (glow ink vs breeze rod) - a new player following the prose would try the wrong recipe and the slime-bucket craft would not appear.
- Task-vs-text: all 6 resource quests use a `productivefrogs:configurable_froglight` item task with the correct `slime_variant` component and `match_components: strict` - froglight-check law satisfied. Player filter task = `darkutils:filter_player` item; Beyond Iron = checkmark gate. All tasks align with prose. Terminology "Froglight" (never "Configurable Froglight") is correct throughout. No em/en dashes found; color codes balanced and `&r`-closed.
