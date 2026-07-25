"""Shared access to the Iron Jetpacks tier ladder (which coil each jetpack takes).

One consumer today:
  - tools/validate_quests.py (Q-JETPACK-COIL diffs the Take Flight chapter's copy
    AGAINST the live tier table, so the #233 drift class is caught by machine)

Why this module exists at all: Iron Jetpacks does NOT assign coils by name. It
generates its recipes in code (DynamicRecipeManager) and picks a coil from the
jetpack's POSITION in the registered-tier list:

    r = index(tier) / len(tiers)
    r > 0.75 -> ultimate,  r > 0.5 -> elite,  r > 0.25 -> advanced,  else basic

Tiers <= -1 (the creative jetpack) are never added to that list, and a jetpack
with "disable": true is never registered at all - so disabling ONE jetpack can
drop a whole tier and silently re-map which coil every OTHER jetpack needs.
That is what made #233 possible: the Take Flight chapter said the Iron Jetpack
takes a Basic Coil when the real answer, at this pack's tier spread, is the
Advanced one. Nothing in the pack repo shows this; you have to compute it.

Source of truth, in precedence order:
  1. pack/config/ironjetpacks/jetpacks/*.json - anything the PACK ships (packwiz
     overwrites the instance copy, so a shipped file wins).
  2. <dev instance>/config/ironjetpacks/jetpacks/*.json - the mod's generated
     defaults, i.e. what a player actually gets when the pack ships no override.

The pack currently ships none of (1), so (2) is the live answer. Callers that can
proceed without the data (the validator) treat None as "skip with INFO", matching
tools/pf_jar.py - CI has no dev instance and must not fail on its absence.
"""

from __future__ import annotations

import json
import os

_REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_PACK_DIR = os.path.join(_REPO, "pack", "config", "ironjetpacks", "jetpacks")

_INSTANCE_DIRS = [
    os.path.expanduser("~/curseforge/minecraft/Instances/Sky Frogs/config/ironjetpacks/jetpacks"),
    "C:/Users/User/curseforge/minecraft/Instances/Sky Frogs/config/ironjetpacks/jetpacks",
]

COILS = ("basic", "advanced", "elite", "ultimate")


def _read_dir(path: str) -> dict[str, dict]:
    """{jetpack name: its config dict} for one directory, or {} if unreadable."""
    out: dict[str, dict] = {}
    if not os.path.isdir(path):
        return out
    for entry in sorted(os.listdir(path)):
        if not entry.endswith(".json"):
            continue
        try:
            with open(os.path.join(path, entry), encoding="utf-8") as fh:
                data = json.load(fh)
        except (OSError, ValueError):
            continue
        name = data.get("name") or entry[: -len(".json")]
        out[name] = data
    return out


def find_config_dir(explicit: str | None = None) -> str | None:
    """The dev instance's jetpack config dir, or None. `explicit` wins."""
    if explicit:
        return explicit if os.path.isdir(explicit) else None
    for d in _INSTANCE_DIRS:
        if os.path.isdir(d):
            return d
    return None


def load_jetpacks(explicit_dir: str | None = None) -> dict[str, dict] | None:
    """{name: config} with any pack-shipped override layered on top, or None.

    None means "no instance config found" - the caller decides whether that is a
    clean skip (validator) or fatal. A pack-shipped file for a jetpack the
    instance has never generated is still honoured: packwiz would place it.
    """
    instance_dir = find_config_dir(explicit_dir)
    pack = _read_dir(_PACK_DIR)
    if instance_dir is None:
        return dict(pack) if pack else None
    merged = _read_dir(instance_dir)
    merged.update(pack)
    return merged or None


def _tier(cfg: dict) -> int | None:
    """A config's tier as an int, or None if it is missing or malformed.

    Hand-edited or partially-written configs happen, and this module backs a
    pre-commit validator - a stray string tier must degrade to "ignore that
    jetpack", never crash the commit hook for an unrelated quest edit.
    """
    try:
        return int(cfg.get("tier"))
    except (TypeError, ValueError):
        return None


def registered_tiers(jetpacks: dict[str, dict]) -> list[int]:
    """The sorted tier list the mod builds at registration.

    Mirrors JetpackRegistry.register: a jetpack with "disable": true is never
    registered, and only tiers > -1 join the list (so the creative jetpack's -1
    is excluded). Duplicates collapse - several jetpacks share a tier.
    """
    tiers = set()
    for cfg in jetpacks.values():
        if cfg.get("disable", False):
            continue
        tier = _tier(cfg)
        if tier is not None and tier > -1:
            tiers.add(tier)
    return sorted(tiers)


def coil_for_tier(tier: int, tiers: list[int]) -> str | None:
    """Which coil a jetpack of `tier` needs, or None if that tier is unregistered.

    Exactly JetpackRegistry.getCoilForTier, including its float division and its
    strict > comparisons (a ratio of exactly 0.25 is BASIC, not advanced - the
    boundary matters: with a 4-tier ladder it is what pushes the second rung back
    down onto the basic coil).
    """
    if tier not in tiers or not tiers:
        return None
    ratio = float(tiers.index(tier)) / float(len(tiers))
    if ratio > 0.75:
        return "ultimate"
    if ratio > 0.5:
        return "elite"
    if ratio > 0.25:
        return "advanced"
    return "basic"


def coil_for(name: str, jetpacks: dict[str, dict]) -> str | None:
    """Which coil the named jetpack needs, or None if absent/disabled."""
    cfg = jetpacks.get(name)
    if cfg is None or cfg.get("disable", False):
        return None
    tier = _tier(cfg)
    if tier is None:
        return None
    return coil_for_tier(tier, registered_tiers(jetpacks))


def lowest_tier_jetpacks(jetpacks: dict[str, dict]) -> list[str]:
    """Names at the lowest registered tier - the ONLY ones craftable from parts.

    Every other jetpack is a JetpackUpgradeRecipe taking the tier below it, so
    this is the set the quest copy's "crafted from scratch" claim describes.
    """
    tiers = registered_tiers(jetpacks)
    if not tiers:
        return []
    return sorted(
        n for n, c in jetpacks.items()
        if not c.get("disable", False) and _tier(c) == tiers[0]
    )


def tiers_below(name: str, jetpacks: dict[str, dict]) -> list[str]:
    """Names one registered tier below `name` - what its upgrade recipe accepts."""
    cfg = jetpacks.get(name)
    if cfg is None or cfg.get("disable", False):
        return []
    tier = _tier(cfg)
    if tier is None:
        return []
    target = tier - 1
    return sorted(
        n for n, c in jetpacks.items()
        if not c.get("disable", False) and _tier(c) == target
    )
