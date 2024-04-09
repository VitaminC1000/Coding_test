import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split()) # n: 행, m: 열
x, y, d = map(int, input().split()) # x: 초기 행 위치, y: 초기 열 위치, d: 초기 바라보는 방향
room = [list(map(int, input().split())) for _ in range(n)]

directions = deque([(-1, 0), (0, 1), (1, 0), (0, -1)]) # 북, 동, 남, 서

def clean(x, y, dir):
    global turn, cnt # turn: 회전 수, cnt: 청소 횟수

    while True:
        dir.rotate(1) # 반시계 방향으로 90도 회전
        nx, ny = dir[0][0], dir[0][1] # 현재 진행 방향

        if room[x + nx][y + ny] == 0: # (현재 진행 방향) 다음 칸이 0이면 이동
            x += nx # 행 정보 업데이트
            y += ny # 열 정보 업데이트
            room[x][y] = 2 # 청소 표시
            turn = 0 # 회전 수 초기화
            cnt += 1 # 청소 횟수 1 증가

        else:
            turn += 1 # 회전 수 1 증가

        if turn == 4: # 네 방향 모두 확인한 상황
            if room[x - nx][y - ny] == 1: # 진행 방향의 뒷쪽이 벽일 경우
                break

            else: # 진행 방향 뒷쪽이 벽이 아닐 경우
                turn = 0 # 회전 수 초기화
                x -= nx # 진행 방향 뒷쪽으로 행 정보 업데이트
                y -= ny # 진행 방향 뒷쪽으로 열 정보 업데이트

directions.rotate(-d) # 초기 방향 정보에 따른 업데이트
cnt, turn = 1, 0
room[x][y] = 2 # 초기 위치 청소 완료 표시
clean(x, y, directions)

print(cnt)