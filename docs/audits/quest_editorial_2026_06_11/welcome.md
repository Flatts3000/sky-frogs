# Audit: welcome ("Welcome to Sky Frogs")

Mod(s) referenced: Ex Deorum (crook, silkworm, crucible, barrel, iron hammer), Productive Frogs (spawnery, frog egg, frog net), Cobble Gen Galore (block_gen_stone), Simple Magnets (basicmagnet), Functional Storage (oak drawer reward), Sophisticated Backpacks, Squat Grow, FTB Ultimine. Generated chapter: no.

## Mechanic-claims ledger

| Quest | Claim (paraphrase) | Source checked (jar path / pack override) | Verdict |
|-------|--------------------|-------------------------------------------|---------|
| Frogs, Not Pickaxes | Resource Slime fed to its frog returns a Froglight loaded with that resource | core PF loop (design canon) | MATCHES |
| The Road to Iron | Cave Frog deals in iron/copper/gold/ores | PF Cave category; pack design canon | MATCHES |
| A Rain Barrel | Craft an Oak Barrel, leave in weather, it catches rain | exdeorum oak_barrel.json (3x3 planks+slab); barrel rain-fill is core ExDeorum | MATCHES |
| Strip the Leaves | Shears turn oak leaves into whole leaf blocks (crucible feedstock) | vanilla shears + exdeorum water_crucible/leaves.json | MATCHES |
| The Crucible | Oak Crucible steeps leaves into water, no heat; stone crucibles melt cobble to lava (heat) | exdeorum water_crucible/leaves.json (no heat), lava_crucible/cobblestone.json (heat) | MATCHES |
| Running Water | Two water sources one block apart make an infinite source | vanilla | MATCHES |
| A Crook | Four sticks make a Crook; crooking oak leaves yields saplings + occasional Silkworm | exdeorum crook.json (4 wooden rods), crook/silkworm.json (0.01 from leaves tag) | MATCHES |
| Silkworms | Set a silkworm loose on a leaf block; it infests the leaves around it | exdeorum silkworm entity (leaves -> infested_leaves) | MATCHES |
| String from Silk | "Break the infested leaves and they shed string" | exdeorum loot_table/blocks/infested_leaves.json = EMPTY entries; crook/string_roll_1.json + _2.json drop string by CROOKING fully-infested leaves (0.4 + 0.1) | **WRONG** -- VERIFY: VERIFIED. exdeorum-3.10.jar `data/exdeorum/loot_table/blocks/infested_leaves.json` pools[0].entries=[] (breaking drops nothing); `crook/string_roll_1.json` chance 0.4 + `string_roll_2.json` chance 0.1, both `block_predicate` infested_leaves state fully_infested=true, result minecraft:string. String comes from CROOKING fully-infested leaves. AFTER edit (crook fully-infested leaves) is correct -- apply. |
| A Bed of Your Own | 4 string -> wool; 3 wool + 3 planks -> bed | vanilla | MATCHES |
| Tools of the Trade | Wooden pickaxe = three planks, two sticks | vanilla | MATCHES |
| Cobblestone | Water + lava one block apart make cobble; Iron Hammer turns rock into other rock | vanilla cobblegen; exdeorum iron_hammer.json + hammer recipes | MATCHES |
| Sand | Iron Hammer pounds cobblestone -> gravel -> sand | exdeorum hammer/gravel.json (cobble->gravel), hammer/sand.json (gravel->sand) | MATCHES |
| Glass | Smelt sand into glass, charcoal as fuel | vanilla | MATCHES |
| Cobblestone Generator | Six smooth stone around two glass blocks builds a Stone Block Generator | cobblegengalore recipe/crafting/block_gen_stone.json (RRR/G_G/RRR; R=smooth_stone, G=glass) | MATCHES |
| A Dark Room | Cave Slimes spawn in dark; big ones need 3-tall headroom, 5x5 minimum | vanilla slime/dark-spawn behavior; pack adds cave_slime spawns | MATCHES (size advice plausible, runtime-tuned) |
| A Composter | Composter = seven wooden slabs in a U; yields bone meal | vanilla | MATCHES |
| The Spawnery | Spawnery = 5 cobblestone, 3 planks, bone meal in middle; fueled by slime ball; primed by the resource | PF spawnery.json (PPP/CMC/CCC); pack spawnery_primer/cave.json = cobblestone (replace:true) | MATCHES |
| Synthesize Life | Prime with cobblestone (Cave's primer); slime ball fuel; glass bottle -> "Bottle of Cave Frog Frogspawn" | pack cave primer = cobblestone OK; **item is "Bottle of Cave Frog Eggs"** per PF lang | MATCHES (mechanic) / **WRONG item name** -- VERIFY: VERIFIED. productivefrogs-1.20.0.jar lang `item.productivefrogs.frog_egg.cave` = "Bottle of Cave Frog Eggs". AFTER edit (Bottle of Cave Frog Eggs) is correct -- apply. |
| The Frog Net | Six string + a stick; catches a frog whole (species, Appetite/Bounty/Reach, name) | PF frog_net.json (SSS/S_S/_I_); PF lang frog_net stats Appetite/Bounty/Reach | MATCHES |
| Two Shortcuts | Squat Grow (sneak by sapling/crop to grow); FTB Ultimine (mass-break) | squatgrow + ftb-ultimine jars present | MATCHES |

## Per-quest findings

### Welcome to Sky Frogs (quest.01A8E068925B319F)
- Disposition: CLEAN

### Join the Pond (quest.111D15C0DE000001)
- Disposition: CLEAN

### Frogs, Not Pickaxes (quest.05BFA1537298A589)
- Disposition: EDIT
- Issues: Voice: subtitle "The whole pitch, in three words." is cute but the body is not three words; harmless, leave. Minor: "ender" as a resource name reads oddly mid-list. Optional tightening only - leaving as CLEAN-adjacent.
- Verdict: treat as CLEAN (no factual problem). No edit required.

### The Road to Iron (quest.378B93672C31CF5D)
- Disposition: CLEAN

### Wood to Stand On (quest.79D9A7438B1DD129)
- Disposition: CLEAN

### Two Shortcuts (quest.65F6A1B2C3D40001)
- Disposition: CLEAN
- Note: Squat Grow and FTB Ultimine both ship; keybind guidance ("Options -> Controls") accurate.

### A Rain Barrel (quest.21B2C3D4E5F60001)
- Disposition: CLEAN

### Strip the Leaves (quest.21B2C3D4E5F60011)
- Disposition: EDIT
- Issues: Voice/accuracy: subtitle "Saplings and sticks." describes leaf-decay drops, but this quest is about shearing leaves into whole blocks for the crucible - the subtitle points at the wrong payoff. Body is accurate.
- BEFORE:
  quest.21B2C3D4E5F60011.quest_subtitle: "Saplings and sticks."
- AFTER:
  quest.21B2C3D4E5F60011.quest_subtitle: "Leaves, whole."

### The Crucible (quest.21B2C3D4E5F60021)
- Disposition: EDIT
- Issues: Voice: subtitle "Melt blocks into fluid." overstates - the Oak Crucible steeps leaves cold (no melting); melting is the later stone-crucible lava path the body itself flags. Minor mismatch with own copy.
- BEFORE:
  quest.21B2C3D4E5F60021.quest_subtitle: "Melt blocks into fluid."
- AFTER:
  quest.21B2C3D4E5F60021.quest_subtitle: "Leaves into water."

### Running Water (quest.21B2C3D4E5F60031)
- Disposition: CLEAN

### A Crook (quest.32C3D4E5F6A10001)
- Disposition: CLEAN

### Silkworms (quest.32C3D4E5F6A10011)
- Disposition: CLEAN

### String from Silk (quest.32C3D4E5F6A10021)
- Disposition: EDIT
- Issues: **Factual (top priority): WRONG mechanic.** Body says "Break the infested leaves and they shed string." Breaking infested leaves drops NOTHING (exdeorum loot_table/blocks/infested_leaves.json has empty entries). String comes from CROOKING fully-infested leaves (crook/string_roll_1.json 40% + string_roll_2.json 10%). The player must crook the infested leaves, not break them. Also subtitle "No spiders required." is fine.
- BEFORE:
  quest.32C3D4E5F6A10021.quest_desc: ["Break the infested leaves and they shed &fstring&r - no spider required."
  ""
  "Here's a &eMagnet&r to vacuum it up while you work. You'll want more than four for what's next."]
- AFTER:
  quest.32C3D4E5F6A10021.quest_desc: ["Once your leaves are &efully infested&r, run the Crook back across them - now they shed &fstring&r instead of silkworms. No spider required."
  ""
  "Here's a &eMagnet&r to vacuum it up while you work. Toggle it on, then crook your way to more than four string for what's next."]

### A Bed of Your Own (quest.32C3D4E5F6A10031)
- Disposition: CLEAN

### Tools of the Trade (quest.43D4E5F6A1B20001)
- Disposition: CLEAN

### Cobblestone (quest.43D4E5F6A1B20011)
- Disposition: CLEAN

### Sand (quest.43D4E5F6A1B20021)
- Disposition: CLEAN

### Glass (quest.43D4E5F6A1B20031)
- Disposition: CLEAN

### Cobblestone Generator (quest.43D4E5F6A1B20041)
- Disposition: CLEAN
- Note: title says "Cobblestone Generator" but the block is the "Stone Block Generator" (and the body uses the correct name). The recipe makes stone, not cobblestone. Title is a thematic shorthand; the in-world block name appears correctly in the body. Borderline - flag only, no edit (the chapter-title convention may intend the generic "cobblegen" framing). If tightening: rename title to "Stone Generator".

### A Dark Room (quest.54E5F6A1B2C30001)
- Disposition: CLEAN

### A Composter (quest.54E5F6A1B2C30011)
- Disposition: CLEAN

### The Spawnery (quest.54E5F6A1B2C30021)
- Disposition: CLEAN
- Note: cobblestone-as-Cave-primer confirmed via pack override kubejs/data/productivefrogs/tags/item/spawnery_primer/cave.json (replace:true -> cobblestone). PF default primer is iron ingot; the pack override makes the quest copy correct.

### Synthesize Life (quest.54E5F6A1B2C30031)
- Disposition: EDIT
- Issues: Terminology: "Bottle of Cave Frog Frogspawn" does not match the in-game item name. PF lang item.productivefrogs.frog_egg.cave = "Bottle of Cave Frog Eggs". Player text must match the item. (Mechanic - cobblestone prime, slime-ball fuel, glass bottle - is correct.)
- BEFORE:
  quest.54E5F6A1B2C30031.quest_desc: ["&aPrime the Spawnery with cobblestone&r - that's the Cave frog's calling card - drop in a slime ball to burn, and seat a glass bottle."
  ""
  "Out comes a &eBottle of Cave Frog Frogspawn&r. Make &btwo&r: two frogs is a breeding pair, and a breeding pair is a farm that never runs dry."
  ""
  "That's the last thing you'll build by hand for a while. Tip them onto water and let the frogs take over."]
- AFTER:
  quest.54E5F6A1B2C30031.quest_desc: ["&aPrime the Spawnery with cobblestone&r - that's the Cave frog's calling card - drop in a slime ball to burn, and seat a glass bottle."
  ""
  "Out comes a &eBottle of Cave Frog Eggs&r. Make &btwo&r: two frogs is a breeding pair, and a breeding pair is a farm that never runs dry."
  ""
  "That's the last thing you'll build by hand for a while. Tip them onto water and let the frogs take over."]

### The Frog Net (quest.54E5F6A1B2C30041)
- Disposition: CLEAN

## Chapter summary
- Quests: 24 total, 4 EDIT, 20 CLEAN
- Accuracy bugs (WRONG ledger rows): 2
  1. **String from Silk** - body claims string comes from "breaking" infested leaves; it comes from CROOKING fully-infested leaves (breaking drops nothing). Highest-severity factual error.
  2. **Synthesize Life** - "Bottle of Cave Frog Frogspawn" should be "Bottle of Cave Frog Eggs" (in-game item name; terminology, not a mechanic break).
- Two subtitle-vs-body mismatches (Strip the Leaves, The Crucible) and one title shorthand note (Cobblestone Generator -> block is "Stone Block Generator").
- Highest-severity finding: String from Silk describes an invented "break the leaves for string" mechanic - the actual path is crooking fully-infested leaves; a new player following the text literally would break the leaves and get nothing.
