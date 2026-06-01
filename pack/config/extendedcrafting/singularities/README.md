# Sky Frogs singularities (Extended Crafting)

One singularity drives the Tier 6 / Void endgame: the **Froglight Singularity**
(`froglight.json`). It compresses **plain Froglights** (`productivefrogs:configurable_froglight`,
any variant) in the Quantum Compressor.

**Why one, made from Froglights (not six per species):** the singularity is a *proof-of-automation*
gate - at `defaultMaterialsRequired = 1000` (see `../../extendedcrafting-common.toml`) you cannot
hand-make the inputs, so a Froglight Singularity means you automated a Froglight farm. It feeds the
Ultimate Singularity -> the Master Frog (`kubejs/server_scripts/void_recipes.js`).

**Why NOT per-species:** Productive Frogs ships ONE Froglight item keyed by a
`productivefrogs:slime_variant` data component, so distinguishing variants needs a data-component
ingredient. **Extended Crafting 7.0.8's singularity `ingredient` field is item/tag/array only - it
rejects `neoforge:components`** (confirmed at runtime: `Failed to parse either ... Not a json array`,
`Loaded 0 singularity type(s)`). So variant-specific Froglight singularities are impossible; the
plain Froglight item is the codec-valid way to keep the input a Froglight. The six-species span is
enforced by progression instead (you cleared all six species chapters to reach the endgame, and the
Master Frog's recipe rings the singularity with Froglights).

If a future need wants *per-species* singularities, the only codec-valid route is plain smelted
resources (`{"item":"minecraft:iron_ingot"}`, etc.) - which are still Froglight-derived on this pack
(you smelt the variant Froglight to get them), just one step removed.
