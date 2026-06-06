"""Shared access to the pinned Productive Frogs jar (the pack's ground truth).

Two consumers:
  - tools/gen_singularities.py (writes the committed singularity JSONs from variant data)
  - tools/validate_quests.py (Q-SINGULARITY-INGREDIENT / Q-DISSOLUTION-THREADING diff the
    committed pack files AGAINST that same data, so the three-places drift class - #101 -
    is caught by machine instead of maintainer memory)

The jar is looked up in the dev instance's mods folder (the post-sync_instance.py state).
Callers that can proceed without it (the validator) treat None as "skip with INFO";
callers that cannot (the generator) exit.
"""

from __future__ import annotations

import glob
import json
import os
import zipfile

VARIANT_PREFIX = "data/productivefrogs/productivefrogs/slime_variant/"

_JAR_PATTERNS = [
    os.path.expanduser("~/curseforge/minecraft/Instances/Sky Frogs/mods/productivefrogs-*.jar"),
    "C:/Users/User/curseforge/minecraft/Instances/Sky Frogs/mods/productivefrogs-*.jar",
]


def find_jar(explicit: str | None = None) -> str | None:
    """Path to the PF jar, or None. `explicit` (e.g. --jar/--pf-jar) wins."""
    if explicit:
        return explicit if os.path.exists(explicit) else None
    for pat in _JAR_PATTERNS:
        matches = sorted(glob.glob(pat))
        if matches:
            return matches[-1]
    return None


def load_variants(jar: str) -> dict[str, dict]:
    """variant name -> its slime_variant JSON (primer_item, category, colors,
    neoforge:conditions when mod-gated, ...) straight from the jar."""
    out: dict[str, dict] = {}
    with zipfile.ZipFile(jar) as archive:
        for name in archive.namelist():
            if name.startswith(VARIANT_PREFIX) and name.endswith(".json"):
                variant = name[len(VARIANT_PREFIX):-len(".json")]
                out[variant] = json.loads(archive.read(name))
    return out


def is_vanilla(variant_data: dict) -> bool:
    """The generator's rule: vanilla = unconditioned AND a minecraft: primer."""
    primer = variant_data.get("primer_item", "")
    return "neoforge:conditions" not in variant_data and primer.startswith("minecraft:")
