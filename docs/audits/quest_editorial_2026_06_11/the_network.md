# Audit: the_network ("The Network")

Mod(s) referenced: Refined Storage 2.0.8 (`refinedstorage-neoforge-2.0.8.jar`), Mekanism (energy source, prior tier). Generated chapter: no.

## Mechanic-claims ledger
| Quest | Claim (paraphrase) | Source checked (jar path / pack override) | Verdict |
|-------|--------------------|-------------------------------------------|---------|
| Quartz Enriched Iron | "iron forged with nether quartz" makes the part | `data/refinedstorage/recipe/quartz_enriched_iron.json` = 3x `c:ingots/iron` + 1x `c:gems/quartz` -> 4 output | MATCHES (nether quartz is in `c:gems/quartz`) |
| Quartz Enriched Iron | "Every Refined Storage part starts here" / quartz-gated | `storage_quartz_free.js` only re-issues Sophisticated/Functional controllers quartz-free; RS recipes untouched, controller/grid both need `quartz_enriched_iron` | MATCHES (RS stays quartz-gated) |
| The Controller | "The Controller is the network... feed it Forge Energy, everything downstream wakes up" | RS lang `controller.help` = "Provides the storage network with energy"; no pack RS config, so `requireEnergy` defaults true | MATCHES (energy required; "Forge Energy" is the loose-but-accepted name for the FE/NeoForge energy RS consumes) |
| The Controller | energy comes from "Geode-era Mekanism setup" | Mekanism generators output FE; RS accepts FE | MATCHES |
| The Grid | "the terminal - search, sort, and pull any item" | RS lang `grid.help` = "Allows for interacting with the storage network" | MATCHES |
| Disk Drive | "Disk Drive full of Storage Disks is the network's memory" | RS lang `disk_drive.help` = "Accepts storage disks to provide storage space"; tag = "Storage Disks" | MATCHES |
| Disk Drive | "Start with a 1k disk; scale to 64k and beyond" | RS lang: disk tiers are 1k/4k/16k/64k only; Quartz Arsenal addon adds Wireless Crafting Grid, NOT higher disks | PARTLY WRONG - 64k is the ceiling; "and beyond" overpromises (no non-creative tier above 64k in this pack) |
| | | | VERIFY: VERIFIED - RS 2.0.8 lang has exactly 1k/4k/16k/64k storage disks (+ Creative). No 256k/1024k item disk. Quartz Arsenal 1.0.8 lang adds only Wireless Crafting Grid (no disk tier). "and beyond" overpromises; AFTER fix correct. |
| Wire It Up | "Cable carries the network signal... run it between Controller, Grid, Disk Drive" | RS lang `cable.help` = "Connects storage network devices with each other" | MATCHES |
| External Storage | "exposes a drawer, barrel, or chest to the network" | RS lang `external_storage.help` = "Provides the network with storage from an external source" | MATCHES |
| Import and Export | "Importer pulls items in; Exporter pushes them out" | RS lang `importer.help` = "Imports resources from an external source"; `exporter.help` = "Exports resources to an external destination" | MATCHES |
| Crafting Grid | "a crafting table wired to the network - no hauling, it pulls them for you" | RS lang `crafting_grid.help` = "interacting with the storage network, with crafting abilities" | MATCHES |
| Autocrafting | "Pattern Grid records a recipe; Autocrafter runs it; request an item and the network crafts the whole tree" | RS lang `pattern_grid.help` = "creation of Patterns for use in autocrafting"; `autocrafter.help` = "Accepts patterns for autocrafting" | MATCHES |

## Per-quest findings

### Quartz Enriched Iron (quest.52E0000000000002)
- Disposition: CLEAN
- Task is `refinedstorage:quartz_enriched_iron` x1; prose matches the recipe and the quartz gate. Color codes balanced.

### The Controller (quest.52E0000000000005)
- Disposition: CLEAN
- "Forge Energy" is slightly dated (NeoForge 1.21.1 renames it NeoForge Energy) but it remains the universally understood player term, and RS itself does not surface a different name. Energy genuinely is required (no pack config disables it). Leave as-is to avoid jargon churn.

### The Grid (quest.52E0000000000008)
- Disposition: CLEAN
- Task `refinedstorage:grid` x1; "search, sort, pull" matches Grid behavior. Codes balanced.

### Disk Drive (quest.52E000000000000B)
- Disposition: EDIT
- Issues: Factual accuracy: "scale to 64k and beyond" overpromises. In this pack the storage-disk tiers stop at 64k (1k/4k/16k/64k); the Quartz Arsenal addon adds a Wireless Crafting Grid, not higher disks. "and beyond" implies a tier that does not exist outside creative.
- BEFORE:
  ```
  	quest.52E000000000000B.quest_desc: [
  		"A &eDisk Drive&r full of &bStorage Disks&r is the network's memory. Start with a 1k disk; scale to 64k and beyond later."
  	]
  ```
- AFTER:
  ```
  	quest.52E000000000000B.quest_desc: [
  		"A &eDisk Drive&r full of &bStorage Disks&r is the network's memory. Start with a 1k disk; swap in 4k, 16k, then 64k as you outgrow them."
  	]
  ```

### Wire It Up (quest.52E000000000000F)
- Disposition: CLEAN
- Task `refinedstorage:cable` x1; matches cable role. Codes balanced.

### External Storage (quest.52E0000000000012)
- Disposition: CLEAN
- Task `refinedstorage:external_storage` x1; "drawer, barrel, or chest" matches the "external source" help. "Functional Storage wall becomes searchable" ties to the quartz-free stopgap network the pack ships - consistent. Codes balanced.

### Import and Export (quest.52E0000000000015)
- Disposition: CLEAN
- Tasks require both `importer` and `exporter` x1; desc covers both directions. Codes balanced.

### Crafting Grid (quest.52E0000000000019)
- Disposition: CLEAN
- Task `refinedstorage:crafting_grid` x1; "crafting table wired to the network" matches. Codes balanced.

### Autocrafting (quest.52E000000000001C)
- Disposition: CLEAN
- Tasks require both `pattern_grid` and `autocrafter` x1; Pattern-records / Autocrafter-runs split matches the help text. Capstone "Infernal verb, complete" framing is accurate. Codes balanced.

## Chapter summary
- Quests: 9 total, 1 EDIT, 8 CLEAN
- Accuracy bugs (WRONG ledger rows): 1 - Disk Drive "scale to 64k and beyond" implies a storage-disk tier above 64k that does not exist in this pack (max is 64k; Quartz Arsenal adds only a Wireless Crafting Grid, not higher disks).
- Highest-severity finding: Disk Drive "64k and beyond" overpromise (low severity, single-word fix; rest of chapter is factually clean and well-grounded against RS 2.0.8).
