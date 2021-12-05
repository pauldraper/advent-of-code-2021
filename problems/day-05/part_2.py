#!/usr/bin/env python3
import sys

counts = {}

for line in sys.stdin:
    a, b = line.split(" -> ")
    ax, ay = map(int, a.split(","))
    bx, by = map(int, b.split(","))

    if ax == bx:
        for i in range(min(ay, by), max(ay, by) + 1):
            p = (ax, i)
            counts[p] = counts.get(p, 0) + 1

    if ay == by:
        for i in range(min(ax, bx), max(ax, bx) + 1):
            p = (i, ay)
            counts[p] = counts.get(p, 0) + 1

    if ax - bx == ay - by:
        x = min(ax, bx)
        y = min(ay, by)
        for i in range(0, abs(ax - bx) + 1):
            p = (i + x, i + y)
            counts[p] = counts.get(p, 0) + 1

    if ax - bx == by - ay:
        x = min(ax, bx)
        y = max(ay, by)
        for i in range(0, abs(ax - bx) + 1):
            p = (x + i, y - i)
            counts[p] = counts.get(p, 0) + 1


print(sum(c > 1 for c in counts.values()))
