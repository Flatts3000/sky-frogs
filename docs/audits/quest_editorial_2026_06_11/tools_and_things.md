# Audit: tools_and_things ("Tools & Things")

Mod(s) referenced: Just Dire Things (Direwolf20), Productive Frogs (Slime Churn), Building Gadgets 2, Industrial Foregoing (forward reference: Dissolution Chamber latex intake). Generated chapter: no.

## Mechanic-claims ledger

| Quest | Claim (paraphrase) | Source checked (jar path / pack override) | Verdict |
|-------|--------------------|-------------------------------------------|---------|
| First Goo | Primogel Goo crafts from clay balls, mycelium, rotten flesh, sugar | `justdirethings data/justdirethings/recipe/gooblock_tier1.json` | WRONG - recipe is `clay_ball` + `dirt` + `rotten_flesh` + `sugar` (pattern `csc/fdf/csc`). Center filler is **dirt**, not mycelium. No mycelium anywhere; the "comes off your Bog mycelium frog" tie-in is fabricated. VERIFY: VERIFIED - cracked gooblock_tier1.json: key c=clay_ball, d=dirt, f=rotten_flesh, s=sugar; pattern csc/fdf/csc -> 4 clay, 1 dirt center, 2 rotten flesh, 2 sugar. No mycelium. No PF datapack override for this recipe. The audit's dirt correction is correct. |
| First Goo | Item named "Primogel Goo Block" | `justdirethings assets/.../lang/en_us.json` → `"block.justdirethings.gooblock_tier1": "Primogel Goo"` | WRONG name - in-game name is **"Primogel Goo"** (no "Block"). VERIFY: VERIFIED - lang `block.justdirethings.gooblock_tier1` = "Primogel Goo" exactly. No "Block". |
| First Goo | "stack blocks against its sides - it slowly spreads into each one, transmuting it into a raw resource" | goospread recipes in `justdirethings data/.../recipe/*-goospread.json` | MISLEADING - goospread only converts **specific full metal/coal blocks** to ores (tier-1 gooblock: `iron_block`->raw ferricore, `coal_block`->raw coal). It does not transmute arbitrary blocks. VERIFY: VERIFIED - tier-1 goospread recipes (tierRequirement:1): iron_block->raw_ferricore_ore and coal_block (+ charcoal-block tag)->raw_coal_t1_ore, 2400t each. Only specific metal/coal blocks; not arbitrary. (Charcoal block is an extra tier-1 input the audit omits, but doesn't change the finding.) |
| The Slime Churn | Churn loads a Slime Milk bucket + empties, fills empties with that variant's slime on the same schedule/budget/catalysts as a placed milk pool | PF JEI `assets/productivefrogs/lang/en_us.json` `productivefrogs.jei.slime_churn.info` ("The Milker's inverse... same schedule and budget... catalysts included") | MATCHES |
| The Slime Churn | Output item "Slime in a Bucket" | PF lang `"item.productivefrogs.slime_bucket": "Bucket of Slime"` / `..._bucket.<variant>` "Bucket of <Variant> Slime" | WRONG name - item is **"Bucket of [Variant] Slime"**, not "Slime in a Bucket." VERIFY: VERIFIED - PF lang confirms `item.productivefrogs.slime_bucket` = "Bucket of Slime" and per-variant keys "Bucket of [Variant] Slime" (e.g. "Bucket of Bog Slime"). "Slime in a Bucket" is not the item name. |
| Ferricore Ingot | Iron blocks stacked against Primogel Goo spread into each, becoming Raw Ferricore Ore over ~2 min; mine + smelt to Ferricore Ingot | `raw_ferricore_ore-goospread.json` (input `minecraft:iron_block` -> `raw_ferricore_ore`, craftingDuration 2400, tier 1) | MATCHES (2400t = 2 min; iron_block is the correct input) |
| Ferricore Ingot | Subtitle "The starter alloy" | same; body says "JDT's iron"; ferricore is a base metal smelted from one ore | WRONG - ferricore is a base metal, not an alloy. Self-contradicts the body ("JDT's iron"). VERIFY: VERIFIED - ferricore ingot smelts from raw_ferricore_ore (one ore, goospread from iron_block); it is JDT's tier-1 base metal, not an alloy (JDT alloys like blazegold/eclipsealloy are the multi-input ones). Subtitle fix to "JDT's base metal" is correct. |
| Vacuum the Floor | Item Collector "takes a diamond and an ender pearl" | `justdirethings data/.../recipe/itemcollector.json` (pattern ` d /heh/fff`: 1 diamond, **2 ender pearls**, 2 hoppers, 3 ferricore ingots) | WRONG - undercounts (2 ender pearls) and omits hoppers + ferricore. VERIFY: VERIFIED - cracked itemcollector.json: pattern " d "/"heh"/"fff", d=diamond(1), h=hopper(2), e=ender_pearl(2), f=ferricore_ingot(3). Exactly 1 diamond + 2 ender pearls + 2 hoppers + 3 ferricore. No PF datapack shortcut. |
| Vacuum the Floor | Item Collector vacuums items in a radius | `justdirethings:itemcollector` (in-game "Item Collector"); chapter task/icon = itemcollector | MATCHES (general behavior correct) |
| Exchanging Gadget | Mekanism hands you the basic Building Gadget as the Enrichment Chamber reward | `chapters/mekanism.snbt` quest 6ECA15000000001A rewards `buildinggadgets2:gadget_building` | MATCHES |
| Exchanging Gadget | Exchanging Gadget swaps one block for another in place | BG2 lang `"item.buildinggadgets2.gadget_exchanging": "Exchanging Gadget"` | MATCHES |
| Copy, Paste | Copy/Paste Gadget captures a shape to a Template, stamps it anywhere | BG2 lang `gadget_copy_paste` = "Copy Paste Gadget", `template` = "Template" | MATCHES (name is "Copy Paste Gadget"; "Copy/Paste" is acceptable friendly form) |
| Copy, Paste | "The Template is its companion; the gadget loads it automatically" - reward is Template Manager | chapter reward `buildinggadgets2:template_manager` = "Template Manager" | PARTIAL - reward is the **Template Manager** (block for naming/saving templates), not a Template item; the prose conflates them. |
| Fluid Collector | Reaches into the block in front, slurps a fluid source (water/lava/latex) into its tank | `justdirethings:fluidcollectort1` = "Simple Fluid Collector"; recipe exists | MATCHES (behavior); name is "Simple Fluid Collector" |
| Fluid Collector | "Pipe it into your Dissolution Chamber's latex intake" | pack override `kubejs/server_scripts/dissolution_slime_recipes.js` (Dissolution Chamber recipes consume `industrialforegoing:latex` 100 mb) | MATCHES - pack's Dissolution Chamber slime recipes really take latex. |
| Fluid Placer | Pours from its tank into the block in front; infinite-water spread / lava cobblegen | `justdirethings:fluidplacert1` = "Simple Fluid Placer" | MATCHES (behavior); name is "Simple Fluid Placer" |

## Per-quest findings

### First Goo (quest.1F00000000000002)
- Disposition: EDIT
- Issues:
  - Factual: recipe ingredient WRONG - claims "mycelium," actual is **dirt** (clay_ball/dirt/rotten_flesh/sugar). The "Mycelium comes off your Bog mycelium frog" sentence is entirely fabricated and must go.
  - Terminology: "Primogel Goo Block" -> in-game name is "Primogel Goo."
  - Factual/clarity: "stack blocks against its sides - it slowly spreads into each one, transmuting it into a raw resource" implies any block works; goospread only converts specific metal/coal blocks. Should say plainly that you stack the right block (iron/coal) next to it.
  - Voice: tighten; drop "tier-1 entry into JDT's farming and machines" jargon.
- BEFORE:
  - `quest.1F00000000000002.quest_desc: [`
  - `	"Just Dire Things runs on &eGoo&r. Mix &fclay balls&r, &fmycelium&r, &frotten flesh&r, and &fsugar&r into a &ePrimogel Goo Block&r - the tier-1 entry into JDT's farming and machines. Mycelium comes off your Bog mycelium frog."`
  - `	""`
  - `	"Place the goo down and stack blocks against its sides - it slowly spreads into each one, transmuting it into a raw resource. Direwolf20's mod is opening up."`
  - `]`
  - `quest.1F00000000000002.quest_subtitle: "Just Dire Things begins."`
  - `quest.1F00000000000002.title: "First Goo"`
- AFTER:
  - `quest.1F00000000000002.quest_desc: [`
  - `	"Just Dire Things runs on &eGoo&r. Craft &fclay balls&r, &fdirt&r, &frotten flesh&r, and &fsugar&r into a block of &ePrimogel Goo&r - your way into Direwolf20's machines."`
  - `	""`
  - `	"Place the goo, then set a &firon block&r or &fcoal block&r right next to it. The goo slowly creeps into that block and turns it into a raw ore. Mine the ore and you're off."`
  - `]`
  - `quest.1F00000000000002.quest_subtitle: "Just Dire Things begins."`
  - `quest.1F00000000000002.title: "First Goo"`

### The Slime Churn (quest.1F00000000000020)
- Disposition: EDIT
- Issues:
  - Terminology: "Slime in a Bucket" is not the item name; it's "Bucket of [Variant] Slime."
  - Voice: one long run-on sentence; trim the triple "same cadence, same per-bucket budget, same catalysts."
- BEFORE:
  - `quest.1F00000000000020.quest_desc: [`
  - `	"Tired of pouring out &eSlime Milk&r and chasing down every slime it spawns? The &eSlime Churn&r does the catching for you. Load a bucket of any variant's &eSlime Milk&r and a stack of empties, and it fills them with that variant's &bSlime in a Bucket&r - same cadence, same per-bucket budget, same catalysts as a placed milk pool, with no slime to chase and no entity at all."`
  - `	""`
  - `	"Craft a &eSlime Churn&r."`
  - `]`
- AFTER:
  - `quest.1F00000000000020.quest_desc: [`
  - `	"Tired of pouring out &eSlime Milk&r and chasing down every slime it spawns? The &eSlime Churn&r catches them for you. Load a bucket of any variant's &eSlime Milk&r and a stack of empties, and it fills each one with that variant's &bBucket of Slime&r - same rate, same budget, same catalysts as a placed milk pool, but with no slimes to chase."`
  - `	""`
  - `	"Craft a &eSlime Churn&r."`
  - `]`

### Ferricore Ingot (quest.1F00000000000005)
- Disposition: EDIT
- Issues:
  - Factual: subtitle "The starter alloy" is wrong - ferricore is a base metal (the body correctly calls it "JDT's iron"). Not an alloy.
  - Voice: body mechanic is accurate; keep, light trim.
- BEFORE:
  - `quest.1F00000000000005.quest_desc: [`
  - `	"&fFerricore&r is JDT's iron - the metal every Simple machine downstream needs. Stack &firon blocks&r against your &ePrimogel Goo&r and it spreads into each one over a couple of minutes, turning it into &fRaw Ferricore Ore&r. Mine the ore and smelt the raw ferricore to a &bFerricore Ingot&r."`
  - `	""`
  - `	"Stock up. Everything Direwolf20 makes from here takes ferricore."`
  - `]`
  - `quest.1F00000000000005.quest_subtitle: "The starter alloy."`
- AFTER:
  - `quest.1F00000000000005.quest_desc: [`
  - `	"&fFerricore&r is JDT's iron - the metal every Simple machine downstream needs. Set &firon blocks&r against your &ePrimogel Goo&r and it creeps into each one over a couple of minutes, turning it into &fRaw Ferricore Ore&r. Mine the ore and smelt it to a &bFerricore Ingot&r."`
  - `	""`
  - `	"Stock up. Everything Direwolf20 makes from here takes ferricore."`
  - `]`
  - `quest.1F00000000000005.quest_subtitle: "JDT's base metal."`

### Fluid Collector (quest.1F00000000000017)
- Disposition: CLEAN
- Behavior and the Dissolution-Chamber-latex forward reference both ground-truth correctly (pack's dissolution recipes consume `industrialforegoing:latex`). In-game name is "Simple Fluid Collector"; the quest's friendly "Fluid Collector" is acceptable. No edit required.

### Fluid Placer (quest.1F0000000000001A)
- Disposition: CLEAN
- Behavior correct; "Fluid Placer" friendly name acceptable for "Simple Fluid Placer." No edit required.

### Vacuum the Floor (quest.1F0000000000000E)
- Disposition: EDIT
- Issues:
  - Factual: "takes a diamond and an ender pearl" undercounts and omits ingredients. Real recipe: 1 diamond, **2 ender pearls**, 2 hoppers, 3 ferricore ingots.
  - Voice: keep the enderman/dark-room flavor (still true: ender pearls needed) but fix the count.
- BEFORE:
  - `quest.1F0000000000000E.quest_desc: [`
  - `	"Done chasing dropped &bFroglights&r across the platform? An &eItem Collector&r vacuums up everything in a radius - Froglights, slimeballs, anything that hits the floor."`
  - `	""`
  - `	"Sink one into your habitat floor and stop bending over. The Item Collector takes a diamond and an &fender pearl&r, so it's worth picking up after you've farmed a few enderman in the dark room."`
  - `	""`
  - `	"Claim your reward."`
  - `]`
- AFTER:
  - `quest.1F0000000000000E.quest_desc: [`
  - `	"Done chasing dropped &bFroglights&r across the platform? An &eItem Collector&r vacuums up everything in a radius - Froglights, slimeballs, anything that hits the floor."`
  - `	""`
  - `	"Sink one into your habitat floor and stop bending over. It takes a diamond, two &fender pearls&r, hoppers, and ferricore - so farm a few enderman in the dark room first."`
  - `	""`
  - `	"Claim your reward."`
  - `]`

### Exchanging Gadget (quest.1F00000000000011)
- Disposition: CLEAN
- "Exchanging Gadget" name correct; Mekanism Enrichment-Chamber-gives-Building-Gadget cross-reference verified against `chapters/mekanism.snbt`. No edit required.

### Copy, Paste (quest.1F00000000000014)
- Disposition: EDIT
- Issues:
  - Factual/clarity: the quest's reward is the **Template Manager** (a block for saving/naming templates), but the prose says "The Template is its companion" - it conflates the Template item with the Template Manager block. The reward should be named.
  - Terminology: in-game name is "Copy Paste Gadget"; "Copy/Paste Gadget" is acceptable friendly form (no change needed there).
- BEFORE:
  - `quest.1F00000000000014.quest_desc: [`
  - `	"The &eCopy/Paste Gadget&r captures a shape into a &bTemplate&r and stamps it anywhere - build one frog habitat, paste it ten times, turn one corner of the platform into a whole pond."`
  - `	""`
  - `	"The &bTemplate&r is its companion; the gadget loads it automatically."`
  - `]`
- AFTER:
  - `quest.1F00000000000014.quest_desc: [`
  - `	"The &eCopy/Paste Gadget&r captures a shape into a &bTemplate&r and stamps it anywhere - build one frog habitat, paste it ten times, turn one corner of the platform into a whole pond."`
  - `	""`
  - `	"Your reward, the &bTemplate Manager&r, lets you name and save those templates to reuse later."`
  - `]`

## Chapter summary
- Quests: 8 total, 5 EDIT, 3 CLEAN
- Accuracy bugs (WRONG ledger rows): 6
  1. First Goo - gooblock_tier1 ingredient is **dirt**, not mycelium (the Bog-mycelium-frog tie-in is fabricated).
  2. First Goo - item is "Primogel Goo," not "Primogel Goo Block."
  3. First Goo - goospread converts only specific metal/coal blocks (iron/coal at tier 1), not "any block stacked against it."
  4. Slime Churn - output item is "Bucket of [Variant] Slime," not "Slime in a Bucket."
  5. Ferricore Ingot - subtitle "The starter alloy" is wrong; ferricore is a base metal (body says "JDT's iron").
  6. Vacuum the Floor - Item Collector recipe is 1 diamond + 2 ender pearls + 2 hoppers + 3 ferricore, not "a diamond and an ender pearl."
- Highest-severity finding: "First Goo" claims the Primogel Goo recipe needs **mycelium from the Bog mycelium frog** - it needs dirt; the entire mycelium-frog sentence is an invented mechanic that would send players hunting for the wrong ingredient. (This is the issue's worked-example bug; confirmed: the false "seed the soil" framing is replaced here with the real goospread-into-iron/coal-block behavior, and the gooblock recipe corrected to dirt.)
