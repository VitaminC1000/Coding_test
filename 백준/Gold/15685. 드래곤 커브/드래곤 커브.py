import sys

N = int(input())  # 드래곤 커브의 개수
curves = [list(map(int, input().split())) for _ in range(N)]

grid = [[False] * 101 for _ in range(101)]

# 이동 방향: 우(0), 상(1), 좌(2), 하(3)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for x, y, d, g in curves:
    directions = [d]  # 초기 방향
    grid[y][x] = True  # 시작점
    x, y = x + dx[d], y + dy[d]  # 다음 점
    grid[y][x] = True
    
    for _ in range(g):  # 각 세대에 대해
        temp = []
        for d in reversed(directions):  # 방향을 뒤집어서 90도 회전
            nd = (d + 1) % 4
            x, y = x + dx[nd], y + dy[nd]
            grid[y][x] = True
            temp.append(nd)
        directions.extend(temp)  # 새로운 방향 추가

# 정사각형 찾기
answer = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] and grid[i][j+1] and grid[i+1][j] and grid[i+1][j+1]:
            answer += 1

print(answer)