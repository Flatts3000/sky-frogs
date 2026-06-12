# Audit: drowned_riches ("Drowned Riches")

Mod(s) referenced: Productive Frogs (PF 1.20.0), Functional Storage (compacting drawers), vanilla Minecraft (sea lantern, sponge, ice family, conduit). Generated chapter: no.

## Mechanic-claims ledger
| Quest | Claim (paraphrase) | Source checked (jar path / pack override) | Verdict |
|-------|--------------------|-------------------------------------------|---------|
| Drowned Riches | Each Tide resource: chamber slime, milk, feed a Tide Frog, smelt the Froglight | Pack frog-loop convention (Dissolution Chamber + per-variant milk + smelting); PF froglight smelting recipes confirmed | MATCHES |
| Prismarine Crystals | Prismarine Crystals Froglight smelts into prismarine crystals | PF `recipe/configurable_froglight_prismarine_crystals_to_prismarine_crystals.json` -> `minecraft:prismarine_crystals` | MATCHES |
| Prismarine Crystals | "four of them [crystals] around a prismarine shard make a sea lantern" | Vanilla sea_lantern recipe (no pack/mod override found; only mcwlights adds a sea_lantern_slab) | WRONG - vanilla sea lantern = 5 prismarine crystals + 4 prismarine shards (crystals in the plus/center, shards in the 4 corners), NOT 4 crystals around 1 shard. Ratio and central item both inverted. VERIFY: VERIFIED - jar sweep found no override of `minecraft:sea_lantern` (only `mcwlights:sea_lantern_slab`, a different item); no pack override. Vanilla recipe stands: 5 crystals + 4 shards. Prismarine shards are frog-available (PF `configurable_froglight_prismarine_to_prismarine_shard.json` exists), so the corrected recipe is achievable at tier. |
| Sponge | Sponge Froglight smelts to a dry sponge; soak up water with it | PF `recipe/configurable_froglight_sponge_to_sponge.json` -> `minecraft:sponge` (dry sponge); dry sponge absorbs water (vanilla) | MATCHES |
| Ink Sac | Ink Sac Froglight smelts to ink (black dye) | PF `recipe/configurable_froglight_ink_sac_to_ink_sac.json` -> `minecraft:ink_sac` | MATCHES |
| Sea Pickle | Sea Pickle Froglight smelts to a sea pickle (light source) | PF `recipe/configurable_froglight_sea_pickle_to_sea_pickle.json` -> `minecraft:sea_pickle` | MATCHES |
| Ice | Ice Froglight smelts to ice | PF `recipe/configurable_froglight_ice_to_ice.json` -> `minecraft:ice` | MATCHES |
| Ice | "Nine ice [pack] to packed ice, nine packed to blue ice" | Functional Storage compacting: `data/functionalstorage/recipe/compacting/ice.json` (9 ice -> 1 packed_ice) and `compacting/packed_ice.json` (9 packed_ice -> 1 blue_ice) | MATCHES (in-pack via compacting drawer; NOTE: this is NOT a vanilla crafting recipe - vanilla cannot craft packed ice from ice. The 9:1 chain is real here only because Functional Storage compacting drawers provide it. The chapter's own reward item is `functionalstorage:oak_1` drawers, so the path is available, but the text reads as if it were a crafting recipe.) |
| Ice | Froglights glow; ice melts under bright light; do not light an ice farm with its own froglights | Vanilla light/ice-melt behavior; PF froglights are light sources | MATCHES |
| Snow | Snow Froglight smelts to a snow block; enables snow layers, snowballs, snow golems | PF `recipe/configurable_froglight_snow_to_snow_block.json` -> `minecraft:snow_block`; vanilla snow block -> snow layers -> snowballs, and snow golem = 2 snow blocks + pumpkin | MATCHES (loose flavor: snowballs are reached via snow layers, not directly from the block, but the block does gate all three) |
| Turtle Scute | Turtle Scute Froglight smelts to a turtle scute, skipping the egg/baby life cycle | PF `recipe/configurable_froglight_turtle_scute_to_turtle_scute.json` -> `minecraft:turtle_scute` | MATCHES |
| Nautilus Shell | Nautilus Shell Froglight smelts to a nautilus shell; "the shell that aims a Conduit" | PF `recipe/configurable_froglight_nautilus_shell_to_nautilus_shell.json` -> `minecraft:nautilus_shell`; vanilla conduit = 8 nautilus shells + 1 heart of the sea | MATCHES (loose flavor: a conduit projects an area effect, it does not "aim"; nautilus shells *build* the conduit. Minor liberty, not an error.) |

## Per-quest findings

### Drowned Riches (quest.7D00000000000002)
- Disposition: EDIT
- Issues: Factual/task-alignment: "Five more to land the full aquatic roster" undercounts. The chapter has 8 resource quests after this gateway (Prismarine Crystals, Sponge, Ink Sac, Sea Pickle, Ice, Snow, Turtle Scute, Nautilus Shell). Even counting only the ones gated below this node it is 8, not 5.
- BEFORE:
  quest.7D00000000000002.quest_desc: [
  	"You pulled &bprismarine&r out of the void-sea; the rest of the reef follows the same loop. Each &eTide&r resource: chamber its slime, milk it, feed a &eTide Frog&r, smelt the &bFroglight&r."
  	""
  	"Five more to land the full aquatic roster. Claim your reward and dive in."
  ]
- AFTER:
  quest.7D00000000000002.quest_desc: [
  	"You pulled &bprismarine&r out of the void-sea; the rest of the reef follows the same loop. Each &eTide&r resource: chamber its slime, milk it, feed a &eTide Frog&r, smelt the &bFroglight&r."
  	""
  	"Eight more to land the full aquatic roster. Claim your reward and dive in."
  ]

### Prismarine Crystals (quest.7D00000000000005)
- Disposition: EDIT
- Issues: Factual accuracy (HIGH): the sea lantern recipe is stated backwards. Vanilla sea lantern = 5 prismarine crystals + 4 prismarine shards (crystals in the center plus, shards in the 4 corners), not "four crystals around a prismarine shard." Both the counts and the central item are wrong. Prismarine shards are available at this tier (the prismarine bridge froglight smelts to shards), so the corrected recipe is achievable.
- BEFORE:
  quest.7D00000000000005.quest_desc: ["Run the loop for &bPrismarine Crystals&r. Smelt the &bPrismarine Crystals Froglight&r into crystals - four of them around a prismarine shard make a &esea lantern&r."]
- AFTER:
  quest.7D00000000000005.quest_desc: ["Run the loop for &bPrismarine Crystals&r. Smelt the &bPrismarine Crystals Froglight&r into crystals - five crystals plus four prismarine shards make a &esea lantern&r."]

### Sponge (quest.7D00000000000008)
- Disposition: CLEAN
- Smelt -> dry sponge -> soak water is accurate; voice is tight and warm. No change.

### Ink Sac (quest.7D0000000000000B)
- Disposition: CLEAN
- Smelt -> ink sac (black dye) accurate. No change.

### Sea Pickle (quest.7D0000000000000E)
- Disposition: CLEAN
- Smelt -> sea pickle (light source) accurate. No change.

### Ice (quest.7D00000000000020)
- Disposition: EDIT
- Issues: Voice/clarity (LOW-MEDIUM): the "Nine ice [pack] to packed ice, nine packed to blue ice" chain is accurate ONLY via the Functional Storage compacting drawer (this chapter's reward item), not a crafting table - vanilla has no 9-ice -> packed-ice recipe. The text reads as if it were a vanilla crafting recipe and may mislead a player who tries it in a crafting grid. Also "ice pack" is an awkward typo-ish phrasing for "ice blocks." Tighten to name the mechanism.
- BEFORE:
  quest.7D00000000000020.quest_desc: [
  	"No cold biome ever forms out here - &bice&r exists because a frog makes it. Nine ice pack to packed ice, nine packed to &bblue ice&r: the whole frozen family unlocks from this one variant."
  	""
  	"Turn in the &bIce Froglight&r. (Placement note: Froglights glow, and ice melts under bright light - do not light an ice farm with its own produce.)"
  ]
- AFTER:
  quest.7D00000000000020.quest_desc: [
  	"No cold biome ever forms out here - &bice&r exists because a frog makes it. A &ecompacting drawer&r packs nine ice into packed ice, nine packed into &bblue ice&r: the whole frozen family unlocks from this one variant."
  	""
  	"Turn in the &bIce Froglight&r. (Placement note: Froglights glow, and ice melts under bright light - do not light an ice farm with its own produce.)"
  ]

### Snow (quest.7D00000000000023)
- Disposition: CLEAN
- Smelt -> snow block accurate; snow layers/snowballs/snow golems all gate off the block (snowballs via snow layers). Flavor is fine. No change.

### Turtle Scute (quest.7D00000000000029)
- Disposition: CLEAN
- Smelt -> turtle scute accurate; "skips the life cycle" is correct flavor (no eggs/babies needed). Note: task icon/title uses "Turtle Scute"; PF output is `minecraft:turtle_scute`. No change.

### Nautilus Shell (quest.7D00000000000011)
- Disposition: CLEAN
- Smelt -> nautilus shell accurate; "aims a Conduit" is loose flavor (a conduit is built from 8 shells + a heart of the sea and projects an area effect; it does not aim) but not a factual claim about a recipe. Acceptable as voice. No change.

## Chapter summary
- Quests: 9 total, 3 EDIT, 6 CLEAN
- Accuracy bugs (WRONG ledger rows): 1
  - Prismarine Crystals: sea lantern recipe stated backwards (real = 5 crystals + 4 shards, text says 4 crystals + 1 shard).
- Highest-severity finding: Prismarine Crystals (quest.7D00000000000005) gives a wrong vanilla recipe (sea lantern). A player following it literally cannot craft the item. HIGH.
- Secondary: Drowned Riches gateway miscounts remaining quests ("Five more" -> "Eight more"); Ice quest presents a Functional Storage compacting-drawer chain as if it were vanilla crafting (clarified to name the drawer).
