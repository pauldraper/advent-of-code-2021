#!/usr/bin/env pypy3
import functools
import sys

algorithm = list(c == "#" for c in next(sys.stdin).strip())
next(sys.stdin)


def next_pixel(values):
    n = functools.reduce(lambda n, v: 2 * n + v, values)
    return algorithm[n]


image = {
    (i, j): c == "#"
    for i, line in enumerate(sys.stdin)
    for j, c in enumerate(line.strip())
}

default = False
for r in range(2):
    new_image = {}
    min_i = min(i for i, _ in image)
    max_i = max(i for i, _ in image)
    min_j = min(j for _, j in image)
    max_j = max(j for _, j in image)
    for i in range(min_i - 2, max_i + 2 + 1):
        for j in range(min_j - 2, max_j + 2 + 1):
            new_image[(i, j)] = next_pixel(
                image.get((k, l), default)
                for k in range(i - 1, i + 1 + 1)
                for l in range(j - 1, j + 1 + 1)
            )
    default = next_pixel([default] * 9)
    image = new_image

print(sum(image.values()))
