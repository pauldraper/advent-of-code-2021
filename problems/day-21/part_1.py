#!/usr/bin/env python3
import itertools

pos = [10, 3]

score = [0, 0]
die = 1
for n in itertools.count():
    turn = n % 2
    for _ in range(3):
        pos[turn] = (pos[turn] + die - 1) % 10 + 1
        die = die % 100 + 1
    score[turn] += pos[turn]
    if 1000 <= score[turn]:
        print(score[1 - turn] * (n + 1) * 3)
        break
