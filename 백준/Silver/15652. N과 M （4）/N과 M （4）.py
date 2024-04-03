import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().split())

arr = combinations_with_replacement(list(range(1, n + 1)), m)

for l in arr:
    print(*l)