import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())

arr = permutations(list(range(1, n + 1)), m)

for l in arr:
    if len(l) == len(set(l)):
        print(*l)