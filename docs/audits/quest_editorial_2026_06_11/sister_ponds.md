# Audit: sister_ponds ("Sister Ponds")

Mod(s) referenced: All the Ores, Powah, Refined Storage, Mekanism, Industrial Foregoing, Flux Networks, Just Dire Things. Generated chapter: **yes** (`tools/gen_completionist_chapters.py`).

This is the MODDED Completionist census chapter: 34 per-resource census quests (one per loaded-mod PF variant) plus 1 capstone = 35 quests. Every census quest carries **only a title** (no subtitle, no description); the only bespoke prose is the capstone's subtitle + description. All fixes below belong in `tools/gen_completionist_chapters.py` (generated chapter) - a direct lang edit is wiped on the next regen.

The per-resource title is emitted at **generator line 322**:
`lang.append(f'\tquest.{qid}.title: "{title_case(name)} ({MOD_LABELS[mod]})"')`
where `name` is the raw PF variant slug and `title_case` (line 183-184) only splits on `_` and capitalizes each word. So any variant whose in-game item name differs from `title_case(slug)` produces a title the player can't reconcile with the item in their hand. There is no display-name override map today (only `ICON_OVERRIDES`); the icons are all correct, but the titles for two mod columns drift from the jar lang.

## Mechanic-claims ledger

These quests make no mechanic claims (each task is a froglight-component check with no prose). The "claim" being verified is therefore the **display name in each title** vs the mod jar's `assets/<ns>/lang/en_us.json`. Capstone prose is verified separately.

| Quest | Claim (the title's display name) | Source checked (jar path) | Verdict |
|-------|----------------------------------|---------------------------|---------|
| Osmium / Aluminum / Lead / Nickel / Silver / Tin / Uranium / Zinc (All the Ores) | bare metal name | `alltheores` lang `item.alltheores.<m>_ingot` = "Osmium Ingot" etc. | MATCHES (variant = the material; bare name reads fine, icon is the ingot) |
| Uraninite (Powah) | "Uraninite" | `powah` `item.powah.uraninite` = "Uraninite" | MATCHES |
| Energized Steel (Powah) | "Energized Steel" | `powah` `item.powah.steel_energized` = "Energized Steel" | MATCHES |
| Dry Ice (Powah) | "Dry Ice" | `powah` `block.powah.dry_ice` = "Dry Ice" | MATCHES |
| Blazing (Powah) | "Blazing" | `powah` `item.powah.crystal_blazing` = **"Blazing Crystal"** | WRONG - title drops "Crystal"; in-game item is "Blazing Crystal" |
| | | | VERIFY: VERIFIED - Powah 6.2.8 lang `item.powah.crystal_blazing` = "Blazing Crystal". Fix to "Blazing Crystal (Powah)" correct (generator-level via TITLE_OVERRIDES). |
| Niotic (Powah) | "Niotic" | `powah` `item.powah.crystal_niotic` = **"Niotic Crystal"** | WRONG - in-game item is "Niotic Crystal" |
| | | | VERIFY: VERIFIED - lang `item.powah.crystal_niotic` = "Niotic Crystal". |
| Spirited (Powah) | "Spirited" | `powah` `item.powah.crystal_spirited` = **"Spirited Crystal"** | WRONG - in-game item is "Spirited Crystal" |
| | | | VERIFY: VERIFIED - lang `item.powah.crystal_spirited` = "Spirited Crystal". |
| Nitro (Powah) | "Nitro" | `powah` `item.powah.crystal_nitro` = **"Nitro Crystal"** | WRONG - in-game item is "Nitro Crystal" |
| | | | VERIFY: VERIFIED - lang `item.powah.crystal_nitro` = "Nitro Crystal". |
| Silicon / Quartz Enriched Iron / Basic Processor / Improved Processor / Advanced Processor (Refined Storage) | as titled | `refinedstorage` lang: "Silicon", "Quartz Enriched Iron", "Basic Processor", "Improved Processor", "Advanced Processor" | MATCHES (all five exact) |
| Steel (Mekanism) | "Steel" | `mekanism` `item.mekanism.ingot_steel` = "Steel Ingot" | MATCHES (variant = material "Steel"; icon is the ingot - acceptable, see note) |
| Fluorite (Mekanism) | "Fluorite" | `mekanism` `item.mekanism.fluorite_gem` = "Fluorite" | MATCHES |
| Refined Glowstone (Mekanism) | "Refined Glowstone" | `mekanism` `ingot_refined_glowstone` = "Refined Glowstone Ingot" | MATCHES (material name; icon is the ingot) |
| Refined Obsidian (Mekanism) | "Refined Obsidian" | `mekanism` `ingot_refined_obsidian` = "Refined Obsidian Ingot" | MATCHES (material name; icon is the ingot) |
| Plastic (Industrial Foregoing) | "Plastic" | `industrialforegoing` `item.industrialforegoing.plastic` = "Plastic" | MATCHES |
| Pink Slime (Industrial Foregoing) | "Pink Slime" | `industrialforegoing` `item.industrialforegoing.pink_slime` = "Pink Slime" | MATCHES |
| Flux Dust (Flux Networks) | "Flux Dust" | `fluxnetworks` `item.fluxnetworks.flux_dust` = "Flux Dust" | MATCHES |
| Ferricore (Just Dire Things) | "Ferricore" | `justdirethings` `ferricore_ingot` = "Ferricore Ingot" | MATCHES (material "Ferricore") |
| Blazegold (Just Dire Things) | "Blazegold" | `justdirethings` `blazegold_ingot` = "Blazegold Ingot" | MATCHES (material "Blazegold") |
| Celestigem (Just Dire Things) | "Celestigem" | `justdirethings` `celestigem` = "Celestigem" | MATCHES |
| Eclipsealloy (Just Dire Things) | "Eclipsealloy" | `justdirethings` `eclipsealloy_ingot` = **"Eclipse Alloy Ingot"** | WRONG - title reads "Eclipsealloy" (one word); the mod renders the material as two words, "Eclipse Alloy" |
| | | | VERIFY: VERIFIED - JDT 1.5.7 lang renders the material two words everywhere (`eclipsealloy_ingot` = "Eclipse Alloy Ingot", `template_eclipsealloy` = "Template: Eclipse Alloy", block = "Eclipse Alloy Block"). Census title "Eclipsealloy" wrong; fix to "Eclipse Alloy (Just Dire Things)" correct. Sibling `eclipse_ember` HAS the underscore so title_case handles it - the override is per-slug, not a title_case change. Generator-level fix (TITLE_OVERRIDES) is the right call. |
| Blaze Ember (Just Dire Things) | "Blaze Ember" | `justdirethings` `refined_t2_fluid_bucket` = "Blaze Ember Fuel Bucket" | MATCHES (material "Blaze Ember"; icon is the fuel bucket) |
| Voidflame (Just Dire Things) | "Voidflame" | `justdirethings` `refined_t3_fluid_bucket` = "Voidflame Fuel Bucket" | MATCHES (material "Voidflame") |
| Eclipse Ember (Just Dire Things) | "Eclipse Ember" | `justdirethings` `refined_t4_fluid_bucket` = "Eclipse Ember Fuel Bucket" | MATCHES (material "Eclipse Ember") |
| Sister Ponds (capstone) | prose, see below | n/a | MATCHES (ASCII only, no dash) |

Note on the "material name vs item name" rows marked MATCHES: titles like "Steel", "Refined Glowstone", "Refined Obsidian", "Ferricore", "Blazegold", "Blaze Ember" name the *material* rather than the exact item ("... Ingot" / "... Fuel Bucket"). This is internally consistent (the census is a roster of resources the frog makes, not a shopping list of items) and the icon disambiguates. Left as MATCHES - no change recommended. The five WRONG rows are different: "Blazing"/"Niotic"/"Spirited"/"Nitro" and "Eclipsealloy" are not the material name *or* the item name - they are an artifact of `title_case` mangling the slug.

## Per-quest findings

The 34 census quests and capstone are listed below. Census quests with MATCHES titles are CLEAN (one-liner). The five drift titles + a generator-level recommendation follow.

### All the Ores column (8 quests) - all CLEAN
Osmium (quest.70DD9CE8D28270C3), Aluminum (70DDE8959C46DE77), Lead (70DDD75E3D26ECE7), Nickel (70DD1B4FCB046228), Silver (70DD3DED432660AC), Tin (70DD42E9DCA61D0A), Uranium (70DD227DBEE3A633), Zinc (70DD8FDCBCF1C143): CLEAN. Bare metal name + ingot icon; "Aluminum" matches ATO's US spelling.

### Powah column (7 quests) - 3 CLEAN, 4 EDIT
- Uraninite (quest.70DDF22219138525): CLEAN.
- Energized Steel (quest.70DD8655ED1C027C): CLEAN.
- Dry Ice (quest.70DD4189CF5B59C4): CLEAN.

#### Blazing (Powah) (quest.70DDFF714569D134)
- Disposition: EDIT
- Issues: terminology/factual: title is "Blazing"; the Powah item is **"Blazing Crystal"**. The bare adjective doesn't name a recognizable item.
- BEFORE: `quest.70DDFF714569D134.title: "Blazing (Powah)"`
- AFTER: `quest.70DDFF714569D134.title: "Blazing Crystal (Powah)"`
- Fix belongs in `tools/gen_completionist_chapters.py` (generated chapter): add a display-name override (see recommendation below). Do not edit the lang file directly.

#### Niotic (Powah) (quest.70DD6F2CFCE78A17)
- Disposition: EDIT
- Issues: terminology/factual: title "Niotic"; item is **"Niotic Crystal"**.
- BEFORE: `quest.70DD6F2CFCE78A17.title: "Niotic (Powah)"`
- AFTER: `quest.70DD6F2CFCE78A17.title: "Niotic Crystal (Powah)"`
- Fix belongs in `tools/gen_completionist_chapters.py` (generated chapter).

#### Spirited (Powah) (quest.70DD2DA496EE8E42)
- Disposition: EDIT
- Issues: terminology/factual: title "Spirited"; item is **"Spirited Crystal"**.
- BEFORE: `quest.70DD2DA496EE8E42.title: "Spirited (Powah)"`
- AFTER: `quest.70DD2DA496EE8E42.title: "Spirited Crystal (Powah)"`
- Fix belongs in `tools/gen_completionist_chapters.py` (generated chapter).

#### Nitro (Powah) (quest.70DDB24A799921BC)
- Disposition: EDIT
- Issues: terminology/factual: title "Nitro"; item is **"Nitro Crystal"**.
- BEFORE: `quest.70DDB24A799921BC.title: "Nitro (Powah)"`
- AFTER: `quest.70DDB24A799921BC.title: "Nitro Crystal (Powah)"`
- Fix belongs in `tools/gen_completionist_chapters.py` (generated chapter).

### Refined Storage column (5 quests) - all CLEAN
Silicon (70DD7DB00881838A), Quartz Enriched Iron (70DD8519EEC1B004), Basic Processor (70DD8B76266B84E5), Improved Processor (70DD24314911C52A), Advanced Processor (70DD11972EEAF468): CLEAN. All five exact-match the RS lang.

### Mekanism column (4 quests) - all CLEAN
Steel (70DD8BDEB27E47C3), Fluorite (70DDCD212AE52B37), Refined Glowstone (70DDC61CE7A31EAF), Refined Obsidian (70DD872930906038): CLEAN. Material-name convention, ingot/gem icon disambiguates.

### Industrial Foregoing column (2 quests) - all CLEAN
Plastic (70DD52504B7A1FAD), Pink Slime (70DD8A8DA15CC882): CLEAN.

### Flux Networks column (1 quest) - CLEAN
Flux Dust (70DD3C94BA8BD5DD): CLEAN.

### Just Dire Things column (7 quests) - 6 CLEAN, 1 EDIT
- Ferricore (70DD094F71ACB4A4): CLEAN.
- Blazegold (70DDCDB366848F36): CLEAN.
- Celestigem (70DDAAEA0EA55AAA): CLEAN.

#### Eclipsealloy (Just Dire Things) (quest.70DDE576AB2A4D82)
- Disposition: EDIT
- Issues: terminology/factual: title "Eclipsealloy" (single word); the JDT material renders as two words, **"Eclipse Alloy"** (item "Eclipse Alloy Ingot"). The PF variant slug is `eclipsealloy` with no underscore, so `title_case` can't split it - the only column entry where the material name is a compound the slug collapses.
- BEFORE: `quest.70DDE576AB2A4D82.title: "Eclipsealloy (Just Dire Things)"`
- AFTER: `quest.70DDE576AB2A4D82.title: "Eclipse Alloy (Just Dire Things)"`
- Fix belongs in `tools/gen_completionist_chapters.py` (generated chapter).

- Blaze Ember (70DDC713FC1F7A30): CLEAN.
- Voidflame (70DD39115A47C69E): CLEAN.
- Eclipse Ember (70DD37EF0BD0D556): CLEAN. (Note the contrast: `eclipse_ember` HAS the underscore so it splits correctly to "Eclipse Ember", while sibling `eclipsealloy` does not - confirming the fix is a per-slug display override, not a title_case change.)

### Sister Ponds (capstone) (quest.70DD831A136C804F)
- Disposition: CLEAN
- Title "Sister Ponds", subtitle "Diplomacy, by froglight.", desc "Every modded resource the loaded mods taught your frogs - one column per neighbor. The sister ponds send their regards." All ASCII (the " - " is a hyphen, not an em/en dash), color codes none/balanced, voice on-register. No change.

## Generator-level recommendation (the actual fix)

All 5 EDIT findings share one root cause and one fix. Add a display-name override map mirroring `ICON_OVERRIDES`, consulted before `title_case` at generator lines 283 and 322:

```python
# Display-name overrides: variants whose in-game name differs from title_case(slug).
# Powah crystals carry a "Crystal" suffix; JDT eclipsealloy is two words in-game.
TITLE_OVERRIDES = {
    "blazing": "Blazing Crystal",
    "niotic": "Niotic Crystal",
    "spirited": "Spirited Crystal",
    "nitro": "Nitro Crystal",
    "eclipsealloy": "Eclipse Alloy",
}
```

Then at line 322 (Sister Ponds) and line 283 (Whole Pond, for parity if any vanilla variant ever needs it):
`disp = TITLE_OVERRIDES.get(name) or title_case(name)` and emit `"{disp} ({MOD_LABELS[mod]})"`.
Re-run `python tools/gen_completionist_chapters.py`; ids are deterministic so completion survives. (whole_pond has no affected variants today, but adding the lookup there too keeps the two census chapters consistent for future roster growth.)

## Chapter summary
- Quests: 35 total (34 census + 1 capstone), 5 EDIT, 30 CLEAN.
- Accuracy bugs (WRONG ledger rows): 5 - all title display-name drift from the mod jar:
  1. "Blazing (Powah)" should be "Blazing Crystal (Powah)" (item is "Blazing Crystal").
  2. "Niotic (Powah)" should be "Niotic Crystal (Powah)".
  3. "Spirited (Powah)" should be "Spirited Crystal (Powah)".
  4. "Nitro (Powah)" should be "Nitro Crystal (Powah)".
  5. "Eclipsealloy (Just Dire Things)" should be "Eclipse Alloy (Just Dire Things)" (in-game material is two words "Eclipse Alloy").
- Highest-severity finding: the 4 Powah crystal titles + the eclipsealloy title don't match the item names the player holds; all 5 trace to `title_case(slug)` and must be fixed via a `TITLE_OVERRIDES` map in `tools/gen_completionist_chapters.py`, never a direct lang edit (regen would wipe it).
- Nothing unverifiable: all 34 display names were ground-truthed against the mod jars' `en_us.json`; icon ids and MOD_LABELS are all correct.
