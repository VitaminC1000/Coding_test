from itertools import combinations
import sys

input = sys.stdin.readline
n = int(input().strip())
ability = [list(map(int, input().split())) for _ in range(n)]

minimum = 1e5

def total_ability(team):
    return sum(ability[i][j] + ability[j][i] for i, j in combinations(team, 2))

players = list(range(n))

for sta in combinations(players, n // 2):
    lin = [x for x in players if x not in sta]
    diff = abs(total_ability(sta) - total_ability(lin))
    minimum = min(minimum, diff)

print(minimum)