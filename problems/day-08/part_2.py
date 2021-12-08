#!/usr/bin/env python3
import sys

sum_ = 0

for line in sys.stdin:
    
    a, b = line.split(" | ")
    
    numbers = a.split()
    outputs = b.split()

    counts = {}
    for number in numbers:
        for n in number:
            counts[n] = counts.get(n, 0) + 1

    b = next(k for k, v in counts.items() if v == 6)
    e = next(k for k, v in counts.items() if v == 4)
    f = next(k for k, v in counts.items() if v == 9)

    one = next(v for v in numbers if len(v) == 2)
    c = next(char for char in one if counts[char] == 8)

    seven = next(v for v in numbers if len(v) == 3)
    a = next(char for char in seven if char != c and char != f)

    four = next(v for v in numbers if len(v) == 4)
    d = next(char for char in four if char != b and char != c and char != f)

    eight = next(v for v in numbers if len(v) == 7)
    g = next(k for k, v in counts.items() if v == 7 and k != d)

    result = 0
    for output in outputs:
        digit = None
        if set(output) == set([a, b, c, e, f, g]):
            digit = 0
        elif set(output ) == set([c, f]):
            digit = 1
        elif set(output) == set([a, c, d, e, g]):
            digit = 2
        elif set(output) == set([a, c, d, f, g]):
            digit = 3
        elif set(output) == set([b, c, d, f]):
            digit = 4
        elif set(output) == set([a, b, d, f, g]):
            digit = 5
        elif set(output) == set([a, b, d, e, f, g]):
            digit = 6
        elif set(output) == set([a, c, f]):
            digit = 7
        elif set(output) == set([a, b, c, d, e, f, g]):
            digit = 8
        elif set(output) == set([a, b, c, d, f, g]):
            digit = 9
        else:
            print(a, b, c, d, e, f, g)
            print(counts)
            print(output)
        result = result * 10 + digit

    sum_ += result

print(sum_)
