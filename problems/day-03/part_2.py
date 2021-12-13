#!/usr/bin/env python3
import itertools
import sys

lines = [line.strip() for line in sys.stdin]


def common_number(digit):
    numbers = lines
    for i in itertools.count():
        count = sum(n[i] == "1" for n in numbers)
        numbers = [
            number
            for number in numbers
            if (len(numbers) / 2 <= count) == (number[i] == digit)
        ]
        if len(numbers) == 1:
            return int(numbers[0], 2)


oxygen = common_number("1")
co2 = common_number("0")
print(oxygen * co2)
