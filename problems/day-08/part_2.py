#!/usr/bin/env python3
import sys

sum_ = 0

for line in sys.stdin:
    numbers, outputs = (list(map(set, part.split())) for part in line.split(" | "))

    one = next(n for n in numbers if len(n) == 2)
    seven = next(n for n in numbers if len(n) == 3)
    four = next(n for n in numbers if len(n) == 4)
    eight = next(n for n in numbers if len(n) == 7)
    nine = next(n for n in numbers if len(n) == 6 and four < n)
    zero = next(n for n in numbers if len(n) == 6 and n != nine and one < n)
    six = next(n for n in numbers if len(n) == 6 and n != zero and n != nine)
    three = next(n for n in numbers if len(n) == 5 and one < n)
    five = next(n for n in numbers if len(n) == 5 and n != three and n < nine)
    two = next(n for n in numbers if len(n) == 5 and n != three and n != five)

    key = [zero, one, two, three, four, five, six, seven, eight, nine]

    sum_ += int("".join(str(key.index(o)) for o in outputs))

print(sum_)
