#!/usr/bin/env python3
import sys

points = set()
for line in sys.stdin:
    if line == "\n":
        break
    x, y = map(int, line.split(","))
    points.add((x, y))

for line in sys.stdin:
    direction, n = line.split()[2].split("=")
    n = int(n)

    new_points = set()
    for (x, y) in points:
        if direction == "x":
            new_points.add((x, y) if x < n else (2 * n - x, y))
        if direction == "y":
            new_points.add((x, y) if y < n else (x, 2 * n - y))
    points = new_points

max_x = max(x for x, _ in points)
max_y = max(y for _, y in points)
for y in range(max_y + 1):
    print("".join("X" if (x, y) in points else " " for x in range(max_x + 1)))
