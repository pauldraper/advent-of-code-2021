#!/usr/bin/env python3
import collections
import sys

counts = collections.defaultdict(int)

for line in sys.stdin:
    a, b = line.split(" -> ")
    ax, ay = map(int, a.split(","))
    bx, by = map(int, b.split(","))

    if ax == bx:
        for i in range(min(ay, by), max(ay, by) + 1):
            counts[(ax, i)] += 1

    if ay == by:
        for i in range(min(ax, bx), max(ax, bx) + 1):
            counts[(i, ay)] += 1

print(sum(c > 1 for c in counts.values()))
