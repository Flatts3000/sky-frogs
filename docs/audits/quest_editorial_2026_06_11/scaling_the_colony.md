# Audit: scaling_the_colony ("Scaling the Colony")

Mod(s) referenced: Ex Deorum (Hammer, Barrel), Productive Frogs (Sweetslime, breeding/stats, Froglights), Botany Pots, Iron Furnaces, vanilla (mud, flower pot, terracotta). Generated chapter: no.

## Mechanic-claims ledger
| Quest | Claim (paraphrase) | Source checked (jar path / pack override) | Verdict |
|-------|--------------------|-------------------------------------------|---------|
| Hands Off | Chapter starts by pulverizing cobblestone | exdeorum hammer chain (below) | MATCHES |
| Grind It Down | Iron Hammer grinds cobble -> gravel -> sand -> Dust | exdeorum `recipe/hammer/{gravel,sand,dust}.json` | MATCHES |
| Grind It Down | clay starts as cobblestone run through a Hammer | exdeorum hammer chain + barrel_mixing/clay.json | MATCHES (cobble->...->dust->clay) |
| Grind It Down | item name "Dust"; "Iron Hammer" | exdeorum lang: `block.exdeorum.dust`="Dust", `item.exdeorum.iron_hammer`="Iron Hammer" | MATCHES |
| Just Add Water | Fill Ex Deorum Barrel with water + drop Dust in -> clay | exdeorum `recipe/barrel_mixing/clay.json` (dust + 1000mB water -> minecraft:clay) | MATCHES |
| Fired Earth | smelt clay block -> Terracotta; clay balls -> bricks; 3 bricks -> Flower Pot | vanilla recipes | MATCHES |
| A Pot to Grow In | 5 terracotta around a flower pot -> Botany Pot | botanypots `recipe/.../terracotta_botany_pot.json` pattern `["M M","MPM"," M "]`, M=terracotta P=flower_pot | MATCHES (5 terracotta + 1 flower pot) |
| A Pot to Grow In | Botany Pot self-tends crops; saplings grow trees | botanypots is the data-driven self-growing planter; ships sapling/shrub crop defs | MATCHES |
| Sweet Tooth | sugar + slime ball -> Sweetslime | PF `recipe/sweetslime.json` (slime_ball + sugar -> sweetslime x2) | MATCHES |
| Sweet Tooth | Sweetslime breeds frogs + binds new resource slimes | PF config `[frog_stats]` (Sweetslime is the breeding item) + pack `*_slime_chain.js` use sweetslime as binder | MATCHES |
| Dirt from Decay | Ex Deorum Barrel composts organic scraps -> dirt | exdeorum `recipe/barrel_compost/*` + advancement "compost organic material into dirt" | MATCHES |
| Make Mud | water bottle on dirt -> mud; items fall through mud | vanilla 1.19+ (mud is a non-full block items drop through) | MATCHES |
| A Floor of Hoppers | hopper under each mud block catches what falls through | vanilla hopper | MATCHES |
| Hands-Free Froglights | Iron Furnace pushes finished output to an adjacent inventory on its own | ironfurnaces lang `tooltip.ironfurnaces.gui_auto_output`="Auto Output" (Auto Input/Output features) | MATCHES (mechanic exists; Auto Output is a GUI toggle, see note) |
| Raising the Line | stat names Appetite / Bounty / Reach; read with Jade on frog/tadpole/primed egg | PF lang `jade.appetite/bounty/reach`, `frog_net.stats`; Jade plugins for frog_stats/tadpole/primed egg | MATCHES |
| Raising the Line | stats run 1-10; 10/10/10 is the cap | PF config `statCap = 10` | MATCHES |
| Raising the Line | regress toward parent average, else hold at better parent | PF config `regressionChance = 0.3` (to parent average), remainder holds at better parent | MATCHES |
| Raising the Line | "roughly 1 in 5" chance a stat climbs above the better parent | PF config `improvementChance = 0.4` (per stat) | **WRONG - it is 0.40 (~2 in 5), not 1 in 5. 0.20 was the pre-1.19.1 default.** -- VERIFY: VERIFIED. Live instance config `productivefrogs-common.toml` line 157 `improvementChance = 0.4`, line 163 `regressionChance = 0.3`, line 167 `statCap = 10`. Pack config does NOT override these (inherits jar default per PF 1.19.1 "Survival of the Fittest"). AFTER edit ("2 in 5" climb, "3 in 10" regress) is correct -- apply. Also strip the "(new page placeholder text)" scaffold. |

## Per-quest findings

### Hands Off (quest.2A5700000A570002)
- Disposition: CLEAN
- Strong intro framing; accurate; no formatting/punctuation issues.

### Grind It Down (quest.2A5700000A570005)
- Disposition: CLEAN
- Hammer chain (cobble->gravel->sand->Dust), "Dust" and "Iron Hammer" names all verified correct.

### Just Add Water (quest.2A5700000A570008)
- Disposition: CLEAN
- barrel_mixing dust+water->clay verified; "same barrel that catches rainwater" is accurate (Ex Deorum barrels do both).

### Fired Earth (quest.2A5700000A57000B)
- Disposition: CLEAN
- Vanilla clay->terracotta / clay ball->brick / 3 bricks->flower pot all correct. (Task wants 1 terracotta + 1 flower pot; prose's "five terracotta" is forward-pointing to the next quest's pot recipe, not this task - acceptable, reads as a heads-up.)

### A Pot to Grow In (quest.2A5700000A57000F)
- Disposition: CLEAN
- 5-terracotta-around-flower-pot recipe verified; self-tending planter + sapling/tree support correct.

### Sweet Tooth (quest.2A5700000A570012)
- Disposition: CLEAN
- sugar + slime ball -> Sweetslime verified (note: yields 2 per craft; prose doesn't state a count so no conflict). Dual role (breeding + slime-chain binder) accurate.

### Dirt from Decay (quest.2A5700000A570015)
- Disposition: CLEAN
- Compost-organics-to-dirt verified against Ex Deorum compost recipes + advancement text.

### Make Mud (quest.2A5700000A570018)
- Disposition: CLEAN
- Water-bottle-on-dirt and items-fall-through-mud are correct vanilla behavior; reward math (8 more for 9 total, 3x3) is internally consistent.

### A Floor of Hoppers (quest.2A5700000A57001B)
- Disposition: CLEAN
- Vanilla hopper behavior; reward math consistent with the 3x3 floor.

### Hands-Free Froglights (quest.2A5700000A57001E)
- Disposition: EDIT (minor - optional)
- Issues: Factual nuance: Iron Furnace Auto Output is a per-furnace GUI toggle, not on by default. "shoves its finished output straight into an adjacent inventory on its own" is true once Auto Output is enabled; a brand-new player may not know to flip it. Worth one clause so the build doesn't silently fail to push.
- BEFORE:
  "The last piece. Craft an &eIron Furnace&r - unlike a vanilla one, it shoves its finished output straight into an adjacent inventory on its own."
- AFTER:
  "The last piece. Craft an &eIron Furnace&r - unlike a vanilla one, it can push its finished output straight into an adjacent inventory. Open it and toggle &eAuto Output&r on."

### Raising the Line (quest.2A5700000A570022)
- Disposition: EDIT
- Issues: Factual accuracy (top priority): the per-stat improvement chance is stated as "&a1 in 5&r" but the pinned PF config is `improvementChance = 0.4` - about &a2 in 5&r per stat. "1 in 5" is the pre-1.19.1 default (0.20); PF 1.19.1 "Survival of the Fittest" raised it to 0.40 and the pack does not override it, so the live value is 0.40. This is the only hard accuracy bug in the chapter.
- Issues: Voice (minor): "(new page placeholder text)" after the `{@pagebreak}` is leftover scaffolding visible to players - should be removed or filled.
- BEFORE (the stat-roll line):
  "Each baby's stat is rolled from its parents: roughly &a1 in 5&r it climbs a point above the better parent, sometimes it slips back toward their average, otherwise it holds at the better of the two. So breed your &lbest with your best&r - over generations the whole line drifts upward."
- AFTER:
  "Each baby's stat is rolled from its parents: roughly &a2 in 5&r it climbs a point above the better parent, about &b3 in 10&r it slips back toward their average, otherwise it holds at the better of the two. So breed your &lbest with your best&r - over generations the whole line drifts upward."
- BEFORE (trailing scaffold lines):
  "{@pagebreak}"
  "(new page placeholder text)"
- AFTER (drop the placeholder; either remove the pagebreak block entirely or replace the placeholder with real second-page copy):
  (remove both lines, or replace "(new page placeholder text)" with intended continuation text)

## Chapter summary
- Quests: 11 total, 2 EDIT (1 hard, 1 minor/optional), 9 CLEAN
- Accuracy bugs (WRONG ledger rows): 1
  - Raising the Line: stat-improvement chance stated as "1 in 5" but live PF config is `improvementChance = 0.4` (~2 in 5); 0.20 was the pre-1.19.1 default the pack no longer runs.
- Highest-severity finding: the stale "1 in 5" breeding odds in Raising the Line - a player optimizing their stat line is being told the climb is half as fast as it actually is. Fix to "2 in 5" (and optionally add the ~3 in 10 regression figure for symmetry); also strip the "(new page placeholder text)" scaffold.
