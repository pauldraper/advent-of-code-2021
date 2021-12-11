#!/usr/bin/env python3
import sys

data = {
    (i, j): int(v)
    for i, line in enumerate(sys.stdin)
    for j, v in enumerate(line.strip())
}

basins = []
for i, j in data:
    visited = set()

    def visit(i, j, last):
        try:
            v = data[(i, j)]
        except KeyError:
            return
        if v == 9 or v < last or (i, j) in visited:
            return
        visited.add((i, j))
        visit(i - 1, j, v)
        visit(i, j - 1, v)
        visit(i + 1, j, v)
        visit(i, j + 1, v)

    visit(i, j, -1)
    basins.append(len(visited))

basins.sort()

a, b, c = basins[-3:]

print(a * b * c)
