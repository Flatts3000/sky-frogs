# Branding

> **Status:** DRAFT — non-canonical except for the **category color palette**, which mirrors the load-bearing `Category.tintArgb()` source-of-truth in Productive Frogs (`src/main/java/com/flatts/productivefrogs/data/Category.java`). The palette is fixed because PF enforces it at runtime; everything else (typography, asset list, mood guidelines) is a first-pass proposal.

The brief for anyone producing visual assets for Sky Frogs — logos, banners, hero shots, panoramas, screenshots, social cards. The goal is for art assets to feel like they belong to the same pack and reinforce the category-based progression mechanic without contradicting it.

## Identity in one sentence

**Vanilla-feeling skyblock where six categories of breedable frogs replace mining.** The aesthetic is friendly, slightly whimsical (frogs!), grounded in vanilla Minecraft palette and forms — not a "dark/edgy modpack" and not a "cutesy cartoon." Closer to vanilla's own promotional art than to most NeoForge tech packs.

## Color palette

### Category accent colors (authoritative)

These six colors come directly from Productive Frogs' `Category` enum. Any per-category branding (chapter banner, category icon, tier badge, frog silhouette) **must** use these exact hex values. Mod-side tinting renders frogs, slimes, eggs, and Configurable Froglights with these tints at runtime — branding that diverges will look wrong in-game.

| Category   | Hex       | RGB             | Use                                                          |
|------------|-----------|-----------------|--------------------------------------------------------------|
| Metallic   | `#808088` | (128, 128, 136) | Tier 1 — iron / copper / gold tones, cool gray               |
| Mineral    | `#B5651D` | (181, 101, 29)  | Tier 2 — redstone / coal / earth tones, saddle brown         |
| Gem        | `#7EE8FA` | (126, 232, 250) | Tier 3 — diamond / amethyst / certus, light cyan sparkle     |
| Aquatic    | `#70C7B8` | (112, 199, 184) | Tier 4 — prismarine / kelp / sea, soft sea green             |
| Infernal   | `#C73E1D` | (199, 62, 29)   | Tier 5 — blaze / magma / nether, fire red                    |
| Arcane     | `#9070D0` | (144, 112, 208) | Tier 6 — ender / chorus / end, royal purple                  |

### Parent slime tints (secondary palette)

The four PF parent slime species ship with their own outer-layer tints. These are useful as secondary accents when illustrating the parent → resource slime infusion mechanic, but they're not load-bearing for general branding.

| Parent species | Hex       | Maps to category |
|----------------|-----------|------------------|
| Cave Slime     | `#8A8A8A` | Mineral          |
| Geode Slime    | `#6CDCD7` | Gem              |
| Tide Slime     | `#3F76E4` | Aquatic          |
| Void Slime     | `#5E3782` | Arcane           |

(Metallic uses vanilla slimes infused with metals; Infernal uses vanilla magma cubes. No custom parent species there.)

### Neutrals

| Role            | Hex       | Notes                                                     |
|-----------------|-----------|-----------------------------------------------------------|
| Background dark | `#1A1A1F` | The void. Backdrop for skyblock-themed scenes.            |
| Background mid  | `#2D3038` | Card / panel backgrounds in cover art.                     |
| Foreground light| `#E8E8EC` | Body text on dark; off-white, not pure white.              |
| Accent gold     | `#F5C04A` | Sparing — call-to-action highlights, Master Frog trophy.   |

## Asset inventory

### Required for v0.1 launch

| Asset                 | Dimensions     | Format        | Where it ships                                                |
|-----------------------|----------------|---------------|---------------------------------------------------------------|
| Pack icon             | 256×256        | PNG, ≤500 KB  | `pack/icon.png` — launcher profile thumbnail                  |
| CurseForge logo       | 256×256        | PNG           | CF project page header                                        |
| CurseForge banner     | 512×288        | PNG           | CF project page banner                                        |
| Hero / cover          | 1280×720       | PNG or JPG    | CF gallery first slide, GitHub README hero                    |
| Gallery screenshots   | 1920×1080      | PNG or JPG    | CF gallery (6 slots — see `docs/curseforge_page.md` capture order) |
| Social card (OG)      | 1200×630       | PNG           | Open Graph preview for GitHub / shares                        |

### Nice-to-have for v0.1

| Asset                 | Dimensions     | Format        | Where it ships                                                |
|-----------------------|----------------|---------------|---------------------------------------------------------------|
| Demo gif              | 640×360, ≤5s   | GIF, ≤3 MB    | CF page mid-body, README, social posts                        |

### Deferred to v1.x (in-game presentation)

| Asset                 | Dimensions     | Format        | Where it ships                                                |
|-----------------------|----------------|---------------|---------------------------------------------------------------|
| Title-screen panorama | 6× 1024×1024   | PNG cubemap   | `pack/kubejs/assets/skyfrogs/textures/gui/title/background/panorama_{0..5}.png` |
| Main menu logo overlay| 512×128        | PNG           | Via `packmenu` mod config                                     |
| Loading screen background | 1920×1080  | PNG           | Via `packmenu`                                                |

## Logo guidelines

The pack identifier is the frog silhouette. Strong reads at 256×256 thumbnail size; readable at 64×64 favicon size. Mark must work in three contexts:

1. **Color** — primary use, full category palette across multiple frogs.
2. **Single-color** — black or off-white, for embeds, social avatars, terminal output.
3. **Reverse** — light on dark, for the launcher profile icon over the void background.

The wordmark "Sky Frogs" pairs to the right of the silhouette (horizontal lockup) or below (stacked lockup, square crop).

Avoid:
- Photo-realistic frog renderings — clashes with Minecraft's blocky idiom.
- Multiple frogs overlapping — at small sizes they smear into a blob.
- Drop shadows under the wordmark — vanilla Minecraft uses crisp text, no shadow-on-shadow.

## Typography

- **Headings** — Minecraft's title font (`Mojangles` / `Minecraftia`) for any in-game-feeling UI. For web/CF pages: **Inter Bold** or a similar geometric sans is fine.
- **Body** — system sans (CurseForge handles this; don't fight it). On the GitHub README, default markdown rendering.
- **Code / commands** — monospace, no special treatment.

Avoid hand-lettered, frog-themed display fonts. The whimsy comes from the frogs themselves; the lettering should stay quiet.

## Hero shot composition

The CF gallery's first slide is the highest-leverage single asset. It should immediately communicate:

1. **It's a skyblock.** Void background, finite island in frame.
2. **There are frogs.** At least one Resource Frog visible, ideally mid-loop (next to a Frog Egg, or eating a slime).
3. **Resources flow.** A Configurable Froglight item entity or a hopper-collected stack visible.

Composition target: rule-of-thirds, frog as focal subject, void background giving the eye a place to rest, one tier color dominant (probably Metallic or Gem — both photograph well).

## Gallery capture order

Tracked in `docs/curseforge_page.md`. Recap:

1. Hero — void skyblock starter island.
2. Tier 1 enclosure — Metallic Frog setup with Iron Slimes.
3. Tier 3 multi-enclosure — Gem Frog setups in a row.
4. Endgame singularity altar.
5. Quest book UI open to a tier chapter.
6. Tier 5/6 set piece — Nether arena or End dimension.

Capture order matches when each tier becomes playable. Tier 1 first (unblocked at v0.1 alpha); the rest as later tiers go live.

## Demo gif guidelines

Target ~5 seconds, ~3 MB. Show the core loop in one continuous sweep:

```
1.0s — frog visible, player approaches with a glass bottle
2.0s — bottle slimeball spawn → frog eats slime
3.5s — Configurable Froglight drops, hopper collects
5.0s — output ingot count ticks up in player inventory
```

No text overlays. No music. The mechanic should be self-evident; if it needs caption explanation, the gif is failing.

## Mood: what Sky Frogs is not

- **Not grimdark.** No skulls, no chains, no "INSIDE: hell" framing.
- **Not corporate cute.** No mascot eyes with sparkles, no hover-bouncing logos.
- **Not retro pixel-art-for-its-own-sake.** Minecraft itself is pixel-art; doubling down with chunky 8-bit promo art reads as derivative.
- **Not crowded.** A hero shot with one frog and one Froglight beats a shot with twelve enclosures and a singularity altar.

## File organization

Final art assets live under `pack/branding/` (gitignored if any contain proprietary source files; PNG/JPG/GIF deliverables are fine to commit). Working files (Aseprite, Affinity, Figma, etc.) live wherever the artist prefers — out of repo.

```
pack/
├── icon.png                              # launcher profile thumbnail
└── branding/
    ├── logo/
    │   ├── logo_color.png                # 256×256 master
    │   ├── logo_color_horiz.png          # horizontal lockup
    │   ├── logo_mono.png                 # single-color
    │   └── logo_reverse.png              # light on dark
    ├── cf_page/
    │   ├── header.png                    # 512×288
    │   ├── hero.png                      # 1280×720
    │   └── gallery_*.png                 # 1920×1080
    ├── social/
    │   └── og_card.png                   # 1200×630
    └── demo.gif                          # ~5s, ~3 MB
```

## Open branding questions

- **Who produces the assets?** Defer — could be Flatts, a commissioned designer, or AI-assisted with hand-polish. The brief is the same regardless.
- **Is there a tagline lockup** (logo + "skyblock where frogs replace mining" as a combined mark), or does the tagline always sit free? Defer until logo concepts exist.
- **Mascot for social media** (a specific named hero frog, à la Industrial Foregoing's pink slime guy)? Probably skip — the six-category structure is the brand; picking a single mascot frog would imply one tier matters more than the rest.
- **Animated logo / lottie** for the GitHub README hero? Defer post-v0.1.
