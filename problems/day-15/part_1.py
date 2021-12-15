#!/usr/bin/env python3.10
import functools
import sys

data = {
    (i, j): int(v) for i, row in enumerate(sys.stdin) for j, v in enumerate(row.strip())
}


@functools.cache
def dist(i, j, d=0):
    if not i and not j:
        return 0
    if 400 < d:
        return float("inf")
    d += 1
    try:
        v = data[(i, j)]
    except KeyError:
        return float("inf")
    return v + min(
        dist(i - 1, j, d), dist(i, j - 1, d), dist(i, j + 1, d), dist(i + 1, j, d)
    )


print(dist(*max(data.keys())))
