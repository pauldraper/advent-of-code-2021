#!/usr/bin/env python3
import itertools
import sys

data = {
    (i, j): int(v)
    for i, line in enumerate(sys.stdin)
    for j, v in enumerate(line.strip())
}

for step in itertools.count(1):
    for p in data:
        data[p] += 1

    flashed = True
    while flashed:
        flashed = False
        for i, j in data:
            if data[(i, j)] <= 9:
                continue
            flashed = True
            data[(i, j)] = 0
            for k in range(i - 1, i + 2):
                for l in range(j - 1, j + 2):
                    if data.get((k, l)):
                        data[(k, l)] += 1

    if not sum(data.values()):
        break

print(step)
