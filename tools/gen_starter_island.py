#!/usr/bin/env python3
"""Generate the Sky Frogs starter-island structure NBT for SkyblockBuilder.

A deliberately minimal, chestless platform: a 5x5 footprint, 3 blocks deep -
two layers of dirt topped with grass_block. There is NO chest (first-join items
come from KubeJS `first_join.js`) and NO pre-placed tree (the player grows one
from the granted saplings).

Output: pack/config/skyblockbuilder/templates/islands/default.nbt
(gzipped vanilla structure NBT, DataVersion 3955 = MC 1.21.1).

Re-run after changing the island design. Requires `pip install nbtlib`.
The island is wired into worldgen via pack/config/skyblockbuilder/templates.json5.
"""
import os
import nbtlib
from nbtlib import File
from nbtlib.tag import Compound, List, String, Int

SX, SY, SZ = 5, 3, 5
DATA_VERSION = 3955  # MC 1.21.1

OUT = os.path.normpath(os.path.join(
    os.path.dirname(__file__), "..",
    "pack", "config", "skyblockbuilder", "templates", "islands", "default.nbt",
))


def build():
    palette = List[Compound]([
        Compound({"Name": String("minecraft:dirt")}),
        Compound({"Name": String("minecraft:grass_block")}),
    ])
    blocks = []
    for y in range(SY):
        state = 1 if y == SY - 1 else 0  # grass on top, dirt below
        for x in range(SX):
            for z in range(SZ):
                blocks.append(Compound({
                    "state": Int(state),
                    "pos": List[Int]([Int(x), Int(y), Int(z)]),
                }))
    return Compound({
        "size": List[Int]([Int(SX), Int(SY), Int(SZ)]),
        "palette": palette,
        "blocks": List[Compound](blocks),
        "entities": List[Compound]([]),
        "DataVersion": Int(DATA_VERSION),
    })


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    File(build()).save(OUT, gzipped=True)
    print(f"wrote {OUT} ({SX}x{SY}x{SZ})")


if __name__ == "__main__":
    main()
