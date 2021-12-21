#!/usr/bin/env python3.10
import functools

pos = (10, 3)


@functools.cache
def f(pos, scores=(0, 0), turn=0, rolls=0):
    wins = [0, 0]
    if 21 <= scores[0]:
        wins[0] += 1
    elif 21 <= scores[1]:
        wins[1] += 1
    else:
        for roll in range(1, 4):
            n_rolls = (rolls + 1) % 3
            n_pos = list(pos)
            n_pos[turn] = (n_pos[turn] + roll - 1) % 10 + 1
            n_scores = list(scores)
            if not n_rolls:
                n_scores[turn] += n_pos[turn]
            n_turn = turn if n_rolls else 1 - turn
            result = f(tuple(n_pos), tuple(n_scores), n_turn, n_rolls)
            for i, w in enumerate(result):
                wins[i] += w
    return wins


print(max(f(pos)))
