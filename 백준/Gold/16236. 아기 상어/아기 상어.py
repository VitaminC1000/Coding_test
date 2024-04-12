from collections import deque
import sys

def bfs(start, size):
    # 거리를 저장하는 그리드 초기화 (-1은 방문하지 않았음을 의미)
    distances = [[-1] * n for _ in range(n)]
    # 시작 위치를 큐에 추가하고, 해당 위치의 거리를 0으로 설정
    queue = deque([start])
    distances[start[0]][start[1]] = 0
    # 먹을 수 있는 물고기 리스트
    fish = []
    
    while queue:
        x, y = queue.popleft()
        
        # 4방향 이동 (상, 좌, 우, 하)
        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            nx, ny = x + dx, y + dy

            # 격자 범위 내에서, 방문하지 않았으며 상어 크기 이하인 경우 이동 가능
            if 0 <= nx < n and 0 <= ny < n and distances[nx][ny] == -1 and grid[nx][ny] <= size:
                distances[nx][ny] = distances[x][y] + 1
                queue.append((nx, ny))
                
                # 이동 위치에 먹을 수 있는 물고기가 있는 경우 리스트에 추가
                if 0 < grid[nx][ny] < size:
                    fish.append((distances[nx][ny], nx, ny))
                    
    # 먹을 수 있는 물고기를 거리, x좌표, y좌표 순으로 정렬
    return sorted(fish)

input = sys.stdin.readline
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

shark_size = 2
time_spent = 0
eaten = 0

# 아기 상어 초기 위치 찾기 및 초기화
shark_pos = None
for i in range(n):
    for j in range(n):
        if grid[i][j] == 9:
            shark_pos = (i, j)
            grid[i][j] = 0
            break

    if shark_pos:
        break

while True:
    # 현재 상어 위치와 크기를 기준으로 먹을 수 있는 물고기 탐색
    fishes = bfs(shark_pos, shark_size)
    if not fishes:
        break  # 먹을 수 있는 물고기가 없는 경우 종료
    
    dist, fish_x, fish_y = fishes[0]  # 가장 가까운 물고기 선택
    time_spent += dist  # 총 이동 시간에 이동 거리 추가
    eaten += 1  # 먹은 물고기 수 증가
    grid[fish_x][fish_y] = 0  # 물고기 위치 초기화
    shark_pos = (fish_x, fish_y)  # 상어 위치 갱신
    
    # 상어 크기만큼 물고기를 먹었을 경우 크기 증가
    if eaten == shark_size:
        shark_size += 1
        eaten = 0

print(time_spent)