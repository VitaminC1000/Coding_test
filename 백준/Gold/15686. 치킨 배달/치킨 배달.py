import sys
from copy import deepcopy
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

house = [(i, j) for i in range(n) for j in range(n) if city[i][j] == 1]
chicken = [(i, j) for i in range(n) for j in range(n) if city[i][j] == 2]

m_chicken = combinations(chicken, m)

minimum = 1e10

def check(current_chicken):
    global house

    ans = 0

    for h in house:
        temp = 1e10
        
        for c in current_chicken:
            l = abs(h[0] - c[0]) + abs(h[1] - c[1])
            temp = min(temp, l)

        ans += temp     
    
    return ans

for c in m_chicken:
    ans = check(c)
    minimum = min(minimum, ans)
    
print(minimum)