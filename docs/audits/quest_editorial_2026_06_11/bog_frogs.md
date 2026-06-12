# Audit: bog_frogs ("Bog Frogs")

Mod(s) referenced: Productive Frogs (productivefrogs-1.20.0.jar), Industrial Foregoing (industrialforegoing-1.21-3.6.38.jar), Functional Storage (rewards), Mekanism (crafting block path, in chain script), Botany Pots (botanypots-neoforge-1.21.1-21.1.42.jar). Generated chapter: no.

## Mechanic-claims ledger

| Quest | Claim (paraphrase) | Source checked (jar path / pack override) | Verdict |
|-------|--------------------|-------------------------------------------|---------|
| Beyond Dirt | Each resource threads off the prior one's Slime Milk (mud from dirt, clay from mud) | pack `bog_slime_chain.js` chain array | MATCHES |
| Beyond Dirt | Loop = prior milk + 4 mossy cobblestone + 3 sweetslime + a Bog frogspawn -> next Slime in a Bucket | pack `bog_slime_chain.js` (chain.forEach: `${from}_slime_milk_bucket` + 4 mossy_cobblestone + 3 sweetslime + bog frog_egg) | MATCHES |
| Beyond Dirt | Milk the slime, feed the frog, it drops the Froglight; turn in the Froglight before smelting | froglight-check law; tasks all want `configurable_froglight` w/ `slime_variant` | MATCHES |
| Mud | Mud Slime off dirt milk; smelt for mud | chain `['dirt','mud']`; variant `mud.json` primer_item minecraft:dirt -> resource mud | MATCHES |
| Clay | Clay from mud milk | chain `['mud','clay_ball']`; variant `clay_ball.json` (id is clay_ball) | MATCHES |
| Clay | Clay feeds terracotta, bricks | vanilla (smelt clay block -> terracotta; smelt clay ball -> brick) | MATCHES |
| Clay | Clay feeds concrete | vanilla: concrete powder = sand+gravel+dye, no clay | WRONG - concrete uses no clay. VERIFY: VERIFIED - vanilla concrete powder is sand+gravel+dye; no clay. No pack/mod recipe override adds clay->concrete (grep of pack server_scripts/data clay hits are only the Bog slime-chain, not a concrete recipe). |
| Clay | "Botany Pot soil all start here" (clay -> botany soil) | botanypots jar: no soil recipe takes clay; base soils are code/dirt-derived | UNVERIFIABLE - no clay-based Botany Pots soil found. VERIFY: VERIFIED-WRONG (claim unsupported) - Botany Pots soils are tag/code-generated (MissingSoilGenerator), no soil JSON recipes in jar; soil tags are dirt/sand/end/snow/lava/nether/water and the dirt tag contains no clay. No clay-based soil anywhere. Drop the Botany Pots claim. |
| Moss | Moss from clay milk; bonemeal-spreadable | chain `['clay_ball','moss']`; vanilla moss spreads w/ bone meal | MATCHES |
| Mycelium | Mycelium from moss milk; grows mushrooms without light | chain `['moss','mycelium']`; vanilla mycelium hosts mushrooms at any light | MATCHES |
| Lily Pad | Lily Pads from mycelium milk | chain `['mycelium','lily_pad']` | MATCHES |
| Plastic | Plastic from lily pad milk | chain `['lily_pad','plastic']` (IF-gated) | MATCHES |
| Plastic | "normal latex recipe is gone" -> frog is the only plastic source | pack `if_plastic_gate.js` removes `industrialforegoing:plastic` (the dryrubber->plastic smelt); c:plastic = only that item | MATCHES (gameplay) but IMPRECISE - the removed recipe is the dryrubber->plastic SMELT, the final step of the latex chain, not a "latex recipe" |
| Plastic | Plastic is the key to Industrial Foregoing; most machines need it | IF: plastic is a core crafting component (conveyors, machine frames) | MATCHES |
| Pink Slime | Pink Slime from plastic milk; IF's "living synthetic" | chain `['plastic','pink_slime']`; variant pink_slime.json primer industrialforegoing:pink_slime | MATCHES |
| Pink Slime | Reward = Speed, Efficiency, Processing addons (tier 2) | chapter rewards: speed/efficiency/processing_addon_tier_2; lang names "Speed/Efficiency/Processing" | MATCHES |
| Bone | Bone from the mob-drop lane bootstrap | `bone.json` BOG; bone lane seeds off bone_meal in chain script | MATCHES |
| Gunpowder | Gunpowder; TNT, fireworks, rockets | chain `['bone','gunpowder']`; vanilla uses | MATCHES |
| Rotten Flesh | Rotten flesh; cleric trade fodder, emergency food | chain `['gunpowder','rotten_flesh']`; vanilla (cleric buys rotten flesh, edible w/ hunger) | MATCHES |
| String | String; bows, fishing rods, scaffolding, "wool four-at-a-time" | chain `['rotten_flesh','string']`; vanilla 4 string -> 1 wool | MATCHES (phrasing slightly awkward) |
| Leather | Leather from string milk; books, armor, frames | chain `['string','leather']`; vanilla (book needs leather, armor, item frame) | MATCHES |
| Feather | Feathers from leather milk; arrows | chain `['leather','feather']`; vanilla arrow needs feather | MATCHES |
| Armadillo Scute | Armadillo scutes -> wolf armor | chain `['feather','armadillo_scute']`; vanilla wolf armor = armadillo scute | MATCHES |
| Honeycomb | Honeycomb -> waxed copper, hives, candles | chain `['armadillo_scute','honeycomb']`; vanilla uses | MATCHES |

All 16 variants confirmed `category: bog` in PF jar; all task froglight components valid.

## Per-quest findings

### Beyond Dirt (quest.7B06000000000002)
- Disposition: CLEAN
- Accurate intro: the threading model, the exact loop recipe, and the froglight-check law all match the pack scripts and the froglight-check rule. Voice is warm and on-target. No dashes, balanced color codes.

### Mud (quest.7B06000000000005)
- Disposition: CLEAN
- Accurate; concise. (Color codes balanced; "&6Froglight&r" correct term.)

### Clay (quest.7B06000000000008)
- Disposition: EDIT
- Issues: Factual accuracy: "concrete... start here" is wrong (concrete powder is sand+gravel+dye, no clay). "Botany Pot soil all start here" is unverifiable - no clay-based Botany Pots soil recipe exists in the jar. Trim to the verified vanilla uses.
- BEFORE:
  quest.7B06000000000008.quest_desc: [
  	"&bClay&r from your &emud milk&r - terracotta, bricks, concrete, and Botany Pot soil all start here."
  	""
  	"Clay compacts, so here's a &9Compacting Drawer&r to stack it."
  ]
- AFTER:
  quest.7B06000000000008.quest_desc: [
  	"&bClay&r from your &emud milk&r - terracotta, bricks, and flower pots all start here."
  	""
  	"Clay compacts, so here's a &9Compacting Drawer&r to stack it."
  ]

### Moss (quest.7B0600000000000B)
- Disposition: CLEAN
- Accurate (bone-meal spreadable, ground cover). Concise.

### Mycelium (quest.7B0600000000000E)
- Disposition: CLEAN
- Accurate (mushrooms grow on mycelium regardless of light). Concise.

### Lily Pad (quest.7B06000000000011)
- Disposition: CLEAN
- Accurate, flavorful, concise.

### Plastic (quest.7B0600000000001A)
- Disposition: EDIT
- Issues: Factual accuracy (imprecise): "the normal latex recipe is gone" misnames the removed recipe. The pack removes `industrialforegoing:plastic` (the Dry Rubber -> Plastic smelt, the final step of the latex chain), not a recipe literally named "latex." Gameplay claim (frog is the only plastic source) is correct; just name the removed step accurately. Minor.
- BEFORE:
  quest.7B0600000000001A.quest_desc: [
  	"The swamp turns synthetic. &fPlastic&r from your &elily pad milk&r - and since the &cnormal latex recipe is gone&r, this frog is now the &lonly&r source of plastic in the pack."
  	""
  	"Plastic is the key to &eIndustrial Foregoing&r - most of its machines need it - so the bog just became mandatory tech."
  ]
- AFTER:
  quest.7B0600000000001A.quest_desc: [
  	"The swamp turns synthetic. &fPlastic&r from your &elily pad milk&r - and since the &cnormal latex-to-plastic recipe is gone&r, this frog is now the &lonly&r source of plastic in the pack."
  	""
  	"Plastic is the key to &eIndustrial Foregoing&r - most of its machines need it - so the bog just became mandatory tech."
  ]

### Pink Slime (quest.7B0600000000001D)
- Disposition: CLEAN
- Accurate; reward labels match the actual addon items. Good capstone voice.

### Bone (quest.7B06000000000028)
- Disposition: CLEAN
- Accurate, on-voice.

### Gunpowder (quest.7B0600000000002B)
- Disposition: CLEAN
- Accurate.

### Rotten Flesh (quest.7B0600000000002E)
- Disposition: CLEAN
- Accurate (cleric trade, edible-with-risk).

### String (quest.7B06000000000031)
- Disposition: CLEAN
- Accurate. "wool four-at-a-time" is slightly awkward but reads correctly (4 string -> 1 wool). Left as-is; not worth churn.

### Leather (quest.7B06000000000014)
- Disposition: CLEAN
- Accurate (books, armor, item frames).

### Feather (quest.7B06000000000017)
- Disposition: CLEAN
- Accurate (arrows).

### Armadillo Scute (quest.7B06000000000022)
- Disposition: CLEAN
- Accurate (wolf armor from scute). Good "savanna's job" framing.

### Honeycomb (quest.7B06000000000025)
- Disposition: CLEAN
- Accurate (waxed copper, hives, candles).

## Chapter summary
- Quests: 16 total, 2 EDIT, 14 CLEAN
- Accuracy bugs (WRONG ledger rows): 2
  1. Clay: "concrete... start here" - concrete uses no clay (sand+gravel+dye). WRONG.
  2. Clay: "Botany Pot soil all start here" - no clay-based Botany Pots soil recipe in the jar. UNVERIFIABLE/likely wrong.
  (Plus 1 imprecise-but-functionally-correct claim in Plastic: removed recipe is the Dry Rubber->Plastic smelt, not a "latex recipe".)
- Highest-severity finding: Clay quest asserts two unsupported vanilla/mod uses (concrete + Botany Pots soil); only terracotta and bricks are verified. Recommend trimming to verified uses.
- Terminology: clean throughout - all player text says "Froglight," never "Configurable Froglight."
- Formatting/punctuation: no em/en dashes; color codes balanced; no broken escapes.
