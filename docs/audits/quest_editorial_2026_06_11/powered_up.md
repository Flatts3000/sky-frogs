# Audit: powered_up ("Powered Up")

Mod(s) referenced: Powah (6.2.8), Flux Networks (8.0.0), Productive Frogs (1.20.0), Mekanism (prior-tier reference). Generated chapter: no.

## Mechanic-claims ledger

| Quest | Claim (paraphrase) | Source checked (jar path / pack override) | Verdict |
|-------|--------------------|-------------------------------------------|---------|
| Dielectric Paste | "three coals, two clay, a bucket of lava" makes dielectric paste | powah `recipe/crafting/dielectric_paste.json` (shapeless: 3x `#minecraft:coals` + 2x clay_ball + 1x lava_bucket -> 24 paste) | MATCHES (text omits that one craft yields 24, not load-bearing) |
| The Furnator | "Paste, a tiny capacitor, a casing, and a plain furnace build the Furnator" | powah `recipe/crafting/furnator_starter.json` (dielectric_paste, capacitor_basic_tiny, dielectric_casing, furnace) | MATCHES |
| The Furnator | "Mekanism's Heat Generator got you here" (prior-tier framing) | Geode automation chapter context | MATCHES (narrative back-reference, not a mechanic) |
| Bottled Lightning | Energy Cell buffers Furnator output | powah `recipe/crafting/energy_cell_starter.json` (block.powah.energy_cell_starter = "Energy Cell (Starter)") | MATCHES |
| The Energizing Orb | "crafts by burning raw FE: ring it with Energizing Rods, give it power, drop materials in" | powah energizing machine; reward = `energizing_rod_starter`; orb is the `powah:energizing` recipe machine | MATCHES |
| Energized Steel | "Orb iron and gold into Energized Steel" | powah `recipe/energizing/energized_steel.json` (`#c:ingots/iron` + `#c:ingots/gold` -> 2x steel_energized) | MATCHES |
| Energized Steel | "make a resource yourself once, the Dissolution Chamber will slime it" (self-keyed) | pack `dissolution_slime_recipes.js` L189 MODDED_SELF_KEYED (`energized_steel` <- `powah:steel_energized`, CAVE filler stone) | MATCHES |
| Uraninite | "no uraninite ore... the Orb presses uraninite from uranium ingots" | powah `recipe/energizing/uraninite_from_uranium.json` (`#c:ingots/uranium` -> uraninite) | MATCHES |
| Uraninite | "uranium sits near the end of the All the Ores seed chain (osmium milk onward)" | pack `ato_slime_chain.js` L9 (osmium->aluminum->lead->nickel->silver->tin->uranium->zinc; uranium is 7th of 8) | MATCHES |
| Uraninite | "A Uraninite Slime can also roll straight out of the Cave pool by split-discovery" | PF slime_variant `uraninite.json` category=cave; pack `ato_slime_chain.js` L4 + `dissolution_slime_recipes.js` L164 treat split-discovery as the real same-category fallback | MATCHES (mechanic confirmed real and category-correct; exact roll odds unverifiable) |
| Dry Ice | "Orb presses Dry Ice from two blue ice; blue ice is 81 ice packed twice" | powah `recipe/energizing/dry_ice.json` (2x `#c:ices/blue` -> dry_ice); blue ice = 9 packed ice = 81 ice | MATCHES |
| Dry Ice | "Tide pool can also roll a Dry Ice Slime by split-discovery" | PF slime_variant `dry_ice.json` category=tide; same split-discovery model as above | MATCHES (same caveat) |
| Blazing Crystal | "Orb wants blaze powder - four of it - for a Blazing Crystal" | powah `recipe/energizing/blazing_crystal.json` (4x blaze_powder -> crystal_blazing) | MATCHES |
| Blazing Crystal | "Infernal frog makes the rods; each rod cracks into two powder" | vanilla blaze_rod -> blaze_powder is 1:2; Infernal frog = blaze_rod variant | MATCHES |
| Niotic Crystal | "Orbed from diamonds" | powah `recipe/energizing/niotic_crystal.json` (1x `#c:gems/diamond` -> crystal_niotic) | MATCHES |
| Niotic Crystal | "the slime rides a Void frog" | PF slime_variant `niotic.json` category=void | MATCHES |
| Spirited Crystal | "Orbed from emeralds" | powah `recipe/energizing/spirited_crystal.json` (1x `#c:gems/emerald` -> crystal_spirited) | MATCHES |
| Nitro Crystal | "a nether star, two redstone blocks, and a block of Blazing Crystal" | powah `recipe/energizing/nitro_crystal.json` (`#c:nether_stars` + 2x `#c:storage_blocks/redstone` + 1x `powah:blazing_crystal_block` -> 16x crystal_nitro) | MATCHES (block of blazing crystal, not the item - correctly stated) |
| The Uraninite Reactor | "multiblock that sips uraninite... Build a Starter Reactor" | powah `recipe/crafting/reactor_starter.json` (4x uraninite + 4x capacitor_basic_tiny + dielectric_casing -> 4x reactor_starter); block name "Reactor (Starter)" | MATCHES |
| Flux Dust | "ritual: redstone thrown onto obsidian that rests on bedrock, punch the obsidian" | FN tooltip "compressing Redstone Dust with Bedrock and Obsidian"; pack `gen_starter_island.py` L41/49 (one bedrock at island center) | MATCHES |
| Flux Dust | "crafting grid presses one dust from redstone sandwiched between two obsidian" | pack override `flux_dust_recipe.js` (shaped O/R/O = obsidian, redstone, obsidian -> 1x flux_dust) | MATCHES |
| Flux Dust | "Once you own a Flux Block, that works as the anvil too" | FN `flux_block` exists; whether it substitutes for the bedrock anvil base is not in readable jar data | UNVERIFIABLE (plausible known FN behavior; no jar evidence either way) |
| Flux on Tap | "you made the dust yourself, so the chamber law is satisfied: slime it, feed the Infernal frog" | pack `dissolution_slime_recipes.js` L192 (`flux_dust` <- `fluxnetworks:flux_dust`, INFERNAL filler prismarine); PF flux_dust category=infernal | MATCHES |
| The Network Is Live | "Controller runs the network, a Plug drinks FE in, a Point pours it out" | FN tooltips: Plug "Receives energy from adjacent blocks... adding energy to your Flux Network"; Point "Provides energy to adjacent blocks... removing energy"; Controller "Enables Wireless Charging" | MATCHES (Plug = input, Point = output - correct) |
| The Network Is Live | task "Build all three" (Controller + Plug + Point) | chapter .snbt tasks 70E000000000002D/2E/2F (flux_controller, flux_plug, flux_point) | MATCHES |

## Per-quest findings

### Dielectric Paste (quest.70E0000000000004)
- Disposition: CLEAN
- Recipe correct; "Mash up 4" matches the task (item, count 4). The one-craft yield is 24 but the text never claims 4-per-craft, so no fix needed.

### The Furnator (quest.70E0000000000007)
- Disposition: EDIT
- Voice & tone: "your Coal frog has opinions" is a cute non-statement - it gestures at fuel preference without telling the player anything actionable. The Furnator burns any solid fuel; the sentence adds words, not help. Tighten to state the real point (any burnable works) and keep the warm register.
- BEFORE:
  ```
  quest.70E0000000000007.quest_desc: [
  	"Paste, a tiny capacitor, a casing, and a plain furnace build the &eFurnator&r - Powah's starter generator. Feed it anything that burns; your Coal frog has opinions."
  	""
  	"Mekanism's Heat Generator got you here. This chapter is the scaling arc."
  ]
  ```
- AFTER:
  ```
  quest.70E0000000000007.quest_desc: [
  	"Paste, a tiny capacitor, a casing, and a plain furnace build the &eFurnator&r - Powah's starter generator. Feed it anything that burns; your Coal frog keeps it stocked."
  	""
  	"Mekanism's Heat Generator got you here. This chapter is the scaling arc."
  ]
  ```

### Bottled Lightning (quest.70E000000000000B)
- Disposition: CLEAN
- Energy Cell buffering claim and cable-facade reward framing both accurate.

### The Energizing Orb (quest.70E000000000000E)
- Disposition: CLEAN
- "crafts by burning raw FE: ring it with Energizing Rods, give it power, drop materials in" matches Powah's orb operation.

### Energized Steel (quest.70E0000000000011)
- Disposition: CLEAN
- Iron+gold->energized steel correct; the self-keyed Dissolution Chamber "law" framing matches the pack override. Length is justified - this is the first modded-variant chamber use and the rule needs stating once.

### Uraninite (quest.70E0000000000014)
- Disposition: EDIT
- Voice & tone: the longest single description in the chapter and the most padded. The uranium-chain sourcing, the Orb press, AND the split-discovery aside all land in one run-on. Every fact is correct; the prose just over-explains. Trim the parenthetical hedging ("if luck beats labor - either way") without dropping any mechanic.
- BEFORE:
  ```
  quest.70E0000000000014.quest_desc: [
  	"There is no uraninite ore on a void skyblock - but the Orb presses &buraninite&r from &buranium ingots&r. Uranium has no ore here either: it sits near the end of the &aAll the Ores seed chain&r (osmium milk onward, the same milk-and-frogspawn craft as the Cave metals), so raise a &aUranium frog&r and feed the Orb its harvest. A &aUraninite Slime&r can also roll straight out of the Cave pool by split-discovery, if luck beats labor - either way, one slime is all the chamber needs to scale the farm."
  	""
  	"Turn in the &bUraninite Froglight&r."
  ]
  ```
- AFTER:
  ```
  quest.70E0000000000014.quest_desc: [
  	"No uraninite ore on a void skyblock - but the Orb presses &buraninite&r from &buranium ingots&r. Uranium has no ore here either; it sits near the end of the &aAll the Ores seed chain&r (osmium milk onward, same milk-and-frogspawn craft as the Cave metals), so raise a &aUranium frog&r and feed the Orb its harvest. A &aUraninite Slime&r can also turn up from a Cave frog's split, but one slime, however you get it, is all the chamber needs to scale the farm."
  	""
  	"Turn in the &bUraninite Froglight&r."
  ]
  ```

### Dry Ice (quest.70E0000000000017)
- Disposition: CLEAN
- "two blue ice... blue ice is 81 ice packed twice" is accurate and a genuinely helpful aside (tells the player how much ice frog output is needed). Split-discovery aside is correct and brief.

### Blazing Crystal (quest.70E000000000001A)
- Disposition: CLEAN
- 4 blaze powder, rod-cracks-into-two-powder, all accurate.

### Niotic Crystal (quest.70E000000000001D)
- Disposition: CLEAN
- Diamond input correct; Void-frog slime gating correct.

### Spirited Crystal (quest.70E0000000000020)
- Disposition: CLEAN
- Emerald input correct; Void-frog gating correct.

### Nitro Crystal (quest.70E0000000000023)
- Disposition: CLEAN
- Nether star + 2 redstone blocks + blazing crystal BLOCK all correct (text says "block of Blazing Crystal" - right). Void-frog gating correct.

### The Uraninite Reactor (quest.70E0000000000026)
- Disposition: CLEAN
- Multiblock sipping uraninite, "Build a Starter Reactor" matches the reactor_starter task.

### Flux Dust (quest.70E0000000000029)
- Disposition: CLEAN
- Native ritual (redstone on obsidian on bedrock, punch), bedrock-heart claim, and crafting-grid fallback all ground-truth correctly against the FN tooltip and the pack override. Dense but every sentence is load-bearing. (The Flux-Block-as-anvil line is unverifiable from jar data - left as-is; it is a known FN feature and reads as a low-risk aside.)

### Flux on Tap (quest.70E000000000002C)
- Disposition: CLEAN
- Self-keyed chamber framing matches the override; Infernal-frog gating correct.

### The Network Is Live (quest.70E0000000000031)
- Disposition: CLEAN
- Controller/Plug(in)/Point(out) directions match FN tooltips exactly; "Build all three" matches the three tasks.

## Chapter summary
- Quests: 15 total, 2 EDIT, 13 CLEAN
- Accuracy bugs (WRONG ledger rows): 0 - every recipe, machine, ingredient, drop, and item/block name ground-truthed correctly against the Powah/Flux Networks/Productive Frogs jars and the pack's `flux_dust_recipe.js` + `dissolution_slime_recipes.js` overrides.

VERIFY PASS (adversarial re-check): CONFIRMED 0 accuracy bugs. Re-verified the highest-risk override/category claims: dissolution_slime_recipes.js self-keyed rows L188-193 (uraninite<-powah:uraninite, energized_steel<-powah:steel_energized, dry_ice<-powah:dry_ice, flux_dust<-fluxnetworks:flux_dust, niotic<-powah:crystal_niotic) all present; flux_dust_recipe.js = O/R/O obsidian-redstone-obsidian; PF variant categories uraninite=cave, dry_ice=tide, niotic=void all confirmed. No false positives. The "Flux Block as anvil" UNVERIFIABLE claim remains unverifiable from jar data (left as low-risk aside, correctly not flagged as an EDIT).
- Highest-severity finding: none factual. The two EDITs are pure tightening - the Furnator's vague "Coal frog has opinions" filler and the Uraninite description's over-padded split-discovery aside. Voice target (factual not technical, helpful not verbose) is otherwise already well met across the chapter.
- One UNVERIFIABLE claim for the verify pass to dig into: Flux Dust's "Once you own a Flux Block, that works as the anvil too" - the Flux Block item exists in the FN jar, but I could find no jar data confirming it substitutes for bedrock as the ritual anvil base. It is a plausible known Flux Networks behavior; not flagged as an EDIT.
