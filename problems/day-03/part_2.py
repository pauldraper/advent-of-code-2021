#!/usr/bin/env python3
import sys

lines = []
for line in sys.stdin:
    lines.append(line.strip())


def counts(numbers):
    data = None
    for number in numbers:
        if not data:
            data = [0] * len(number)
        for i, digit in enumerate(number):
            data[i] += digit == "1"
    return data


oxygen_numbers = list(lines)
i = 0
while 1 < len(oxygen_numbers):
    c = counts(oxygen_numbers)
    oxygen_numbers = [
        number
        for number in oxygen_numbers
        if (len(oxygen_numbers) / 2 <= c[i]) == (number[i] == "1")
    ]
    i += 1

co2_numbers = list(lines)
i = 0
while 1 < len(co2_numbers):
    data = counts(co2_numbers)
    co2_numbers = [
        number
        for number in co2_numbers
        if (len(co2_numbers) / 2 <= data[i]) == (number[i] == "0")
    ]
    i += 1

oxygen = int(oxygen_numbers[0], 2)
co2 = int(co2_numbers[0], 2)

print(oxygen * co2)
