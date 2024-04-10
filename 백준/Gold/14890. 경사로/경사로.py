import sys

input = sys.stdin.readline
n, l = map(int, input().split()) # n: 지도 크기, l: 경사로 길이
map_array = [list(map(int, input().split())) for _ in range(n)] # 지도

road = 0

def hor_count(map_array, x, y, cnt, length, stepper):
    global n, l, road

    if 0 <= y < n - 1:
        if map_array[x][y] == map_array[x][y + 1]: # 다음 칸과 높이가 같은 경우
            hor_count(map_array, x, y + 1, cnt + 1, length + 1, stepper) # 다음 칸으로 이동

        elif map_array[x][y] - map_array[x][y + 1] == -1: # 다음 칸의 높이가 1 높은 경우
            # 이전까지 높이가 같았던 칸들의 길이가 경사로 길이 이상인지 / 경사로를 깔아야 하는 마지막 칸이 이전에 사용되지 않았는지 확인
            if length >= l and (x, y - (l - 1)) not in stepper:
                hor_count(map_array, x, y + 1, cnt + 1, 1, stepper) # 조건 만족하는 경우 다음 칸으로 이동
            
            else: 
                return
            
        elif map_array[x][y] - map_array[x][y + 1] == 1: # 다음 칸의 높이가 1 낮은 경우
            # 경사로가 지도 크기를 넘어가지 않는지 / 앞으로 경사로를 깔아야 하는 칸들의 높이가 같은지 확인
            if l + y + 1 <= n and sum(map_array[x][y + 1: l + y + 1]) / l == map_array[x][y + 1]:
                # 경사로 깔아야 하는 부분 방문 표시
                for i in range(y + 1, l + y + 1):
                    stepper.append((x, i))
                hor_count(map_array, x, y + 1, cnt + 1, 1, stepper) # 조건 만족하는 경우 다음 칸으로 이동

            else:
                return
            
        else: # 다음 칸과의 높이 차이가 2 이상인 경우
            return
        
    else:
        if cnt == n:
            road += 1
            return

for i in range(n):
    hor_count(map_array, i, 0, 1, 1, [])
    hor_count([list(j) for j in zip(*map_array)], i, 0, 1, 1, []) # transpose

print(road)
