#!/usr/bin/env python3
import sys

values = tuple(map(int, sys.stdin))
increases = sum(v < values[i + 1] for i, v in enumerate(values) if i + 1 < len(values))
print(increases)
