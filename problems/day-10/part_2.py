#!/usr/bin/env python3
import sys

pairs = {")": "(", "]": "[", "}": "{", ">": "<"}
scores = []

for line in sys.stdin:
    stack = []
    for c in line.strip():
        try:
            other = pairs[c]
        except KeyError:
            stack.append(c)
        else:
            if not stack or stack.pop() != other:
                break
    else:
        score = 0
        for c in reversed(stack):
            score = score * 5 + "([{<".index(c) + 1
        scores.append(score)


scores.sort()

print(scores[len(scores) // 2])
