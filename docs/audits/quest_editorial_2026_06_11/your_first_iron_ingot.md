# Audit: your_first_iron_ingot ("Your First Iron Ingot")

Mod(s) referenced: Productive Frogs (productivefrogs-1.20.0.jar), vanilla Minecraft. Pack overrides: `pack/kubejs/server_scripts/iron_slime_bucket.js`, `catalyst_recipes.js`. Generated chapter: no.

## Mechanic-claims ledger
| Quest | Claim (paraphrase) | Source checked (jar path / pack override) | Verdict |
|-------|--------------------|-------------------------------------------|---------|
| A Place for Frogs | Frogs jump high and can clear a low wall / leave a void island; cap the pen with a roof or overhang | PF resource-frog entity behavior (frogs hop); design framing, not a recipe | MATCHES (plain behavioral claim, no invented mechanic) |
| A Place for Frogs | Drop water inside; that's where frogspawn goes | PF `frog_egg` placed on water spawns frogs (welcome chapter line 308/317 consistent) | MATCHES |
| Keep Them Close | A Lead clips to a frog and holds it in place | vanilla lead behavior | MATCHES |
| Keep Them Close | 4 string + 1 slime ball make 2 leads | vanilla `minecraft:lead` recipe (4 string + 1 slimeball -> 2 leads) | MATCHES |
| The Slime Milker | Slime Milker is planks, cobblestone, and a slime ball | `data/productivefrogs/recipe/slime_milker.json`: pattern PPP/CSC/CCC, P=planks tag, C=cobblestone, S=slime_ball | MATCHES |
| The Slime Milker | Drop a bucketed slime in the top, wait, it presses out a bucket of that slime's milk | PF Slime Milker reads `bucket_entity_data.Variant`, stamps matching `<variant>_slime_milk_bucket` (per-variant, v1.8+) | MATCHES |
| Iron Slime in a Bucket | PF normally primes an Iron Slime with an iron ingot; pack lets you craft it iron-free from a Cave frogspawn bottle + slime balls + string + bone meal + bucket | `iron_slime_bucket.js`: shaped SBS/TKT/SFS, S=slime_ball, B=bone_meal, T=string, F=`frog_egg[contained_category="cave"]`, K=bucket -> `slime_bucket[Variant=iron,Category=CAVE]` | MATCHES |
| Milk It | Milk a Bucket of Iron Slime in the Slime Milker -> Bucket of Iron Slime Milk | task item `productivefrogs:iron_slime_milk_bucket` (per-variant, correct for v1.8+); display "Bucket of Iron Slime Milk" | MATCHES |
| Milk It | Pour milk -> spawns Iron Slimes; source runs dry after a batch; milk caught slimes for refills | PF Slime Milk fluid spawns resource slimes; catalyst tooltip "More slime spawns before it runs dry" confirms placed sources deplete | MATCHES |
| Milk It | The Geode "Infinite Count Catalyst" makes a source "never run dry" | PF item `infinite_catalyst` displays **"Endless Catalyst"**, tooltip "Source never runs dry"; pack does NOT rename it (`catalyst_recipes.js` only re-recipes the Quantity catalyst) | WRONG - in-game item is "Endless Catalyst", not "Infinite Count Catalyst" -- VERIFY: VERIFIED. productivefrogs-1.20.0.jar lang `item.productivefrogs.infinite_catalyst` = "Endless Catalyst", tooltip.productivefrogs.catalyst.infinite = "Source never runs dry". catalyst_recipes.js only re-recipes the quantity catalyst (no rename). AFTER edit (Endless Catalyst) is correct -- apply. |
| Feed the Frog | Drop an Iron Slime near a Cave Frog; the frog eats it and leaves an Iron Froglight | PF resource-frog feed loop (slime fed -> Froglight drop); consistent with welcome/road chapters | MATCHES |
| Your First Iron Ingot | Smelt one Iron Froglight in a furnace -> a plain iron ingot | `data/productivefrogs/recipe/configurable_froglight_iron_to_iron_ingot.json`: smelting, ingredient froglight w/ slime_variant=iron -> `minecraft:iron_ingot` | MATCHES |
| Your First Iron Ingot | (task design) checks the smelted iron ingot, not the Froglight | chapter task `minecraft:iron_ingot` - the documented pack-wide froglight-check exception | MATCHES (by design, not a bug) |

## Per-quest findings

### A Place for Frogs (quest.6C1F0A2B3D4E5F61)
- Disposition: CLEAN

### Keep Them Close (quest.6C1F0A2B3D4E5F64)
- Disposition: CLEAN

### The Slime Milker (quest.6C1F0A2B3D4E5F67)
- Disposition: CLEAN
- (Note, not flagged: in-game the crafted bucket reads "Bucket of Iron Slime"; this quest doesn't name that item, so no change needed.)

### Iron Slime in a Bucket (quest.6C1F0A2B3D4E5F6A)
- VERIFY: VERIFIED (item exists) but the AFTER edit names the WRONG target. The audit's AFTER changes "Cave Frogspawn bottle" -> "Bottle of Cave Frog Frogspawn", but the real in-game item is **"Bottle of Cave Frog Eggs"** (productivefrogs-1.20.0.jar lang `item.productivefrogs.frog_egg.cave`). The welcome chapter audit (Synthesize Life) corrects to "Eggs"; this AFTER would re-introduce "Frogspawn" and clash. CHANGE the AFTER: use "Bottle of Cave Frog Eggs", not "Bottle of Cave Frog Frogspawn". (The "Bucket of Iron Slime" half of the AFTER is fine.) Note: the wider pack voice uses "frogspawn" generically for the egg-bottle (per road_to_geode audit, 29 lang uses) - if the maintainer keeps "frogspawn" as voice, that is a design call, but the literal ITEM NAME is "...Frog Eggs".
- Disposition: EDIT
- Issues: Terminology (minor): text calls the frogspawn item a "Cave Frogspawn bottle"; the pack's established name (welcome chapter) is "Bottle of Cave Frog Frogspawn" (PF's raw item is "Bottle of Cave Frog Eggs"). Align to the pack convention for consistency. The crafted output is described as "Iron Slime in a Bucket" (matches the quest title and is a fine descriptive label; the in-game item reads "Bucket of Iron Slime" but renaming the prose here would clash with the title - left as-is).
- BEFORE:
  ```
  quest.6C1F0A2B3D4E5F6A.quest_desc: [
  	"Productive Frogs wants an iron ingot to make an Iron Slime - and you don't have one. So we cheat, exactly once."
  	""
  	"Combine a &eCave Frogspawn&r bottle, &aslime balls&r, &fstring&r, &6bone meal&r, and that spare &fbucket&r into an &bIron Slime in a Bucket&r. It's the only iron-free Iron Slime you'll ever make."
  	""
  	"This is the seed. Every scrap of iron from here on grows out of it."
  ]
  ```
- AFTER:
  ```
  quest.6C1F0A2B3D4E5F6A.quest_desc: [
  	"Productive Frogs wants an iron ingot to make an Iron Slime - and you don't have one. So we cheat, exactly once."
  	""
  	"Combine a &eBottle of Cave Frog Frogspawn&r, &aslime balls&r, &fstring&r, &6bone meal&r, and that spare &fbucket&r into a &bBucket of Iron Slime&r. It's the only iron-free Iron Slime you'll ever make."
  	""
  	"This is the seed. Every scrap of iron from here on grows out of it."
  ]
  ```

### Milk It (quest.6C1F0A2B3D4E5F6D)
- Disposition: EDIT
- Issues: Factual accuracy / Terminology (HIGH): names the catalyst "Infinite Count Catalyst" and "Infinite Count" - no such item exists in-game. PF's `infinite_catalyst` displays as **"Endless Catalyst"** (tooltip "Source never runs dry"). A new player reading "Infinite Count Catalyst" won't find it in the recipe book or at the Geode gate. Use the in-game name. (Also tightened the catalyst paragraph - "change the game", "That's the real automation unlock", "untouched", "don't fret the depletion now; the permanent fix is a tier away" is padded restatement of one idea.)
- BEFORE:
  ```
  quest.6C1F0A2B3D4E5F6D.quest_desc: [
  	"Drop your &bIron Slime in a Bucket&r into the top slot of the Slime Milker and give it a few seconds - it presses the slime down into a bucket of &bIron Slime Milk&r."
  	""
  	"Pour that milk out and it spawns &aIron Slimes&r, but the source isn't bottomless - it runs dry after a batch. Milk the slimes you catch for fresh buckets and the cycle feeds itself."
  	""
  	"That refill loop is your answer until the &2Geode&r tier, where &bSlime Milk catalysts&r change the game: the &bInfinite Count Catalyst&r makes a source &enever run dry&r. That's the real automation unlock - drop one in a pool and it pours forever, untouched. So don't fret the depletion now; the permanent fix is a tier away."
  	""
  	"Take a &eDiamond Stick&r for your trouble - it'll make building out your base a good deal faster."
  ]
  ```
- AFTER:
  ```
  quest.6C1F0A2B3D4E5F6D.quest_desc: [
  	"Drop your &bBucket of Iron Slime&r into the top slot of the Slime Milker and give it a few seconds - it presses the slime down into a bucket of &bIron Slime Milk&r."
  	""
  	"Pour that milk out and it spawns &aIron Slimes&r, but the source isn't bottomless - it runs dry after a batch. Milk the slimes you catch for fresh buckets and the cycle feeds itself."
  	""
  	"That refill loop carries you to the &2Geode&r tier, where &bSlime Milk catalysts&r arrive. Drop an &bEndless Catalyst&r into a milk pool and it &enever runs dry&r - the real depletion fix is one tier away, so don't sweat it now."
  	""
  	"Take a &eDiamond Stick&r for your trouble - it'll make building out your base a good deal faster."
  ]
  ```

### Feed the Frog (quest.6C1F0A2B3D4E5F70)
- Disposition: CLEAN

### Your First Iron Ingot (quest.6C1F0A2B3D4E5F73)
- Disposition: CLEAN
- (Confirmed: the task checks `minecraft:iron_ingot`, the deliberate pack-wide exception to the froglight-check law. Not a bug - verified against the chapter task and PF smelting recipe.)

## Chapter summary
- Quests: 7 total, 2 EDIT, 5 CLEAN
- Accuracy bugs (WRONG ledger rows): 1 - "Milk It" calls the catalyst "Infinite Count Catalyst"; the in-game PF item is "Endless Catalyst" (`infinite_catalyst`, tooltip "Source never runs dry"). The pack does not rename it, so the player text must use "Endless Catalyst".
- Highest-severity finding: the "Endless Catalyst" / "Infinite Count Catalyst" name mismatch in "Milk It" - this is a signpost quest specifically added (per backlog v0.10.1) to un-stick players on milk depletion, so pointing them at a non-existent item name undercuts the quest's whole purpose.
