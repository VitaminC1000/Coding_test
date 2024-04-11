import sys
from copy import deepcopy

input = sys.stdin.readline
n, m, h = map(int, input().split())
ladder_hor = [list(map(int, input().split())) for _ in range(m)]

# 사다리 상태를 2차원 배열로 초기화
ladder = [[0 for _ in range(n-1)] for _ in range(h)]

# 사다리 정보를 기반으로 배열 채우기
for a, b in ladder_hor:
    ladder[a-1][b-1] = 1

# 결과를 저장할 변수, 불가능한 경우를 고려하여 초기값을 설정
minimum = 4

# 사다리를 놓을 수 있는지 검사하는 함수
def possible():
    for start in range(n):
        k = start
        for i in range(h):
            if k > 0 and ladder[i][k-1] == 1:
                k -= 1
            elif k < n-1 and ladder[i][k] == 1:
                k += 1
        if start != k:
            return False
    return True

# 사다리를 추가하는 함수, dfs 방식으로 모든 가능성 탐색
def add_ladder(cnt, x, y):
    global minimum
    if cnt >= minimum:  # 이미 찾은 최소값보다 크거나 같은 경우 탐색 중지
        return
    if possible():  # 현재 사다리 상태에서 모든 조건을 만족하는지 검사
        minimum = cnt
        return
    if cnt == 3:  # 3개 이상의 사다리는 추가하지 않음
        return
    for i in range(x, h):
        k = y if i == x else 0
        for j in range(k, n-1):
            if ladder[i][j] == 0:
                if j > 0 and ladder[i][j-1] == 1:
                    continue
                if j < n-2 and ladder[i][j+1] == 1:
                    continue
                ladder[i][j] = 1
                add_ladder(cnt+1, i, j+2)
                ladder[i][j] = 0
        y = 0

add_ladder(0, 0, 0)
print(minimum if minimum < 4 else -1)