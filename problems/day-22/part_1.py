#!/usr/bin/env python3
import sys

cubes = set()

for line in sys.stdin:
    status, positions = line.split()
    x, y, z = positions.split(",")
    x1, x2 = map(int, x.split("=")[1].split(".."))
    y1, y2 = map(int, y.split("=")[1].split(".."))
    z1, z2 = map(int, z.split("=")[1].split(".."))

    for x in range(max(-50, x1), min(x2, 50) + 1):
        for y in range(max(-50, y1), min(y2, 50) + 1):
            for z in range(max(-50, z1), min(z2, 50) + 1):
                if status == "on":
                    cubes.add((x, y, z))
                else:
                    cubes.discard((x, y, z))

print(len(cubes))
