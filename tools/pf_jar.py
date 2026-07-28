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
import re
import zipfile

VARIANT_PREFIX = "data/productivefrogs/productivefrogs/slime_variant/"
RECIPE_PREFIX = "data/productivefrogs/recipe/"
FROGLIGHT_ITEM = "productivefrogs:configurable_froglight"
VARIANT_COMPONENT = "productivefrogs:slime_variant"

_REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_PW_TOML = os.path.join(_REPO, "pack", "mods", "productive-frogs.pw.toml")

_MODS_DIRS = [
    os.path.expanduser("~/curseforge/minecraft/Instances/Sky Frogs/mods"),
    "C:/Users/User/curseforge/minecraft/Instances/Sky Frogs/mods",
]


def pinned_filename() -> str | None:
    """The jar filename the pack PINS (pack/mods/productive-frogs.pw.toml), or None."""
    try:
        text = open(_PW_TOML, encoding="utf-8").read()
    except OSError:
        return None
    m = re.search(r'^filename\s*=\s*"([^"]+)"', text, re.M)
    return m.group(1) if m else None


def find_jar(explicit: str | None = None) -> str | None:
    """Path to the PF jar, or None. `explicit` (e.g. --jar/--pf-jar) wins.

    Auto-discovery prefers the EXACT pinned filename from the pw.toml - this both
    guarantees pin/jar agreement and sidesteps the lexicographic-version trap
    (sorted() ranks '...1.9.2.jar' after '...1.11.0.jar', so a stale leftover jar
    would win a latest-by-name pick). The bare glob is only a fallback for when
    the pw.toml is unreadable; callers that care about staleness should compare
    os.path.basename(jar) against pinned_filename().
    """
    if explicit:
        return explicit if os.path.exists(explicit) else None
    pinned = pinned_filename()
    for d in _MODS_DIRS:
        if pinned:
            exact = os.path.join(d, pinned)
            if os.path.exists(exact):
                return exact
        matches = sorted(glob.glob(os.path.join(d, "productivefrogs-*.jar")))
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


def load_froglight_resources(jar: str) -> dict[str, list[str]]:
    """variant name -> the item id(s) its Froglight SMELTS to, straight from the jar.

    This is the resource a variant's frog actually produces, and it is what the pack
    means by "the resource" everywhere (the Quantum Compressor's singularity input,
    the froglight-check law). It is NOT always the variant's ``primer_item``: the
    primer is what you feed a slime to MAKE that variant, and for `experience` the
    two diverge (primer `minecraft:book`, smelt result `minecraft:experience_bottle`)
    - which is how the Experience Singularity came to demand books (#245).

    Values are lists because a variant CAN carry more than one smelt recipe when two
    host mods each register the resource (`silicon` -> ae2 + refinedstorage). No
    vanilla variant does today; callers decide whether ambiguity is fatal. Sorted,
    so the generator's output does not depend on zip iteration order.

    The fluid pair (water / lava) has no smelting recipe at all - those Froglights
    melt in the Crucible - so both are simply absent from the mapping.
    """
    out: dict[str, set[str]] = {}
    with zipfile.ZipFile(jar) as archive:
        for name in archive.namelist():
            if not name.startswith(RECIPE_PREFIX) or not name.endswith(".json"):
                continue
            data = json.loads(archive.read(name))
            if data.get("type") != "minecraft:smelting":
                continue
            ingredient = data.get("ingredient") or {}
            if FROGLIGHT_ITEM not in (ingredient.get("items") or []):
                continue
            variant = (ingredient.get("components") or {}).get(VARIANT_COMPONENT, "")
            variant = variant.split(":")[-1]
            result = data.get("result") or {}
            result = result.get("id") if isinstance(result, dict) else result
            if variant and result:
                out.setdefault(variant, set()).add(result)
    return {variant: sorted(results) for variant, results in out.items()}


def is_vanilla(variant_data: dict) -> bool:
    """The generator's rule: vanilla = unconditioned AND a minecraft: primer."""
    primer = variant_data.get("primer_item", "")
    return "neoforge:conditions" not in variant_data and primer.startswith("minecraft:")
