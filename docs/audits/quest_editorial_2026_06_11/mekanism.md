# Audit: mekanism ("Power and Machines")

Mod(s) referenced: Mekanism, MekanismGenerators, All the Ores (steel ingot), Productive Frogs (froglight/slime), Functional Storage / Building Gadgets 2 (rewards only). Generated chapter: no.

## Mechanic-claims ledger

| Quest | Claim (paraphrase) | Source checked (jar path / pack override) | Verdict |
|-------|--------------------|-------------------------------------------|---------|
| Osmium | Osmium Slime in a Bucket = redstone milk + 4 stone + 3 sweetslime + Cave frogspawn bottle | pack `osmium_slime_bucket.js` (shapeless: redstone_slime_milk_bucket + 4 stone + 3 sweetslime + cave frog_egg) | MATCHES |
| Osmium | Osmium Froglight smelts to osmium; osmium is a Cave-frog variant | PF `configurable_froglight_*` smelt pattern; pack script header confirms osmium = CAVE variant, ATO-gated | MATCHES |
| First Power | Heat Generator is Mekanism's starter generator, burns coal or a lava bucket | MekanismGenerators heat generator (burns furnace solid fuel + lava); lang "Heat Generator" | MATCHES |
| First Power | Cave frog makes coal | PF coal is a Cave variant froglight (`configurable_froglight_coal_to_coal.json`) | MATCHES |
| Metallurgic Infuser | Infuser presses one material into another, powered; turns iron into enriched iron | Mekanism `processing/iron/enriched.json` = metallurgic_infusing iron + carbon -> enriched_iron | MATCHES |
| Steel | "Infuse iron with carbon into enriched iron, then smelt that into a Steel Ingot" | Mekanism steel chain: iron+carbon->enriched_iron; **enriched_iron+carbon->steel DUST** (`enriched_iron_to_dust.json`); **dust** smelts to ingot (`from_dust_smelting.json`) | WRONG - skips the 2nd infusion. You cannot smelt enriched iron into a steel ingot. Enriched iron must be infused with carbon AGAIN to make steel dust, and the DUST is what smelts. -- VERIFY: VERIFIED. Mekanism-1.21.1-10.7.19.85.jar: `processing/iron/enriched.json` (iron+carbon -> enriched_iron); `processing/steel/enriched_iron_to_dust.json` = metallurgic_infusing, 10mB carbon + enriched_iron -> `mekanism:dust_steel`; `from_dust_smelting.json` smelts dust_steel -> ingot_steel. NO recipe smelts enriched_iron directly to a steel ingot. Checked PF datapack for a steel shortcut: none (PF's steel recipes are froglight/crucible paths, a different chapter). AFTER edit (two infusions, then smelt the dust) is correct -- apply. The task-vs-text `alltheores:steel_ingot` vs `mekanism:ingot_steel` mismatch is a real STRUCTURE issue, correctly routed out of text scope. |
| Steel | Task turn-in is a Steel Ingot (`alltheores:steel_ingot`) | chapter task id `alltheores:steel_ingot`; Mekanism path yields `mekanism:ingot_steel`. ATO's from-scratch steel recipes are all conditioned on enderio/immersiveengineering, **neither loaded**; only live ATO route is `c:dusts/steel` -> dust_smelting | WRONG (task-vs-text) - the Mekanism path the prose teaches produces `mekanism:ingot_steel`, a different item id than the `alltheores:steel_ingot` the task requires. Furnace-smelting `mekanism:dust_steel` has two competing recipes (Mekanism's -> mekanism ingot; ATO's tag recipe -> ATO ingot); the player can't reliably land the ATO ingot. STRUCTURE issue - flag for the chapter owner. |
| Steel Casing | "the shell every Mekanism machine is built into" | Mekanism `steel_casing.json` (steel + osmium + cheap glass); it is the machine-block base | MATCHES |
| Steel Slime | Infuse a Bucket of Iron Slime Milk with carbon (coal/charcoal) -> Steel Slime in a Bucket | pack `steel_slime_infusing.js` (metallurgic_infusing: iron_slime_milk_bucket + 10mB carbon -> steel slime_bucket) | MATCHES |
| Steel Slime | carbon comes from coal or charcoal | Mekanism `chemical_conversion/carbon/from_coal.json`, `from_charcoal.json` | MATCHES |
| Steel Slime | Steel Froglight smelts for steel | PF froglight smelt pattern (steel variant -> steel ingot) | MATCHES |
| Wind Generator | Passive, no fuel, output rises with altitude; "a couple of Energy Tablets do most of the work" | MekanismGenerators `generator/wind.json` (pattern uses 2x `mekanism:energy_tablet`); Wind Generator output scales with Y | MATCHES |
| Energized Smelter | Runs on stored Joules, faster than a furnace; "back half of ore-doubling - dusts in, ingots out" | Mekanism Energized Smelter smelts (incl. dusts -> ingots); pairs with Enrichment Chamber | MATCHES |
| Enrichment Chamber | "run a metal Froglight through it and it splits into two dusts ... one froglight becomes two ingots ... frog metals, doubled" | Mekanism enriching: **ore -> 2 dust** (`dust/from_ore.json`); **ingot -> 1 dust via CRUSHING, not enriching** (`dust/from_ingot.json` is `mekanism:crushing`). PF froglight smelts to an **ingot**, not an ore (`configurable_froglight_iron_to_iron_ingot.json`). No pack recipe doubles a froglight. | WRONG - a Froglight is not an ore. Enrichment Chamber doubling only applies to ores/raw ores. A metal froglight (or its smelted ingot) cannot be doubled here: ingot->dust is 1:1 (and is a Crusher job, not the Enrichment Chamber). The "frog metals, doubled" payoff does not exist with the items the player actually has. |
| Enrichment Chamber | "Gems pass through unchanged - only the metals dust" | derived claim; gems (diamond/emerald/quartz) have no enriching-to-dust recipe | MATCHES (gems indeed don't dust) - but moot, since the metal-doubling premise is false |

## Per-quest findings

### Osmium (quest.6ECA150000000002)
- Disposition: CLEAN
- Recipe, froglight check, and task all match `osmium_slime_bucket.js` and the chapter task (osmium froglight, strict components). Color codes balanced. No dashes.

### First Power (quest.6ECA150000000005)
- Disposition: CLEAN
- Heat Generator as starter generator and coal/lava fuel both verified. Task = craft `mekanismgenerators:heat_generator`, matches.

### The Metallurgic Infuser (quest.6ECA150000000008)
- Disposition: CLEAN
- "presses one material into another, powered" and "turn iron into the enriched iron that becomes steel" both correct. Task = craft the infuser.

### Steel (quest.6ECA15000000000B)
- Disposition: EDIT
- Issues:
  - Factual accuracy: the steel chain is mis-stated. Enriched iron does NOT smelt into a steel ingot. The real chain is iron + carbon (infuse) -> enriched iron; enriched iron + carbon (infuse AGAIN) -> steel dust; steel dust (smelt) -> steel ingot. The current text drops the second infusion.
  - Task-vs-text (STRUCTURE, flag only): task requires `alltheores:steel_ingot`, but the Mekanism path taught here yields `mekanism:ingot_steel`. With enderio/IE absent, the player cannot reliably produce the ATO ingot from the Mekanism flow. Recommend the chapter owner switch the task to a `c:ingots/steel` tag match (covers both) or to `mekanism:ingot_steel`. Note: steel is a sanctioned froglight-check EXCEPTION (checks the smelted ingot, not a froglight) per CLAUDE.md - that part is fine; only the specific item id is the problem.
- BEFORE:
  ```
  quest.6ECA15000000000B.quest_desc: [
  	"Infuse iron with carbon into &fenriched iron&r, then smelt that into a &bSteel Ingot&r."
  	""
  	"Steel is the backbone of every Mekanism machine. Bring one back."
  ]
  ```
- AFTER:
  ```
  quest.6ECA15000000000B.quest_desc: [
  	"In the &eMetallurgic Infuser&r, infuse iron with &fcarbon&r to get &fenriched iron&r, then infuse that with carbon a second time to get &fsteel dust&r. Smelt the dust into a &bSteel Ingot&r."
  	""
  	"Steel is the backbone of every Mekanism machine. Bring one back."
  ]
  ```

### Steel Casing (quest.6ECA15000000000E)
- Disposition: CLEAN
- "the shell every Mekanism machine is built into" matches steel_casing as the machine base block. Task = craft `mekanism:steel_casing`.

### Energized Smelter (quest.6ECA150000000017)
- Disposition: CLEAN
- Runs on stored energy, faster than a furnace, dust->ingot half of ore processing - all accurate. (The "ore-doubling" reference here is generic and correct for ores; the broken-doubling problem is specific to the Enrichment Chamber quest's froglight claim.)

### Enrichment Chamber (quest.6ECA15000000001A)
- Disposition: CLEAN (corrected 2026-06-11 - original audit finding was a FALSE POSITIVE)
- CORRECTION: The original audit flagged the "frog metals, doubled" payoff as mechanically impossible. That was WRONG. The doubling is real and ships in Productive Frogs' OWN jar datapack, not the pack KubeJS or the Mekanism jar (which is why the audit agent missed it - it only cracked the Mekanism jar + pack overrides). Verified directly + confirmed by an in-game JEI screenshot from the user:
  - `data/productivefrogs/recipe/mekanism/{iron,gold,copper,osmium,aluminum,lead,nickel,silver,tin,uranium,zinc}.json` are `mekanism:enriching` recipes: input = `productivefrogs:configurable_froglight` keyed by a `slime_variant` component, output = `count: 2` of the matching dust (e.g. silver -> `alltheores:silver_dust` x2). 11 recipes, each `neoforge:mod_loaded`-gated.
  - The dust smelts to an ingot, so one metallic Froglight enriches to 2 dust -> 2 ingots. The JEI Enrichment Chamber category shows the full per-variant set (user screenshot: "Silver Froglight" -> 2 dust).
  - Therefore the BEFORE text below ("run a metal Froglight through it and it splits into two dusts ... one froglight becomes two ingots ... Your frog metals, doubled") is ACCURATE. No edit needed.
- Current text (accurate, keep as-is):
  ```
  quest.6ECA15000000001A.quest_desc: [
  	"The payoff. The &eEnrichment Chamber&r is Mekanism's ore-doubler - run a metal &bFroglight&r through it and it splits into &btwo dusts&r. Feed those to the Energized Smelter and one froglight becomes &btwo ingots&r."
  	""
  	"Your frog metals, doubled. (Gems pass through unchanged - only the metals dust.)"
  	""
  	"For wiring it all together, a &eBuilding Gadget&r to throw up machine rooms in a click."
  ]
  ```
  - Lesson recorded as a memory ([[project-pf-ships-crossmod-recipes]]): when checking a cross-mod froglight mechanic, authority order is (1) pack KubeJS, (2) PF's own `data/productivefrogs/recipe/` datapack, (3) the other mod's jar. The PF datapack is the easy one to miss.

### Steel Slime (quest.6ECA150000000011)
- Disposition: CLEAN
- Iron Slime Milk + carbon (coal/charcoal) -> Steel Slime in a Bucket via the infuser matches `steel_slime_infusing.js` exactly. Froglight-check task (steel variant, strict) matches. "Bucket of Iron Slime Milk" and "Steel Slime in a Bucket" terminology consistent with PF 1.8 per-variant milk items.

### Wind Generator (quest.6ECA150000000014)
- Disposition: CLEAN
- Passive, fuel-free, altitude-scaling output all correct; recipe uses 2 Energy Tablets ("a couple") - matches. Optional/diamond-shape quest. Minor: "Energy Tablets from the Infuser" is a loose shorthand (the tablet is crafted; its infused-alloy component comes from the infuser) - acceptable, not worth an edit.

## Chapter summary
- Quests: 9 total, 1 EDIT, 8 CLEAN (was 2 EDIT before the Enrichment Chamber false positive was corrected)
- Accuracy bugs (WRONG ledger rows): 1 confirmed (+ 1 structural task-id, + 1 REJECTED false positive)
  1. Steel: enriched iron does not smelt to a steel ingot - the 2nd carbon infusion (enriched iron -> steel dust) is omitted; the dust is what smelts. CONFIRMED.
  2. Steel (task-vs-text, STRUCTURE, not text): task wants `alltheores:steel_ingot` but the taught Mekanism path yields `mekanism:ingot_steel`; ATO's from-scratch steel routes are enderio/IE-gated and not loaded. Recommend tag match `c:ingots/steel`. This is a chapter-structure fix (task item id), out of editorial-text scope - route to the chapter owner / a GitHub issue.
  3. Enrichment Chamber: REJECTED (false positive). The froglight-doubling is real via PF's datapack (see corrected entry above). No edit.
- Highest-severity remaining finding: Steel chain mis-statement (the smelt-enriched-iron step is impossible as written) - a real follow-the-text-and-fail bug. Fix the copy to name the second infusion.
