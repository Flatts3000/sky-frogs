# Audit: infernal_frogs ("Infernal Frogs")

Mod(s) referenced: Productive Frogs (froglights, slime variants, brewed froglights, Curios froglight slot), Industrial Foregoing (Dissolution Chamber), Refined Storage (Quartz Enriched Iron), Curios, Functional Storage (Compacting Drawer reward), vanilla. Generated chapter: no.

## Mechanic-claims ledger
| Quest | Claim (paraphrase) | Source checked (jar path / pack override) | Verdict |
|-------|--------------------|-------------------------------------------|---------|
| Beyond Netherrack | Infernal frog yields obsidian, quartz, glowstone, blaze, netherite | All 9 chain variants present, category "infernal" (PF `data/productivefrogs/productivefrogs/slime_variant/*.json`) | MATCHES (illustrative list, not exhaustive) |
| Obsidian | "Netherrack milk presses into an Obsidian Slime" | Pack override `dissolution_slime_recipes.js` row `['obsidian','minecraft:netherrack']`; recipe type `industrialforegoing:dissolution_chamber`, input = `minecraft:netherrack` ITEM (not milk), output `slime_bucket` Obsidian | WRONG - input is the netherrack resource item in the Dissolution Chamber, there is no "netherrack milk" in this recipe |
| | | | VERIFY: VERIFIED - dissolution_slime_recipes.js line 108 `['obsidian','minecraft:netherrack']` under INFERNAL filler `minecraft:prismarine`. Input is the netherrack resource ITEM, no milk. AFTER fix ("Netherrack feeds the Dissolution Chamber") is correct. Stale-pivot "milk" framing. |
| Obsidian | "Run it through the Dissolution Chamber (Tier 5 slimes are chamber-only)" | `dissolution_slime_recipes.js` (IF chamber); no Tier-5 crafting-table chain exists (`froglight_slime_recipes.js`/table chains are Cave/Geode/Bog only) | MATCHES |
| Obsidian | Smelt the Obsidian Froglight for obsidian | PF `recipe/configurable_froglight_obsidian_to_obsidian.json` smelting -> `minecraft:obsidian` | MATCHES |
| Quartz | Quartz unlocks comparators/observers and the Quartz Enriched Iron that Refined Storage runs on | PF `..._quartz_to_quartz.json` -> `minecraft:quartz`; RS `recipe/quartz_enriched_iron.json` keys on `c:gems/quartz` (nether quartz qualifies) | MATCHES |
| Glowstone | Glowstone Froglight -> glowstone | PF `..._glowstone_dust_to_glowstone_dust.json` -> `minecraft:glowstone_dust` | MATCHES |
| Soul Sand | Soul Sand Froglight -> soul sand (bubble columns, wither fuel, soul-speed) | PF `..._soul_sand_to_soul_sand.json` -> `minecraft:soul_sand`; vanilla uses correct | MATCHES |
| Soul Soil | Soul Soil Froglight -> soul soil (soul campfires/lanterns burn blue) | PF `..._soul_soil_to_soul_soil.json` -> `minecraft:soul_soil`; vanilla correct | MATCHES |
| Blaze | Blaze Froglight smelts to blaze ROD; each rod crafts into two powder | PF `..._blaze_to_blaze_rod.json` -> `minecraft:blaze_rod`; vanilla 1 rod -> 2 blaze powder | MATCHES |
| Ghast Tear | Ghast Tear Froglight -> ghast tear (regen potions, End crystals) | PF `..._ghast_tear_to_ghast_tear.json` -> `minecraft:ghast_tear`; vanilla uses correct | MATCHES |
| Magma Cream | Magma Cream Froglight -> magma cream (fire-res potions, magma blocks) | PF `..._magma_cream_to_magma_cream.json` -> `minecraft:magma_cream`; vanilla correct | MATCHES |
| Netherite Scrap | Scrap smelted from ancient debris; 4 scrap + gold -> Netherite Ingot | PF `..._netherite_scrap_to_netherite_scrap.json` -> `minecraft:netherite_scrap` (variant inner_block ancient_debris); vanilla 4 scrap + 4 gold -> ingot | MATCHES (vanilla ingot recipe is 4 scrap + 4 gold; "plus gold" is loose but not wrong) |
| Pop the Cork | Throw splash/lingering potion at a slime; the Froglight that drops captures the effect; place + right-click to toggle aura; held buffs self | PF Curios `BrewedFroglightCurio`; lang `tooltip.brewed_aura` "Aura: %1$s", `tooltip.aura_enabled` "Active - right-click to toggle", `jade.aura_on/off` | MATCHES |
| Charmed, I'm Sure | Brewed Froglight rides a dedicated Froglight Curios slot and buffs while worn | PF `data/productivefrogs/curios/slots/froglight.json` (validators: `productivefrogs:brewed`), `curios/entities/froglight.json` (player), `curios.identifier.froglight` "Froglight" | MATCHES |

## Per-quest findings

### Beyond Netherrack (quest.51F0000000000002)
- Disposition: CLEAN
- Gateway checkmark; flavor intro. Illustrative resource list is fine. Color codes balanced (`&c...&r`).

### Obsidian (quest.51F0000000000017)
- Disposition: EDIT
- Issues: Factual accuracy: "Netherrack milk presses into an Obsidian Slime" - the Dissolution Chamber recipe input is the netherrack RESOURCE ITEM (`minecraft:netherrack`), not any "milk," and the chamber is not a "press." The threading is netherrack-resource -> Obsidian slime. The second sentence already names the Dissolution Chamber correctly, so the first sentence's "milk" + "presses" is the only slip.
- Minor: the item's in-game name is "Bucket of Obsidian Slime"; "an Obsidian Slime" reads fine as prose, left as-is.
- BEFORE:
  ```
  quest.51F0000000000017.quest_desc: [
  	"&cNetherrack milk&r presses into an &8Obsidian Slime&r - the other portal stone, no bucket-and-lava dance required."
  	""
  	"Run it through the &eDissolution Chamber&r (Tier 5 slimes are chamber-only), turn in the &8Obsidian Froglight&r, and smelt it for &8obsidian&r whenever you need it."
  ]
  ```
- AFTER:
  ```
  quest.51F0000000000017.quest_desc: [
  	"&cNetherrack&r feeds the &eDissolution Chamber&r to make an &8Obsidian Slime&r - the other portal stone, no bucket-and-lava dance required."
  	""
  	"Tier 5 slimes are chamber-only. Raise the Obsidian frog, turn in the &8Obsidian Froglight&r, and smelt it for &8obsidian&r whenever you need it."
  ]
  ```

### Quartz (quest.51F0000000000005)
- Disposition: CLEAN
- "Refined Storage" spelled and capitalized correctly; Quartz Enriched Iron claim verified against RS recipe. Color codes balanced.

### Glowstone (quest.51F0000000000008)
- Disposition: CLEAN

### Soul Sand (quest.51F000000000000B)
- Disposition: CLEAN

### Soul Soil (quest.51F000000000000E)
- Disposition: CLEAN

### Blaze (quest.51F0000000000011)
- Disposition: CLEAN
- Smelts to blaze ROD (not powder) - correct; "each rod crafts into two powder" is accurate vanilla. Codes balanced.

### Ghast Tear (quest.51F000000000001E)
- Disposition: CLEAN

### Magma Cream (quest.51F0000000000021)
- Disposition: CLEAN

### Netherite Scrap (quest.51F0000000000014)
- Disposition: CLEAN
- "Four scrap plus gold makes a Netherite Ingot" is loose (vanilla is 4 scrap + 4 gold) but reads correctly for a quest summary; not flagged as an error. "best gear in the game" is acceptable flavor.

### Pop the Cork (quest.51F0000000000024)
- Disposition: CLEAN
- Brewed-froglight capture + place/right-click aura toggle + held self-buff all verified against PF Curios class and tooltip lang. Honor-system checkmark matches the task. Long but information-dense, voice is on-target. Codes balanced.

### Charmed, I'm Sure (quest.51F0000000000027)
- Disposition: CLEAN
- Dedicated Curios "Froglight" slot (validator `productivefrogs:brewed`) confirmed. Checkmark task matches. Codes balanced.

## Chapter summary
- Quests: 12 total, 1 EDIT, 11 CLEAN
- Accuracy bugs (WRONG ledger rows): 1
  - Obsidian (quest.51F0000000000017): "Netherrack milk presses into an Obsidian Slime" - the Dissolution Chamber input is the netherrack resource ITEM, not "milk," and the chamber is not a press. Fixed in AFTER.
- Highest-severity finding: the Obsidian "Netherrack milk" mechanic slip - a leftover "milk" framing for what is actually a resource-item-fed Dissolution Chamber recipe (the recurring post-pivot stale-wording class). Everything else in the chapter ground-truths clean: all 9 froglight->resource smelts, the RS Quartz Enriched Iron gate, and both brewed-froglight aura/Curios-slot quests match the pinned PF 1.20.0 jar and pack overrides exactly. No em/en dashes, no unbalanced color codes, "Froglight" used throughout (never "Configurable Froglight").
```
