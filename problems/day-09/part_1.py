#!/usr/bin/env python3
import sys

data = {
    (i, j): int(v)
    for i, line in enumerate(sys.stdin)
    for j, v in enumerate(line.strip())
}

sum_ = 0
for i, j in data:
    v = data[(i, j)]
    if (
        v < data.get((i - 1, j), 9)
        and v < data.get((i, j - 1), 9)
        and v < data.get((i, j + 1), 9)
        and v < data.get((i + 1, j), 9)
    ):
        sum_ += 1 + v

print(sum_)
