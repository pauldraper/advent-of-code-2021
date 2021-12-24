#!/usr/bin/env pypy3
import functools
import sys


def read(state, n):
    return state[ord(n) - ord("w")] if "w" <= n <= "z" else int(n)


def write(state, n, v):
    state[ord(n) - ord("w")] = v


ins = [line.split() for line in sys.stdin]


@functools.lru_cache(maxsize=None)
def solve(step=0, z=0):
    for input in range(1, 10):
        state = [0, 0, 0, 0]
        write(state, "z", z)
        write(state, ins[step][1], input)
        i = step + 1
        while True:
            if i == len(ins):
                return None if read(state, "z") != 0 else ""
            n = ins[i]
            if n[0] == "inp":
                r = solve(i, read(state, "z"))
                if r is not None:
                    return str(input) + r
                break
            elif n[0] == "add":
                write(state, n[1], read(state, n[1]) + read(state, n[2]))
            elif n[0] == "mul":
                write(state, n[1], read(state, n[1]) * read(state, n[2]))
            elif n[0] == "div":
                write(state, n[1], read(state, n[1]) // read(state, n[2]))
            elif n[0] == "mod":
                write(state, n[1], read(state, n[1]) % read(state, n[2]))
            elif n[0] == "eql":
                write(state, n[1], int(read(state, n[1]) == read(state, n[2])))
            i += 1


print(solve())
