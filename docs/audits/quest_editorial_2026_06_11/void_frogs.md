# Audit: void_frogs ("Void Frogs" - Tier 6 species chapter)

Mod(s) referenced: Productive Frogs (productivefrogs-1.20.0.jar); vanilla Minecraft (End resources). Generated chapter: no.

## Mechanic-claims ledger

| Quest | Claim (paraphrase) | Source checked (jar path / pack override) | Verdict |
|-------|--------------------|-------------------------------------------|---------|
| Beyond the Pearl | Void frog produces end stone, chorus, echo shards, sculk, shulker shells (the End) | slime_variant/{end_stone,chorus_fruit,echo_shard,sculk,shulker_shell}.json all category "void"; froglight smelt recipes resolve to each vanilla item | MATCHES |
| Beyond the Pearl | "Ender pearls were just the doorway" (gateway used ender pearl) | ender_pearl is a froglight variant; road_to_void gateway leads with it (per project memory) | MATCHES |
| End Stone | End Stone Froglight smelts to end stone | recipe/configurable_froglight_end_stone_to_end_stone.json -> result minecraft:end_stone | MATCHES |
| Chorus Fruit | Froglight gives chorus fruit; teleport snack; popped chorus -> purpur | recipe configurable_froglight_chorus_fruit_to_chorus_fruit.json -> minecraft:chorus_fruit; vanilla teleport + purpur | MATCHES |
| Chorus Fruit | Item named "Chorus Froglight" | lang: block.productivefrogs.configurable_froglight.chorus_fruit = "Chorus Fruit Froglight" | WRONG - in-game name is "Chorus Fruit Froglight", text drops "Fruit" |
| | | | VERIFY: VERIFIED - PF lang `configurable_froglight.chorus_fruit` = "Chorus Fruit Froglight". Text "Chorus Froglight" drops "Fruit". Fix to "Chorus Fruit Froglight" correct. |
| Echo Shard | Echo Shard Froglight smelts to echo shard; makes recovery compass | recipe ...echo_shard_to_echo_shard.json -> minecraft:echo_shard; vanilla recovery compass = 8 compass + 1 echo shard | MATCHES |
| Echo Shard | "straight from the frog instead of the deep dark" (no deep-dark mining) | froglight loop is the only source on skyblock; smelt recipe is the producer | MATCHES |
| Sculk | Sculk Froglight smelts to sculk; "XP blocks and redstone-by-sound" | recipe ...sculk_to_sculk.json -> minecraft:sculk; vanilla sculk drops 1 XP when mined, sculk sensor = sound-driven redstone | MATCHES |
| Phantom Membrane | Froglight gives phantom membrane; slow falling + elytra repair; no night-skip needed | recipe ...phantom_membrane_to_phantom_membrane.json -> minecraft:phantom_membrane; vanilla slow-falling brew + anvil elytra repair | MATCHES |
| Shulker Shell | Shulker Shell Froglight smelts to shulker shell; shulker boxes; no shulker hunt | recipe ...shulker_shell_to_shulker_shell.json -> minecraft:shulker_shell; vanilla shulker box = 2 shells + chest | MATCHES |

All froglight-check tasks confirmed: each quest's task requires `productivefrogs:configurable_froglight` with the matching `slime_variant` component (strict) - the froglight-check law holds across all 7 quests.

## Per-quest findings

### Beyond the Pearl (quest.60F0000000000002)
- Disposition: EDIT
- Issues: Stale/missing reference (minor): the intro enumerates the chapter's resources as "end stone, chorus, echo shards, sculk, and the shells the shulkers leave behind" - 5 of the chapter's 6 resources; phantom membrane is silently omitted. Low-severity; adding it keeps the promise honest without bloating the line.
- BEFORE:
  ```
  quest.60F0000000000002.quest_desc: [
  	"Ender pearls were just the doorway. The &5Void&r frog hands you the whole End:"
  	""
  	"end stone, chorus, echo shards, sculk, and the shells the shulkers leave behind."
  ]
  ```
- AFTER:
  ```
  quest.60F0000000000002.quest_desc: [
  	"Ender pearls were just the doorway. The &5Void&r frog hands you the whole End:"
  	""
  	"end stone, chorus fruit, echo shards, sculk, phantom membranes, and the shells the shulkers leave behind."
  ]
  ```

### End Stone (quest.60F0000000000005)
- Disposition: CLEAN

### Chorus Fruit (quest.60F0000000000008)
- Disposition: EDIT
- Issues: Terminology: text says "Chorus Froglight"; the item's exact in-game name is "Chorus Fruit Froglight". Player text must match the mod's lang exactly.
- BEFORE:
  ```
  quest.60F0000000000008.quest_desc: [
  	"&dChorus Fruit&r - teleport snacks, and popped chorus for purpur. Turn in the &bChorus Froglight&r."
  ]
  ```
- AFTER:
  ```
  quest.60F0000000000008.quest_desc: [
  	"&dChorus Fruit&r - teleport snacks, and popped chorus for purpur. Turn in the &bChorus Fruit Froglight&r."
  ]
  ```

### Echo Shard (quest.60F000000000000B)
- Disposition: CLEAN

### Sculk (quest.60F000000000000E)
- Disposition: CLEAN
- Note: "XP blocks" is accurate (mining a vanilla sculk block drops 1 XP); "redstone-by-sound" fairly describes sculk sensors crafted from it. No change.

### Phantom Membrane (quest.60F0000000000014)
- Disposition: CLEAN
- Note: "slow falling and elytra repair" both verified vanilla; froglight name "Phantom Membrane Froglight" matches lang exactly.

### Shulker Shell (quest.60F0000000000011)
- Disposition: CLEAN
- Note: "the only portable storage that survives the void" is flavor (shulker box contents persist on death); not a false mechanic claim. Froglight name matches lang.

## Chapter summary
- Quests: 7 total, 2 EDIT, 5 CLEAN
- Accuracy bugs (WRONG ledger rows): 1
  - Chorus Fruit (quest.60F0000000000008): item named "Chorus Froglight" in text; correct in-game name is "Chorus Fruit Froglight".
- Highest-severity finding: the "Chorus Froglight" terminology mismatch (quest 0008) - a player searching JEI for the turn-in item by the quest's name finds nothing; fix to "Chorus Fruit Froglight".
- Secondary: "Beyond the Pearl" intro omits phantom membrane from its 6-resource roster list (cosmetic completeness).
- No em/en dashes, no unbalanced color codes, no broken escapes anywhere in the chapter. All froglight-check tasks are correctly variant-strict.
