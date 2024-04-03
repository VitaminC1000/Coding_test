import sys
from itertools import product

n, m = map(int, sys.stdin.readline().split())

arr = product(list(range(1, n + 1)), repeat = m)

for l in arr:
    print(*l)