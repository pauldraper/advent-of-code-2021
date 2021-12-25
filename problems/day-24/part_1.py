#!/usr/bin/env pypy3
import functools
import sys

ins = [line.split() for line in sys.stdin]


@functools.lru_cache(maxsize=None)
def solve(step=0, z=0):
    for input in range(9, 0, -1):
        state = [0, 0, 0, 0]

        def read(n):
            return state[ord(n) - ord("w")] if "w" <= n <= "z" else int(n)

        def write(n, v):
            state[ord(n) - ord("w")] = v

        write("z", z)
        write(ins[step][1], input)
        i = step + 1
        while True:
            if i == len(ins):
                return None if read("z") != 0 else str(input)
            n = ins[i]
            if n[0] == "inp":
                r = solve(i, read("z"))
                if r is not None:
                    return str(input) + r
                break
            elif n[0] == "add":
                write(n[1], read(n[1]) + read(n[2]))
            elif n[0] == "mul":
                write(n[1], read(n[1]) * read(n[2]))
            elif n[0] == "div":
                write(n[1], read(n[1]) // read(n[2]))
            elif n[0] == "mod":
                write(n[1], read(n[1]) % read(n[2]))
            elif n[0] == "eql":
                write(n[1], int(read(n[1]) == read(n[2])))
            i += 1


print(solve())
