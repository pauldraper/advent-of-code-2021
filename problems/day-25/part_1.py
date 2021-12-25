#!/usr/bin/env python3
import itertools
import sys

data = {
    (i, j): c for i, line in enumerate(sys.stdin) for j, c in enumerate(line.strip())
}
rows = max(i for i, j in data) + 1
cols = max(j for i, j in data) + 1

for n in itertools.count():
    n += 1
    move = False
    new_data = dict(data)
    for (i, j), value in data.items():
        if value == ">":
            new_j = (j + 1) % cols
            if data[(i, new_j)] == ".":
                move = True
                new_data[(i, new_j)] = ">"
                new_data[(i, j)] = "."
    data = new_data
    new_data = dict(data)
    for (i, j), value in data.items():
        if value == "v":
            new_i = (i + 1) % rows
            if data[(new_i, j)] == ".":
                move = True
                new_data[(new_i, j)] = "v"
                new_data[(i, j)] = "."
    data = new_data
    if not move:
        break
print(n)
