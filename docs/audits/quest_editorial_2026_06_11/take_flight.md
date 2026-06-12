# Audit: take_flight ("Take Flight")

Mod(s) referenced: Iron Jetpacks (blakebr0), Mekanism, Industrial Foregoing (Dissolution Chamber), Curios, vanilla (Heavy Core, Mace, Breeze Rod, Wind Charge). Generated chapter: no.

## Mechanic-claims ledger
| Quest | Claim (paraphrase) | Source checked (jar path / pack override) | Verdict |
|-------|--------------------|-------------------------------------------|---------|
| Take Flight | Iron Jetpacks runs on frog metals + Forge Energy (RF) | config/ironjetpacks/jetpacks/iron.json (`capacity:800000`, `usage:120`, FE-driven) | MATCHES |
| Leather Strap | Strap = leather + iron nuggets | ironjetpacks `data/ironjetpacks/recipe/strap.json` (5 leather + 2 `c:nuggets/iron`) | MATCHES |
| Leather Strap | leather from Bog frog, iron nuggets from Cave frog | bog_slime_chain.js (leather=Bog), cave chain (iron=Cave) | MATCHES |
| Basic Coil | Basic Coil = iron, redstone, "a couple sticks" | `data/ironjetpacks/recipe/basic_coil.json` (4 `c:ingots/iron` + 2 `c:dusts/redstone` + 1 `c:rods/wooden`) | MATCHES (rod count is 1, "a couple sticks" overstates; minor) VERIFY: VERIFIED - basic_coil.json pattern " DR"/"DSD"/"RD ": D=c:ingots/iron(4), R=c:dusts/redstone(2), S=c:rods/wooden(1). Exactly 1 wooden rod; "a couple sticks" overstates. Fix to "a stick" correct. |
| Basic Coil | all Cave resources | cave_slime_chain.js (iron, redstone both Cave) | MATCHES |
| Off the Ground | Iron Jetpack = coil + cell + thruster + capacitor on the strap; Curios back slot | ironjetpacks DynamicRecipeManager + iron.json (`curios:true`); component lang `%s Energy Cell/Thruster/Capacitor` | MATCHES (item is "Iron Energy Cell", not bare "cell" - minor terminology) VERIFY: VERIFIED - ironjetpacks lang `item.ironjetpacks.cell` = "%s Energy Cell" -> "Iron Energy Cell". "energy cell" fix is correct. |
| Fuel and Fly | Charge from any Forge Energy source (Mekanism energy cube/cable); hold jump to fly, tap hover to hang | ironjetpacks config (FE capacity/usage); standard IJ controls | MATCHES |
| Advanced Coil | Advanced Coil swaps iron for gold; gold is a Cave frog | `advanced_coil.json` (4 `c:ingots/gold` + 2 redstone + 1 rod); cave chain (gold=Cave) | MATCHES |
| Elite Coil | Elite Coil runs on diamond; "Geode gem-tier" | `elite_coil.json` (4 `c:gems/diamond`); geode chain (diamond=Geode) | MATCHES |
| Ultimate Coil | Ultimate Coil = emerald, "the Geode capstone gem" | `ultimate_coil.json` (4 `c:gems/emerald`); geode_slime_chain.js chain ends `amethyst -> emerald -> diamond` | WRONG - **diamond is the Geode capstone, not emerald.** Chain order: `...amethyst, emerald, diamond`. Emerald is a Geode gem but the second-to-last; diamond is the final/capstone resource. VERIFY: VERIFIED - geode_slime_chain.js chain array ends `['amethyst','emerald'],['emerald','diamond']` -> diamond is final/capstone, emerald second-to-last. ultimate_coil.json D=c:gems/emerald (emerald is correctly the ingredient). Only the word "capstone" is wrong; drop it. |
| The Heavy Core | Dissolution Chamber presses Heavy Core from 4 iron blocks + 4 prismarine under latex | pack override kubejs/server_scripts/heavy_core_recipe.js (4 iron_block + 4 prismarine + 100 mB latex) | MATCHES |
| The Heavy Core | no trial chambers generate over the void | void skyblock worldgen (no trial chambers); heavy_core_recipe.js header confirms | MATCHES |
| Drop the Hammer | Breeze Rod + core = Mace; smash scales with fall distance | vanilla mace recipe (breeze_rod + heavy_core) + vanilla fall-damage scaling | MATCHES |
| Drop the Hammer | 1 breeze rod crafts 4 wind charges | vanilla `wind_charge` recipe (1 breeze_rod -> 4 wind_charge) | MATCHES |
| Drop the Hammer | breeze rod is frog-farmable | cave_slime_chain.js (breeze_rod is a Cave variant) | MATCHES |

## Per-quest findings

### Take Flight (quest.7F00000000000002)
- Disposition: CLEAN

### Leather Strap (quest.7F00000000000005)
- Disposition: CLEAN

### Basic Coil (quest.7F00000000000008)
- Disposition: EDIT
- Issues: Factual accuracy (minor): the recipe takes exactly 1 wooden rod, not "a couple sticks." Tighten to match.
- BEFORE:
  `quest.7F00000000000008.quest_desc: ["A &eBasic Coil&r - &firon&r, &fredstone&r, and a couple sticks - is the heart of the cheapest jetpack. Cave resources, all of it."]`
- AFTER:
  `quest.7F00000000000008.quest_desc: ["A &eBasic Coil&r - &firon&r, &fredstone&r, and a &fstick&r - is the heart of the cheapest jetpack. Cave resources, all of it."]`

### Off the Ground (quest.7F0000000000000B)
- Disposition: EDIT
- Issues: Terminology (minor): the component's in-game name is "Energy Cell" (e.g. Iron Energy Cell), not bare "cell." Match the item name so a new player recognizes it in JEI.
- BEFORE:
  `quest.7F0000000000000B.quest_desc: ["Build an &bIron Jetpack&r: the coil plus an iron &ecell&r, &ethruster&r, and &ecapacitor&r on the strap. Wear it in a &eCurios&r back slot (or over your chestplate) - you're a pilot now."]`
- AFTER:
  `quest.7F0000000000000B.quest_desc: ["Build an &bIron Jetpack&r: the coil plus an iron &eenergy cell&r, &ethruster&r, and &ecapacitor&r on the strap. Wear it in a &eCurios&r back slot (or over your chestplate) - you're a pilot now."]`

### Fuel and Fly (quest.7F0000000000000E)
- Disposition: CLEAN

### Advanced Coil (quest.7F00000000000011)
- Disposition: CLEAN

### Elite Coil (quest.7F00000000000014)
- Disposition: CLEAN

### Ultimate Coil (quest.7F00000000000017)
- Disposition: EDIT
- Issues: Factual accuracy: calls emerald "the Geode capstone gem." Per geode_slime_chain.js the Geode chain ends `amethyst -> emerald -> diamond`, so **diamond** is the Geode capstone; emerald is the gem one step before it. Drop the "capstone" claim (it is also internally confusing, since the Elite Coil one tier below uses diamond).
- BEFORE:
  `quest.7F00000000000017.quest_desc: ["The &eUltimate Coil&r tops it out with &femerald&r, the Geode capstone gem - the fastest jetpack in the pack. The void is yours to cross."]`
- AFTER:
  `quest.7F00000000000017.quest_desc: ["The &eUltimate Coil&r tops it out with &femerald&r from your Geode frog - the fastest jetpack in the pack. The void is yours to cross."]`

### The Heavy Core (quest.7F0000000000001A)
- Disposition: CLEAN
- Note: "4 iron blocks and 4 prismarine under latex" matches heavy_core_recipe.js exactly. The aside "Dense Cave ore, Tide stone" reads slightly compressed but is accurate (iron=Cave, prismarine=Tide). No change needed.

### Drop the Hammer (quest.7F0000000000001D)
- Disposition: CLEAN
- Note: mace recipe, fall-scaling smash, and 1-breeze-rod -> 4-wind-charges are all vanilla-accurate.

## Chapter summary
- Quests: 10 total, 3 EDIT, 7 CLEAN
- Accuracy bugs (WRONG ledger rows): 1
  - Ultimate Coil: emerald is NOT the Geode capstone gem - diamond is (chain ends `amethyst -> emerald -> diamond`). The word "capstone" is the error; emerald is correctly the Ultimate Coil ingredient.
- Highest-severity finding: Ultimate Coil's "Geode capstone gem" misnames the tier's capstone (diamond), and is internally inconsistent with the Elite Coil (which uses diamond one tier below). Factual fix, no recipe change.
- No em/en dashes, no unbalanced color codes, no broken escaping anywhere in the chapter. The two other EDITs are minor (1 stick vs "a couple sticks"; "Energy Cell" vs "cell").
