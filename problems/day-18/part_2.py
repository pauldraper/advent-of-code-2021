#!/usr/bin/env python3
import itertools
import json
import sys


def add_value(number, index, value):
    if type(number) == int:
        return number + value
    return [
        add_value(n, index, value) if i == index else n for i, n in enumerate(number)
    ]


def explode(number, depth=0):
    if type(number) == int:
        return
    if depth == 4:
        return 0, number[0], number[1]
    result = explode(number[0], depth + 1)
    if result:
        return [result[0], add_value(number[1], 0, result[2])], result[1], 0
    result = explode(number[1], depth + 1)
    if result:
        return [add_value(number[0], 1, result[1]), result[0]], 0, result[2]


def split(number):
    if type(number) == int:
        if number < 10:
            return
        return [number // 2, (number - 1) // 2 + 1]
    result = split(number[0])
    if result:
        return [result, number[1]]
    result = split(number[1])
    if result:
        return [number[0], result]


def add(a, b):
    number = [a, b]
    while True:
        result = explode(number)
        if result:
            number = result[0]
            continue
        result = split(number)
        if result:
            number = result
            continue
        break
    return number


def magnitude(n):
    if type(n) == int:
        return n
    return 3 * magnitude(n[0]) + 2 * magnitude(n[1])


numbers = [json.loads(line) for line in sys.stdin]
max_ = max(magnitude(add(*n)) for n in itertools.permutations(numbers, 2))
print(max_)
