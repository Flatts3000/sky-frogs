# Sky Frogs singularities (Extended Crafting)

These JSONs are **generated** by `tools/gen_singularities.py` from Productive Frogs' `slime_variant`
data - **one singularity per vanilla froglight resource**. Re-run the generator when PF adds or
removes vanilla variants; do not hand-edit individual files.

There is one singularity for **every vanilla resource the frogs make** - 40 in all, across the six
species:

| Species | Count | Resources |
|---------|-------|-----------|
| Cave | 7 | iron, copper, gold, coal, redstone, obsidian, glow_ink_sac |
| Geode | 6 | diamond, emerald, amethyst, lapis, calcite, tuff |
| Bog | 8 | clay_ball, dirt, mud, moss, mycelium, lily_pad, leather, feather |
| Tide | 6 | prismarine, prismarine_crystals, sponge, sea_pickle, nautilus_shell, ink_sac |
| Infernal | 7 | quartz, glowstone_dust, blaze, soul_sand, soul_soil, netherrack, netherite_scrap |
| Void | 6 | ender_pearl, end_stone, chorus_fruit, echo_shard, sculk, shulker_shell |

Modded variants (steel, osmium, certus_quartz, inferium, ...) are skipped - those mods are not
pinned. Each singularity's two-color gradient is copied from its frog variant's own
`primary_color` / `secondary_color`, so the cube matches the frog that feeds it.

**The Ultimate Singularity = all 40.** Every file is flagged `inUltimateSingularity: true`, and EC
7.0.8 ships zero default singularities, so the auto-generated Ultimate Singularity recipe
(`ultimateSingularityRecipe = true` in `../../extendedcrafting-common.toml`) requires exactly these
40 - nothing foreign leaks in. The Ultimate Singularity then crafts the **Master Frog**
(`kubejs/server_scripts/void_recipes.js`). This makes the endgame a literal "you automated **every**
frog" capstone.

**Proof of automation.** At `defaultMaterialsRequired = 1000`, each singularity needs a thousand of
its resource (40,000 items + 40 Ultimate Catalysts across the full set) - you cannot hand-make that
many, so a finished Ultimate Singularity means you automated all 40 froglight farms. Per-singularity
counts are tunable via the optional `materialCount` field if a specific resource should cost less.

**Why the smelted resource and not the Froglight directly.** Productive Frogs ships ONE Froglight
item (`productivefrogs:configurable_froglight`) keyed by a `productivefrogs:slime_variant` data
component, so telling variants apart needs a data-component ingredient. **EC 7.0.8's singularity
`ingredient` field - and the Quantum Compressor's Cucumber `IngredientWithCount` input - are both
item/tag-value only; neither accepts `neoforge:components`, and a tag cannot help because every
variant shares one item id** (confirmed by reading the EC + Cucumber jars). So the singularity input
is the smelted resource - one codec-legal step removed from the Froglight, and on this void skyblock
the 40 resources have no other source than their frog.

To make a singularity literally consume a specific Froglight variant, the data model has to change
upstream: split Froglights into per-variant *items* in Productive Frogs (the way PF v1.8 split slime
milk into per-variant buckets). Then each variant is item/tag-addressable and usable as a singularity
ingredient directly. Tracked as a Productive Frogs request; until it lands, the smelted resource is
the input.
