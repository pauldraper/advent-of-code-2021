#!/usr/bin/env pypy3
import functools
import sys

pos = "DDDC" "CBCA" "AABB" "BCAD" "..........."

adj = [
    [1],  # 0
    [0, 2],  # 1
    [1, 3],  # 2
    [2, 18],  # 3
    [5],  # 4
    [4, 6],  # 5
    [5, 7],  # 6
    [6, 20],  # 7
    [9],  # 8
    [8, 10],  # 9
    [9, 11],  # 10
    [10, 22],  # 11
    [13],  # 12
    [12, 14],  # 13
    [13, 15],  # 14
    [14, 24],  # 15
    [17],  # 16
    [16, 18],  # 17
    [17, 19, 3],  # 18
    [18, 20],  # 19
    [19, 21, 7],  # 20
    [20, 22],  # 21
    [21, 23, 11],  # 22
    [22, 24],  # 23
    [23, 25, 15],  # 24
    [24, 26],  # 25
    [25],  # 26
]

answer = "AAAA" "BBBB" "CCCC" "DDDD" "..........."


@functools.lru_cache(maxsize=None)
def solve(pos):
    if pos == answer:
        return 0

    result = float("inf")

    for i, c in enumerate(pos):
        if c == ".":
            continue

        if i < 4:
            if all(p == "A" for p in pos[0 : i + 1]):
                continue
        elif i < 8:
            if all(p == "B" for p in pos[4 : i + 1]):
                continue
        elif i < 12:
            if all(p == "C" for p in pos[8 : i + 1]):
                continue
        elif i < 16:
            if all(p == "D" for p in pos[12 : i + 1]):
                continue

        dist = {}

        def visit(i, cost):
            if i in dist:
                return
            if pos[i] != ".":
                return
            dist[i] = cost
            for a in adj[i]:
                visit(a, cost + 1)

        for a in adj[i]:
            visit(a, 1)

        for a, d in dist.items():
            if a in (i, 18, 20, 22, 24):
                continue
            if a < 4:
                if c != "A" or any(p != "A" for p in pos[0:a]):
                    continue
            elif a < 8:
                if c != "B" or any(p != "B" for p in pos[4:a]):
                    continue
            elif a < 12:
                if c != "C" or any(p != "C" for p in pos[8:a]):
                    continue
            elif a < 16:
                if c != "D" or any(p != "D" for p in pos[12:a]):
                    continue
            elif 16 <= i:
                continue

            new_pos = "".join(
                c if j == a else "." if j == i else p for j, p in enumerate(pos)
            )
            cost = d * (
                1 if c == "A" else 10 if c == "B" else 100 if c == "C" else 1000
            )

            result = min(result, cost + solve(new_pos))

    return result


print(solve(pos))
