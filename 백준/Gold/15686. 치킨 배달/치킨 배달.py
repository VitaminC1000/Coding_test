import sys
from copy import deepcopy
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

house = [(i, j) for i in range(n) for j in range(n) if city[i][j] == 1] # 모든 집
chicken = [(i, j) for i in range(n) for j in range(n) if city[i][j] == 2] # 모든 치킨 집

m_chicken = combinations(chicken, m) # m개의 조합 생성

minimum = 1e10

def check(current_chicken):
    global house

    ans = 0

    for h in house:
        temp = 1e10
        
        for c in current_chicken:
            l = abs(h[0] - c[0]) + abs(h[1] - c[1]) # 현재 집과 치킨 집의 치킨 거리
            temp = min(temp, l) # 이전 결과보다 작으면 포함

        ans += temp # 각 집의 치킨 거리 추가 (도시의 치킨 거리)
    
    return ans

for c in m_chicken:
    ans = check(c)
    minimum = min(minimum, ans) # 도시의 치킨 거리 중 최소값 저장
    
print(minimum)
