N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
nutrients = [[5]*N for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

for _ in range(K):
    # 봄과 여름
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                trees[i][j].sort()
                alive, dead = [], 0
                for age in trees[i][j]:
                    if nutrients[i][j] >= age:
                        nutrients[i][j] -= age
                        alive.append(age + 1)
                    else:
                        dead += age // 2
                trees[i][j] = alive
                nutrients[i][j] += dead

    # 가을
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    for i in range(N):
        for j in range(N):
            for age in trees[i][j]:
                if age % 5 == 0:
                    for direction in range(8):
                        ni, nj = i + dx[direction], j + dy[direction]
                        if 0 <= ni < N and 0 <= nj < N:
                            trees[ni][nj].insert(0, 1)  # 번식

    # 겨울
    for i in range(N):
        for j in range(N):
            nutrients[i][j] += A[i][j]

ans = sum(len(trees[i][j]) for i in range(N) for j in range(N))
print(ans)
