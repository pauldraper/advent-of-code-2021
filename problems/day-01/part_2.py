#!/usr/bin/env python3
import sys

values = tuple(map(int, sys.stdin))
increases = sum(v < values[i + 3] for i, v in enumerate(values) if i + 3 < len(values))
print(increases)
