from collections import deque
import sys

input = sys.stdin.readline
n, l, r = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(n)]

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(x, y):
    q = deque([(x, y)])
    temp = []  # 연합을 이루는 국가를 저장

    while q:
        x, y = q.popleft()

        if visited[x][y]: # 이미 방문한 노드 (True)이면 다음 반복 실행
            continue

        visited[x][y] = True
        temp.append((x, y))

        for dx, dy in d:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(country[x][y] - country[nx][ny]) <= r:
                    q.append((nx, ny))

    return temp

cnt = 0

while True:
    visited = [[False] * n for _ in range(n)]
    flag = False # 인구 이동 유무 조사

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                arr = bfs(i, j)

                if len(arr) > 1:
                    flag = True # 연합의 길이가 1 이상 -> 인구 이동 유!
                    new_pop = sum(country[x][y] for x, y in arr) // len(arr)

                    for x, y in arr:
                        country[x][y] = new_pop

    if not flag: # 인구 이동이 없었을 경우 (False)
        break

    cnt += 1

print(cnt)
