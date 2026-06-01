# Sky Frogs singularities (Extended Crafting)

These six singularity definitions are the Tier 6 / Void endgame engine. Each compresses one
**species' variant Froglight** (not the smelted resource) in the Quantum Compressor:

| File | Froglight variant | Species |
|------|-------------------|---------|
| `iron.json` | `productivefrogs:iron` | Cave |
| `diamond.json` | `productivefrogs:diamond` | Geode |
| `clay.json` | `productivefrogs:clay_ball` | Bog |
| `prismarine.json` | `productivefrogs:prismarine_crystals` | Tide |
| `netherite.json` | `productivefrogs:netherite_scrap` | Infernal |
| `ender_pearl.json` | `productivefrogs:ender_pearl` | Void |

**Why Froglights, not resources:** the singularity is a *proof-of-automation* gate. At
`defaultMaterialsRequired = 1000` (see `../../extendedcrafting-common.toml`) you cannot hand-make
the inputs - a Froglight Singularity means you automated that species' frog loop. The Ultimate
Singularity (one of each, auto-recipe) therefore means you automated **all six species**, and the
Master Frog (`kubejs/server_scripts/void_recipes.js`) is the trophy for it.

**The variant match:** Productive Frogs ships ONE froglight item
(`productivefrogs:configurable_froglight`) keyed by a `productivefrogs:slime_variant` data
component, so each singularity uses a NeoForge data-component ingredient
(`"type": "neoforge:components"`, `"strict": false`) to match only its variant.

**Verification risk (check first in playtest):** Extended Crafting's singularity `ingredient`
field must route through the standard (NeoForge-patched) Ingredient codec for the
`neoforge:components` matcher to load. ATM10SKY's 7.0.8 singularities use the object-form
`{"item": ...}`, which is that codec - so this should work - but the mod author's docs describe
the field as item-only, so confirm in-game that the six singularities appear in JEI and accept
their variant Froglight. **If they do not load:** fall back to plain smelted-resource ingredients
(`{"item": "minecraft:iron_ingot"}`, `:diamond`, `:clay_ball`, `:prismarine_crystals`,
`:netherite_scrap`, `:ender_pearl`) - those are Froglight-derived too (you smelt Froglights to get
them), so the automation gate still holds, just one step removed.
