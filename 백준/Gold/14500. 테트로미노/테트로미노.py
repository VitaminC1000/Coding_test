import sys

input = sys.stdin.readline
n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
maximum = 0

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check_range(x, y):
    return 0 <= x < n and 0 <= y < m

def tetromino(x, y, cnt, temp):
    global maximum

    if cnt == 4:
        maximum = max(maximum, temp)
        return
    
    if not check_range(x, y) or visited[x][y]:
        return

    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if check_range(nx, ny) and not visited[nx][ny]:
            tetromino(nx, ny, cnt + 1, temp + array[nx][ny])

    visited[x][y] = False

# 'ㅗ' 모양을 위한 별도의 함수
def special_shape(x, y):
    global maximum

    for i in range(4):
        temp = array[x][y]

        for j in range(3):
            t = (i + j) % 4
            nx = x + dx[t]
            ny = y + dy[t]

            if not check_range(nx, ny):
                temp = 0
                break

            temp += array[nx][ny]
            
        maximum = max(maximum, temp)

for i in range(n):
    for j in range(m):
        tetromino(i, j, 1, array[i][j])  # cnt를 1로 시작, temp는 시작 위치의 값을 가짐
        special_shape(i, j)  # 'ㅗ' 모양 탐색

print(maximum)