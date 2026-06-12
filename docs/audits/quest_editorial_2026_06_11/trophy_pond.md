# Audit: trophy_pond ("Trophy Pond")

Mod(s) referenced: Productive Frogs (boss catalysts, boss Slime Milk, Froglight Cleaver), vanilla Minecraft (Wither, End Crystal/dragon respawn, Dragon Egg/Breath). Generated chapter: no.

Ground-truth sources: `productivefrogs-1.20.0.jar` recipe JSONs + decompiled `FroglightWeaponHandler.class` and `SlimeMilkSourceBlock.class`; pack override `pack/kubejs/server_scripts/catalyst_recipes.js` (only touches the Quantity *milk* catalyst, NOT the boss catalysts) and `dissolution_slime_recipes.js` (self-keyed boss rows, lines 184-187).

## Mechanic-claims ledger
| Quest | Claim (paraphrase) | Source checked (jar path / pack override) | Verdict |
|-------|--------------------|-------------------------------------------|---------|
| Skull Harvest | "Eight soul sand around a skull makes one WSS Catalyst" | recipe/wither_skeleton_skull_catalyst.json (pattern SSS/SKS/SSS, S=soul_sand, K=wither_skeleton_skull) | MATCHES |
| Skull Harvest | "craft six [catalysts]... seal a catalyst against each of its six faces" | SlimeMilkSourceBlock.class: "needs 6 catalyst faces", `catalystFaceCount`, `isFaceSturdy`; task requires count:6 of WSS catalyst | MATCHES |
| Skull Harvest | "wither skeletons drop skulls" at the fortress | vanilla behavior | MATCHES |
| Skull Harvest | "Mouse over the milk - Jade shows the face count" | ProductiveFrogsJadePlugin$MilkSourceProvider.class present | MATCHES |
| The Withering | "Three skulls and four soul sand summon the Wither" | vanilla Wither summon | MATCHES |
| The Withering | "eight obsidian around each makes the six Nether Star Catalysts" | recipe/nether_star_catalyst.json (OOO/OSO/OOO, O=obsidian, S=nether_star); task count:6 | MATCHES |
| A Clutch of Eggs | "Four End Crystals (ghast tears, glass, Eye of Ender) on the portal rim respawn the dragon; kill drops an egg every time" | vanilla End Crystal recipe (7 glass + 1 ghast_tear + 1 eye_of_ender) + vanilla respawn; no pack override found | MATCHES |
| A Clutch of Eggs | "End stone bricks around each: six Dragon Egg Catalysts" | recipe/dragon_egg_catalyst.json (EEE/EDE/EEE, E=end_stone_bricks, D=dragon_egg); task count:6 | MATCHES |
| Breath of Fresh End | "wrap purpur around each: six Dragon Breath Catalysts" | recipe/dragon_breath_catalyst.json (PPP/PBP/PPP, P=purpur_block, B=dragon_breath); task count:6 | MATCHES |
| Breath of Fresh End | "catch dragon breath in glass bottles" | vanilla | MATCHES |
| Froglight Cleaver | "two Nether Star Froglights and a Dragon Egg Froglight, wrapped in Dragon's Breath" | recipe/froglight_cleaver.json (BNB/BNB/BDB; N=nether_star froglight x2, D=dragon_egg froglight x1, B=dragon_breath x6) | MATCHES |
| Froglight Cleaver | "drops a Resource Slime's Froglight when it lands the kill; Looting raises the yield; brewed slime's effect carries onto the Froglight" | FroglightWeaponHandler.class: `onSlimeKilled` -> `lootingLevel`/Enchantments.LOOTING, `getActiveEffects`/`StoredEffect`/`buildFroglight` | MATCHES |
| Froglight Cleaver | "hits harder than netherite, shrugs off fire" | item attributes set in code (FroglightWeaponHandler/item registration); not string-confirmable from class constant pool | UNVERIFIABLE (plausible; consistent with an endgame weapon, no contradicting evidence) |
| | | | VERIFY: UNVERIFIABLE-CONFIRMED - cleaver is registered via `FroglightWeaponHandler` (no dedicated item class); javap found no `FIRE_RESISTANT`/Tiers/attack_damage string constants exposing the values. Not a false positive; consistent with design, nothing contradicts. No edit needed. |
| Do Not Touch / multiple | boss Slime Milk is toxic; standing in it applies the Wither; sealing all 6 faces contains it so it spawns slimes safely | SlimeMilkSourceBlock.class has `entityInside` applying an effect via DeferredHolder + the 6-face containment gate ("paused, altar incomplete (needs 6 catalyst faces)"). The effect Holder is registry-resolved, so the *specific* "Wither" identity is not a literal string in the class. | UNVERIFIABLE-AT-STRING-LEVEL (containment + entityInside-effect confirmed; "Wither" specifically is a design-doc claim, consistent, not contradicted) |
| | | | VERIFY: UNVERIFIABLE-CONFIRMED - javap of `SlimeMilkSourceBlock.entityInside` calls `LiquidBlock.entityInside`; no `MobEffects.WITHER` static found anywhere in PF classes (registry/Holder-resolved). "Wither" is the pack's design claim, not jar-confirmable, not contradicted. No edit needed. |

## Per-quest findings

### Do Not Touch the Milk (quest.7807000000000029)
- Disposition: CLEAN
- Strong warning/primer quest. Accurate to the containment mechanic (6 sealed faces -> safe slime spawner). "Wither" effect is the only soft spot (see ledger), but it's the pack's stated design and not contradicted by the jar. Color codes balanced, no dashes, voice on-target.

### Skull Harvest (quest.7807000000000002)
- Disposition: CLEAN
- Recipe (8 soul sand + skull), count (craft six), face-sealing, Jade readout, and fortress drop all ground-truthed and correct. Good factual-but-warm voice. The "(The jetpack helps. The Mace helps more.)" aside is flavor but earns its keep (it tells the player how to fight at the fortress).

### Wither Skeleton Skull (quest.7807000000000005)
- Disposition: CLEAN
- Task is the WSS Froglight (strict slime_variant component) - prose "Turn in the Wither Skeleton Skull Froglight" matches. "Froglight" terminology correct. Clean.

### The Withering (quest.7807000000000008)
- Disposition: CLEAN
- Wither summon cost (3 skulls + 4 soul sand) and the obsidian catalyst (8 obsidian, craft six) are correct. Note: the desc is a single dense block (one paragraph, no blank-line break) where the sibling quests use a 2-part structure - acceptable, the quest is short. No edit needed.

### Nether Star (quest.780700000000000B)
- Disposition: CLEAN
- Task is the Nether Star Froglight (strict component); prose matches. "the rarest drop in the game" is fair flavor for a nether star. Clean.

### A Clutch of Eggs (quest.780700000000000E)
- Disposition: CLEAN
- The "vanilla one-egg-per-world repealed" framing is accurate to the pack premise (respawn-and-reslay yields an egg each time). End Crystal ingredients listed correctly; end-stone-brick catalyst (craft six) correct. Clean.

### Dragon Egg (quest.7807000000000011)
- Disposition: CLEAN
- Task is the Dragon Egg Froglight (strict component); prose matches. Containment framing accurate. Clean.

### Breath of Fresh End (quest.7807000000000014)
- Disposition: CLEAN
- Glass-bottle catch + purpur catalyst (craft six) correct. "CPR for dragons" subtitle is playful and fits. Clean.

### Dragon Breath (quest.7807000000000017)
- Disposition: CLEAN
- Task is the Dragon Breath Froglight (strict component); prose matches. "Lingering potions forever" correctly reflects dragon's-breath use. Clean.

### The Froglight Cleaver (quest.780700000000001A)
- Disposition: CLEAN
- The headline mechanic (drops the killed Resource Slime's Froglight, Looting scales yield, brewed effect carries onto the Froglight) is fully confirmed in FroglightWeaponHandler.class. Recipe (2 Nether Star Froglights + 1 Dragon Egg Froglight + Dragon's Breath) matches the jar exactly. "harder than netherite, shrugs off fire" is the only unverified line (code-set item attributes, no contradicting evidence) - left as-is; it reads as accurate endgame-weapon flavor. "Froglight" used throughout, never "Configurable Froglight". Clean.

## Chapter summary
- Quests: 10 total, 0 EDIT, 10 CLEAN
- Accuracy bugs (WRONG ledger rows): 0
- Highest-severity finding: none. Two UNVERIFIABLE rows for the verify pass to confirm if it can decompile method bodies: (1) the Froglight Cleaver's "harder than netherite / fire-immune" attribute values, and (2) the *specific* effect applied by boss Slime Milk's `entityInside` (text says Wither; the class confirms an effect is applied and the 6-face containment gate, but the effect Holder is registry-resolved so "Wither" can't be string-confirmed from the class constant pool). Both are consistent with the pack's stated design and nothing in the jar contradicts them. This is one of the most accurate chapters audited - every craftable recipe, count, and the cleaver loop ground-truthed clean.
