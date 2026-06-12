# Audit: road_to_geode ("The Road to Geode")

Mod(s) referenced: Productive Frogs (`productivefrogs-1.20.0.jar`), Functional Storage (reward only). Generated chapter: no.

## Mechanic-claims ledger
| Quest | Claim (paraphrase) | Source checked (jar path / pack override) | Verdict |
|-------|--------------------|-------------------------------------------|---------|
| The Road to Geode | Spawnery prime = redstone for Geode (not the amethyst-shard default) | Pack override `kubejs/data/productivefrogs/tags/item/spawnery_primer/geode.json` → `{replace:true, values:["minecraft:redstone"]}` (jar default is `minecraft:amethyst_shard`) | MATCHES (pack override is the truth) |
| The Road to Geode | Spawnery fuel = a slime ball; output = Geode eggs bottle | PF lang `productivefrogs.jei.spawnery.info`: "fueled by slime balls (one ball per bottle)... a species primer... primes that species' eggs" | MATCHES |
| The Road to Geode | "tip it onto water for Geode frogs" | PF frogspawn-bottle mechanic (pour on water → tadpoles); consistent with Cave welcome chapter | MATCHES |
| A Lapis Slime in a Bucket | Craft = redstone Slime Milk + 4 gravel + 3 sweetslime + Geode frogspawn bottle → Lapis Slime in a Bucket | Pack `kubejs/server_scripts/geode_slime_chain.js` step `['redstone','lapis']`: `redstone_slime_milk_bucket` + 4×`gravel` + 3×`sweetslime` + geode `frog_egg` → lapis slime_bucket | MATCHES |
| A Lapis Slime in a Bucket | "threads straight off the Cave's last resource" (redstone = Cave capstone) | `cave_slime_chain.js` (redstone is the chain capstone) + `geode_slime_chain.js` comment | MATCHES |
| A Bucket of Lapis Slime Milk | Slime Milker converts a Lapis Slime in a Bucket → Lapis Slime Milk | PF lang `productivefrogs.jei.slime_milker.info`: "Place a Slime Bucket containing a variant Resource Slime... after 100 ticks, it converts to the matching Slime Milk bucket" | MATCHES |
| A Bucket of Lapis Slime Milk | "Pour it out and Lapis Slimes spawn" | PF lang `productivefrogs.jei.slime_milk.info`: "Place in the world to create a Slime Milk source block. Periodically spawns a [variant slime]" | MATCHES |
| First Lapis | Geode frog eats Lapis Slimes, drops a Lapis Froglight | PF lang `productivefrogs.jei.variant_slime.info`: "Killed by a [frog], drops a Froglight stamped with this variant" | MATCHES |
| First Lapis | Smelt Lapis Froglight → lapis lazuli | PF recipe `data/productivefrogs/recipe/configurable_froglight_lapis_to_lapis_lazuli.json` (smelting, slime_variant lapis → `minecraft:lapis_lazuli`) | MATCHES |
| First Lapis | Reward = Compacting Drawer | Chapter task reward `functionalstorage:compacting_drawer`; FS lang `block.functionalstorage.compacting_drawer` = "Compacting Drawer" | MATCHES |
| First Lapis | Next chapter's gems = amethyst, emerald, diamond | `geode_slime_chain.js` chain (lapis→tuff→calcite→amethyst→emerald→diamond; amethyst/emerald/diamond are the gems) | MATCHES |

No WRONG rows. Every mechanic claim ground-truthed clean against the pack override or the PF jar.

VERIFY (the one claim that looks wrong on the surface - "prime with redstone" vs PF's amethyst default): VERIFIED CLEAN. PF jar `data/productivefrogs/tags/item/spawnery_primer/geode.json` = `{replace:false, amethyst_shard}`; pack override `kubejs/data/productivefrogs/tags/item/spawnery_primer/geode.json` = `{replace:true, redstone}`. The override wins, so "prime with redstone" is correct. No edit needed -- the chapter is accurate; no accuracy finding to apply.

## Per-quest findings

### The Road to Geode (quest.60ADE60000000002)
- Disposition: CLEAN
- Mechanics verified (redstone primer via pack override, slime-ball fuel, pour-on-water). Color runs `&c…&r`/`&d…&r` balanced. No non-ASCII. "Frogspawn" is the pack-wide term for the egg bottle (29 uses across the lang file, established in the Cave welcome chapter the player has already seen) - intentional voice, not flagged. Glass-bottle input is omitted, but the Cave-tier text frames the Spawnery identically ("draws frogspawn into a bottle"); the player already learned the machine. Voice is tight and factual.

### A Lapis Slime in a Bucket (quest.60ADE6000000000B)
- Disposition: CLEAN
- Recipe in prose (redstone Slime Milk + 4 gravel + 3 sweetslime + Geode frogspawn bottle) matches `geode_slime_chain.js` exactly. Task item is the GEODE/lapis slime_bucket, which the recipe outputs. "Cave's last resource" framing correct. Codes balanced, ASCII only.

### A Bucket of Lapis Slime Milk (quest.60ADE60000000005)
- Disposition: CLEAN
- Milker conversion and pour-to-spawn both match PF JEI mechanic text. Task item `lapis_slime_milk_bucket` matches prose. Names exact ("Slime Milker", "Lapis Slime Milk"). Codes `&b/&e/&9 … &r` balanced.

### First Lapis (quest.60ADE60000000008)
- Disposition: CLEAN
- Froglight smelt → lapis lazuli verified against the smelting recipe. Task requires the Lapis Froglight (configurable_froglight + slime_variant lapis); prose matches. "Froglight" used throughout (never "Configurable Froglight"). Forward-reference to amethyst/emerald/diamond is accurate. Compacting Drawer reward name correct. Codes balanced, ASCII only. Line 5 ("And a Compacting Drawer…") is a sentence fragment but reads fine as a reward call-out; not worth an edit.

## Chapter summary
- Quests: 4 total, 0 EDIT, 4 CLEAN
- Accuracy bugs (WRONG ledger rows): 0
- Highest-severity finding: None. The one claim that looks wrong on the surface - "prime it with redstone" vs PF's amethyst-shard Geode default - is correct because the pack ships a `replace:true` primer-tag override (`spawnery_primer/geode.json`) swapping Geode to redstone. The whole chapter is accurate and the voice already hits the factual-not-verbose target.
