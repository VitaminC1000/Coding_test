import sys
from collections import deque

input = sys.stdin.readline
n = int(input().strip()) # 보드 크기

k = int(input().strip()) # 사과 개수
k_loc = [list(map(int, input().split())) for _ in range(k)] # 사과 위치

l = int(input().strip()) # 방향 변환 횟수
l_array = [list(map(str, input().split())) for _ in range(l)] # 방향 변환 시간 & 변환 방향

snake = deque([[0, 0]])

time = 0
cnt = 0

directions = deque([[0, 1], [1, 0], [0, -1], [-1, 0]]) # 초기 우, 하, 좌, 상
current_direction = directions[0] # 초기 방향: 오른쪽 (우)

while True:
    current_head = snake[-1] # 현재 머리 위치
    time += 1

    if cnt < l and time - 1 == int(l_array[cnt][0]): # 방향 변경 시점이 되었는지 확인
        if l_array[cnt][1] == "L": # "L"이면 왼쪽으로 회전
            directions.rotate(1)
        
        else: # "D"이면 오른쪽으로 회전
            directions.rotate(-1)

        current_direction = directions[0]
        cnt += 1

    cx = snake[-1][0] + current_direction[0] # x 방향 변경
    cy = snake[-1][1] + current_direction[1] # y 방향 변경

    if [cx, cy] in snake or cx < 0 or cx > n - 1 or cy < 0 or cy > n - 1:
        break # 몸 혹은 벽에 부딪히면 끝

    snake.append([cx, cy])

    if [cx + 1, cy + 1] in k_loc:
        k_loc.remove([cx + 1, cy + 1]) # 먹은 사과 제거
    
    else:
        snake.popleft() # 사과 못 먹으면 꼬리 이동

print(time)