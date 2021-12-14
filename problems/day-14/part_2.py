#!/usr/bin/env python3.10
import collections
import functools
import itertools
import sys

data = next(sys.stdin).strip()
next(sys.stdin)
rules = dict(line.strip().split(" -> ") for line in sys.stdin)


@functools.cache
def counts(a, b, steps):
    if steps:
        try:
            new = rules[a + b]
        except KeyError:
            pass
        else:
            return (
                counts(a, new, steps - 1)
                + counts(new, b, steps - 1)
                - collections.Counter(new)
            )
    return collections.Counter(a + b)


result = sum(
    (counts(*d, 40) for d in itertools.pairwise(data)),
    start=collections.Counter(),
)
result -= collections.Counter(data[1:-1])

max_ = max(result.values())
min_ = min(result.values())

print(max_ - min_)
