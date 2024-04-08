from collections import deque

n, m = map(int, input().split())  # 보드의 크기
board = [list(input().strip()) for _ in range(n)]

# 구슬의 초기 위치와 구멍의 위치를 찾습니다.
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            red = (i, j)
        elif board[i][j] == 'B':
            blue = (i, j)
        elif board[i][j] == 'O':
            hole = (i, j)

# 네 방향에 대한 이동
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def move(x, y, dx, dy):
    count = 0  # 이동한 횟수
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

def bfs():
    q = deque([(red, blue, 1)])  # 시작 상태
    visited = set([(red, blue)])  # 방문한 상태
    while q:
        r, b, depth = q.popleft()
        if depth > 10:  # 10번 초과 이동 시 실패
            break
        for dx, dy in directions:
            nrx, nry, rc = move(r[0], r[1], dx, dy)
            nbx, nby, bc = move(b[0], b[1], dx, dy)

            if (nbx, nby) == hole:  # 파란 구슬이 구멍에 빠지면 실패
                continue
            if (nrx, nry) == hole:  # 빨간 구슬이 구멍에 빠지면 성공
                return depth

            if (nrx, nry) == (nbx, nby):  # 두 구슬이 같은 위치에 있으면
                if rc > bc:  # 더 많이 이동한 구슬을 한 칸 뒤로
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy

            if (nrx, nry, nbx, nby) not in visited:
                q.append(((nrx, nry), (nbx, nby), depth + 1))
                visited.add((nrx, nry, nbx, nby))

    return -1  # 구멍에 도달하지 못함

print(bfs())