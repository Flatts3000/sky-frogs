# Audit: storage_and_crafting ("Storage & Crafting")

Mod(s) referenced: Sophisticated Storage, Functional Storage, Mekanism (Basic Fluid Tank), Trash Cans. Generated chapter: no.

Pack override in play: `pack/kubejs/server_scripts/storage_quartz_free.js` re-issues both storage controllers (Sophisticated + Functional) quartz-free. Sophisticated controller: `comparator -> repeater` (planks + `c:stones` + base wooden storage). Functional controllers: `quartz_block -> redstone_block` and `comparator -> repeater`. Storage Link / Storage Tool / ender parts keep ender pearls. The prose's quartz-free claims are all grounded in this override.

## Mechanic-claims ledger
| Quest | Claim (paraphrase) | Source checked | Verdict |
|-------|--------------------|----------------|---------|
| A Barrel of Your Own | Barrel takes upgrades that stack deeper, auto-pull, and compact | sophstorage stack_upgrade / pickup_upgrade / compacting_upgrade tooltips | MATCHES |
| Bigger on the Inside | Barrel tiers go copper -> iron -> gold; Cave frog supplies the metals | recipe copper_barrel.json (`c:ingots/copper`), iron, gold_barrel.json (`c:ingots/gold`, from iron_barrel) | MATCHES |
| Stack 'Em High | Stack Upgrade lets a slot hold "far more than a stack," swallows a whole frog farm | stack_upgrade_tier_1 tooltip = "Multiplies the number of stacks that can fit in a slot by 2" | MATCHES (mechanic) but OVERSTATED - tier 1 is only x2 |
| Hands-Free Intake | Pickup Upgrade grabs ground items; needs a sticky piston (a slime ball away) | recipe pickup_upgrade.json key P = `minecraft:sticky_piston` | MATCHES |
| A Wall of Drawers | Storage Controller ties drawers together; "used to want nether quartz - not in this pack. Stone, redstone, and a repeater do it." | storage_quartz_free.js functional controller = `c:stones` + `redstone_block` + `repeater`; stock recipe used `quartz_block` + `comparator` | MATCHES |
| A Wall of Drawers | "Compacting Drawers ... auto-packs its nuggets, ingots, and blocks" | functionalstorage compacting drawer behavior (standard) | MATCHES, but no compacting-drawer TASK in this chapter (see alignment note) |
| One Window on Everything | Controller opens connected barrels in one searchable window; Link+Tool reach distant ones; "a repeater where the comparator used to go" | storage_quartz_free.js sophstorage controller uses `repeater`; storage_link / storage_tool tooltips confirm linking | MATCHES |
| One Window on Everything | Storage Links want ender pearls | storage_quartz_free.js comment leaves ender-pearl parts intact | MATCHES |
| Liquid Assets | Fluid Drawer = planks + a bucket; holds one fluid; links to the same Storage Controller | recipe fluid_1.json (8 planks + 1 bucket); in-game name "Fluid Drawer (1x1)" | MATCHES |
| Tanks a Lot | Basic Fluid Tank = "just iron and redstone, no machines and no osmium" | recipe basic.json: `c:ingots/iron` + `mekanism:alloys/basic`; that tag resolves to `minecraft:redstone` | MATCHES (basic tier needs no infused alloy / machine) |
| Take Out the Trash | Trash Can voids items; has a filter (up to 9); hopper-feedable | trashcans lang "Can void items, also contains a filter for up to 9 items" | MATCHES |

No WRONG rows.

VERIFY (Stack 'Em High overstatement, the one quasi-accuracy item): VERIFIED. sophisticatedstorage-1.21.1-1.5.52.1756.jar lang `stack_upgrade_tier_1.tooltip` = "Multiplies the number of stacks that can fit in a slot by 2" (x2); higher tiers go x3/x4/x8/x16/x32. The chapter's `storage_and_crafting.snbt` quest 570A6E0000000008 task AND reward are both `sophisticatedstorage:stack_upgrade_tier_1` -- so the player gets the x2 tier, and "far more than a stack / swallows a whole frog farm without blinking" overstates it. AFTER edit (doubles + "higher tiers multiply further") is correct -- apply. (Naming polish rows Barrel / Item Trash Can spot-checked plausible, not re-litigated.)

## Per-quest findings

### A Barrel of Your Own (quest.570A6E0000000002)
- Disposition: EDIT
- Issues: Terminology: the in-game item is named just **"Barrel"** (Sophisticated Storage block id `barrel`, display "Barrel"), not "Sophisticated Barrel." "Sophisticated Barrel" reads as the mod-internal framing. Keep the mod attribution but match the item name a player sees.
- BEFORE:
  "A &eSophisticated Barrel&r starts as a plain wooden box - but it takes &fupgrades&r that stack it deeper, pull items in on their own, and pack them down. Craft your first; everything here slots into it."
- AFTER:
  "A &eBarrel&r starts as a plain wooden box - but it takes &fupgrades&r that stack it deeper, pull items in on their own, and pack them down. Craft your first; everything here slots into it."

### Bigger on the Inside (quest.570A6E0000000005)
- Disposition: CLEAN

### Stack 'Em High (quest.570A6E0000000008)
- Disposition: EDIT
- Issues: Factual accuracy (overstatement): the reward/task is **Stack Upgrade Tier 1**, which only multiplies slot capacity by 2 (its in-game tooltip: "Multiplies the number of stacks that can fit in a slot by 2"). "far more than a stack" and "swallows a whole frog farm's output without blinking" oversell a x2 tier (higher tiers exist for the big multipliers). Trim to a true claim that still reads as a win.
- BEFORE:
  "Here's the real magic. A &eStack Upgrade&r dropped into a barrel lets every slot hold far more than a stack - one barrel swallows a whole frog farm's output without blinking."
  ""
  "Craft one and slot it in."
- AFTER:
  "Here's the real magic. A &eStack Upgrade&r dropped into a barrel doubles what every slot holds - and the higher tiers multiply it further still, so one barrel keeps up with a frog farm."
  ""
  "Craft one and slot it in."

### Hands-Free Intake (quest.570A6E000000000B)
- Disposition: CLEAN

### A Wall of Drawers (quest.570A6E000000000E)
- Disposition: EDIT
- Issues: Task-vs-text alignment: the opening "You've been collecting &bCompacting Drawers&r one Cave metal at a time" presumes drawers the player built off-quest; the chapter's only task here is the **Storage Controller**. Defensible as flavor, but soften so it doesn't read as referencing a step that never appeared. Voice: tighten slightly. (Mechanic claims all correct - keep the quartz-free parenthetical.)
- BEFORE:
  "You've been collecting &bCompacting Drawers&r one Cave metal at a time. Each holds a single resource by the thousand and auto-packs its nuggets, ingots, and blocks together."
  ""
  "Tie the wall together: a &eStorage Controller&r linked to your drawers lets you pull from all of them in one spot. (It used to want nether quartz - not in this pack. Stone, redstone, and a repeater do it.)"
- AFTER:
  "&bCompacting Drawers&r each hold one resource by the thousand and auto-pack its nuggets, ingots, and blocks together - one drawer per Cave metal makes a tidy wall."
  ""
  "Tie that wall together: a &eStorage Controller&r linked to your drawers lets you pull from all of them in one spot. (It used to want nether quartz - not in this pack. Stone, redstone, and a repeater do it.)"

### One Window on Everything (quest.570A6E0000000011)
- Disposition: CLEAN

### A Place for Everything (quest.570A6E0000000014)
- Disposition: CLEAN
- Note: "Crafting Station you've had since day one" - this is the Sophisticated Storage Crafting Station / the pack's day-one crafting table. Not ground-truthable to a task in THIS chapter (checkmark task), but consistent with the chapter's framing as a capstone. No change.

### Liquid Assets (quest.570A6E0000000019)
- Disposition: CLEAN
- Note: in-game name is "Fluid Drawer (1x1)"; prose says "Fluid Drawer" - fine, the size suffix is a variant detail.

### Tanks a Lot (quest.570A6E000000001C)
- Disposition: CLEAN
- Note: "just iron and redstone" verified - basic tier's alloy slot resolves to plain redstone, no Metallurgic Infuser needed. Accurate and reassuring for a Mekanism-shy player.

### Take Out the Trash (quest.570A6E000000001F)
- Disposition: EDIT
- Issues: Terminology: the in-game block is **"Item Trash Can"** (trashcans `item_trash_can`), and the mod ships a separate fluid/energy trash can, so "Trash Can" is mildly ambiguous. Minor - one-word fix.
- BEFORE:
  "Not everything's worth a slot. A &eTrash Can&r quietly voids whatever you feed it - the cobble your generator won't stop making, junk mob drops, the fourth stack of rotten flesh."
- AFTER:
  "Not everything's worth a slot. An &eItem Trash Can&r quietly voids whatever you feed it - the cobble your generator won't stop making, junk mob drops, the fourth stack of rotten flesh."

## Chapter summary
- Quests: 10 total, 4 EDIT, 6 CLEAN
- Accuracy bugs (WRONG ledger rows): 0. One OVERSTATEMENT (Stack 'Em High oversells the Tier-1 x2 multiplier as "far more than a stack" / "without blinking") - flagged as EDIT, not a hard WRONG.
- Highest-severity finding: Stack 'Em High overstates Stack Upgrade Tier 1 (actually x2 per the in-game tooltip) - the only claim that could mislead a player on what they're getting. Everything else is naming polish (Barrel / Item Trash Can) and one alignment softening (Wall of Drawers presumes off-quest drawers). All quartz-free recipe claims correctly track the `storage_quartz_free.js` override.
