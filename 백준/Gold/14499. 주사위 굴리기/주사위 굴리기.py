from collections import deque
import sys

input = sys.stdin.readline
n, m, x, y, k = map(int, input().split()) # 행, 열, 행 위치, 열 위치, 명령 수
map_array = [list(map(int, input().split())) for _ in range(n)] # 지도 위의 숫자 배열
EWNS = list(map(int, input().split())) # 동: 1, 서: 2, 북: 3, 남: 4

directions = [[0, 1], [0, -1], [-1, 0], [1, 0]] # 동, 서, 북, 남

dice_hor = deque([0] * 4) # 주사위 가로 방향 초기화
dice_ver = deque([0] * 4) # 주사위 세로 방향 초기화

def horizontal(x, y):
    global dice_hor, dice_ver, map_array

    if map_array[x][y] != 0: # 지도 숫자가 0이 아닌 경우
        dice_hor[2] = map_array[x][y] # 지도 숫자를 주사위의 수평 방향의 바닥 면에 복사
        map_array[x][y] = 0 # 지도 숫자를 0으로 초기화

    elif map_array[x][y] == 0: # 지도 숫자가 0인 경우
        map_array[x][y] = dice_hor[2] # 주사위의 수평 방향의 바닥 면에 적힌 값은 지도로 복사

    dice_ver[0] = dice_hor[0] # 수직 방향의 윗 면 숫자 변경
    dice_ver[2] = dice_hor[2] # 수직 방향의 바닥 면 숫자 변경

    return


def vertical(x, y):
    global dice_hor, dice_ver, map_array

    if map_array[x][y] != 0:
        dice_ver[2] = map_array[x][y]
        map_array[x][y] = 0

    elif map_array[x][y] == 0:
        map_array[x][y] = dice_ver[2]

    dice_hor[0] = dice_ver[0]
    dice_hor[2] = dice_ver[2]

    return


for i in EWNS:
    x += directions[i - 1][0]
    y += directions[i - 1][1]

    if 0 <= x < n and 0 <= y < m:
        if i == 1:
            dice_hor.rotate(1) # 동쪽: 수평 방향 리스트 시계 방향으로 회전
            horizontal(x, y)
        
        elif i == 2:
            dice_hor.rotate(-1) # 서쪽: 수평 방향 리스트 반시계 방향으로 회전
            horizontal(x, y)

        elif i == 3:
            dice_ver.rotate(-1) # 북쪽: 수직 방향 리스트 반시계 방향으로 회전
            vertical(x, y)

        elif i == 4:
            dice_ver.rotate(1) # 남쪽: 수직 방향 리스트 반시계 방향으로 회전
            vertical(x, y)
        
        print(dice_hor[0])

    else:
        x -= directions[i - 1][0]
        y -= directions[i - 1][1]