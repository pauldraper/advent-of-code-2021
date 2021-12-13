#!/usr/bin/env python3
import sys

points = []
for line in sys.stdin:
    if line == "\n":
        break
    x, y = map(int, line.split(","))
    points.append((x, y))

direction, n = next(sys.stdin).split()[2].split("=")
n = int(n)

new_points = set()
for (x, y) in points:
    if direction == "x":
        new_points.add((x, y) if x < n else (2 * n - x, y))
    if direction == "y":
        new_points.add((x, y) if y < n else (x, 2 * n - y))

print(len(new_points))
