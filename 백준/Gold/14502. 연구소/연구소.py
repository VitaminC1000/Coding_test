from itertools import combinations
from copy import deepcopy
from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())  # 연구소의 크기 입력
lab = [list(map(int, input().split())) for _ in range(n)]  # 초기 연구소 상태 입력

# 바이러스 확산 함수
def spread_virus(start_points, map):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
    queue = deque(start_points)
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and map[nx][ny] == 0:
                map[nx][ny] = 2
                queue.append((nx, ny))
    return sum(row.count(0) for row in map)  # 안전 영역의 크기 반환

# 초기 바이러스 위치 및 벽을 세울 수 있는 위치
virus_locations = [(i, j) for i in range(n) for j in range(m) if lab[i][j] == 2]
empty_locations = [(i, j) for i in range(n) for j in range(m) if lab[i][j] == 0]

answer = 0
# 벽을 세울 수 있는 모든 조합에 대해 시뮬레이션
for walls in combinations(empty_locations, 3):
    temp_lab = deepcopy(lab)
    for x, y in walls:
        temp_lab[x][y] = 1  # 벽 세우기
    answer = max(answer, spread_virus(virus_locations, temp_lab))

print(answer)