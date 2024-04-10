import sys
from copy import deepcopy

input = sys.stdin.readline
n, m = map(int, input().split())
map_array = [list(map(int, input().split())) for _ in range(n)]

cctvs = [(map_array[i][j], i, j) for i in range(n) for j in range(m) if map_array[i][j] != 0 and map_array[i][j] != 6]
minimum = 1e10


def cctv(cnt, arr):
    global minimum

    answer = 0
    new_arr = deepcopy(arr)

    if cnt >= len(cctvs):
        answer = [1 for i in range(n) for j in range(m) if new_arr[i][j] == 0]
        minimum = min(minimum, sum(answer))
        return
    
    cctv_num, i, j = cctvs[cnt]

    if cctv_num == 1:
        for k in range(j + 1, m):
            if new_arr[i][k] == 0:
                new_arr[i][k] = "#"
            
            elif new_arr[i][k] == 6:
                break
        
        cctv(cnt + 1, new_arr)
        
        new_arr = deepcopy(arr)
        
        for k in range(i - 1, -1, -1):
            if new_arr[k][j] == 0:
                new_arr[k][j] = "#"

            elif new_arr[k][j] == 6:
                break
        
        cctv(cnt + 1, new_arr)

        new_arr = deepcopy(arr)

        for k in range(j - 1, -1, -1):
            if new_arr[i][k] == 0:
                new_arr[i][k] = "#"
            
            elif new_arr[i][k] == 6:
                break

        cctv(cnt + 1, new_arr)

        new_arr = deepcopy(arr)

        for k in range(i + 1, n):
            if new_arr[k][j] == 0:
                new_arr[k][j] = "#"

            elif new_arr[k][j] == 6:
                break

        cctv(cnt + 1, new_arr)

    elif cctv_num == 2:
        for k in range(j + 1, m):
            if new_arr[i][k] == 0:
                new_arr[i][k] = "#"
            
            elif new_arr[i][k] == 6:
                break

        for k in range(j - 1, -1, -1):
            if new_arr[i][k] == 0:
                new_arr[i][k] = "#"
            
            elif new_arr[i][k] == 6:
                break

        cctv(cnt + 1, new_arr)

        new_arr = deepcopy(arr)

        for k in range(i - 1, -1, -1):
            if new_arr[k][j] == 0:
                new_arr[k][j] = "#"

            elif new_arr[k][j] == 6:
                break

        for k in range(i + 1, n):
            if new_arr[k][j] == 0:
                new_arr[k][j] = "#"

            elif new_arr[k][j] == 6:
                break

        cctv(cnt + 1, new_arr)

    elif cctv_num == 3:
        for k in range(j + 1, m):
            if new_arr[i][k] == 0:
                new_arr[i][k] = "#"
            
            elif new_arr[i][k] == 6:
                break

        for k in range(i - 1, -1, -1):
            if new_arr[k][j] == 0:
                new_arr[k][j] = "#"

            elif new_arr[k][j] == 6:
                break
        
        cctv(cnt + 1, new_arr)

        new_arr = deepcopy(arr)

        for k in range(i - 1, -1, -1):
            if new_arr[k][j] == 0:
                new_arr[k][j] = "#"

            elif new_arr[k][j] == 6:
                break

        for k in range(j - 1, -1, -1):
            if new_arr[i][k] == 0:
                new_arr[i][k] = "#"
            
            elif new_arr[i][k] == 6:
                break

        cctv(cnt + 1, new_arr)

        new_arr = deepcopy(arr)

        for k in range(j - 1, -1, -1):
            if new_arr[i][k] == 0:
                new_arr[i][k] = "#"
            
            elif new_arr[i][k] == 6:
                break

        for k in range(i + 1, n):
            if new_arr[k][j] == 0:
                new_arr[k][j] = "#"

            elif new_arr[k][j] == 6:
                break

        cctv(cnt + 1, new_arr)

        new_arr = deepcopy(arr)

        for k in range(i + 1, n):
            if new_arr[k][j] == 0:
                new_arr[k][j] = "#"

            elif new_arr[k][j] == 6:
                break

        for k in range(j + 1, m):
            if new_arr[i][k] == 0:
                new_arr[i][k] = "#"
            
            elif new_arr[i][k] == 6:
                break

        cctv(cnt + 1, new_arr)

    elif cctv_num == 4:
        for k in range(j + 1, m):
            if new_arr[i][k] == 0:
                new_arr[i][k] = "#"
            
            elif new_arr[i][k] == 6:
                break

        for k in range(i - 1, -1, -1):
            if new_arr[k][j] == 0:
                new_arr[k][j] = "#"

            elif new_arr[k][j] == 6:
                break

        for k in range(j - 1, -1, -1):
            if new_arr[i][k] == 0:
                new_arr[i][k] = "#"
            
            elif new_arr[i][k] == 6:
                break
        
        cctv(cnt + 1, new_arr)

        new_arr = deepcopy(arr)

        for k in range(i - 1, -1, -1):
            if new_arr[k][j] == 0:
                new_arr[k][j] = "#"

            elif new_arr[k][j] == 6:
                break

        for k in range(j - 1, -1, -1):
            if new_arr[i][k] == 0:
                new_arr[i][k] = "#"
            
            elif new_arr[i][k] == 6:
                break

        for k in range(i + 1, n):
            if new_arr[k][j] == 0:
                new_arr[k][j] = "#"

            elif new_arr[k][j] == 6:
                break
        
        cctv(cnt + 1, new_arr)

        new_arr = deepcopy(arr)

        for k in range(j - 1, -1, -1):
            if new_arr[i][k] == 0:
                new_arr[i][k] = "#"
            
            elif new_arr[i][k] == 6:
                break

        for k in range(i + 1, n):
            if new_arr[k][j] == 0:
                new_arr[k][j] = "#"

            elif new_arr[k][j] == 6:
                break

        for k in range(j + 1, m):
            if new_arr[i][k] == 0:
                new_arr[i][k] = "#"
            
            elif new_arr[i][k] == 6:
                break
        
        cctv(cnt + 1, new_arr)

        new_arr = deepcopy(arr)

        for k in range(i + 1, n):
            if new_arr[k][j] == 0:
                new_arr[k][j] = "#"

            elif new_arr[k][j] == 6:
                break

        for k in range(j + 1, m):
            if new_arr[i][k] == 0:
                new_arr[i][k] = "#"
            
            elif new_arr[i][k] == 6:
                break

        for k in range(i - 1, -1, -1):
            if new_arr[k][j] == 0:
                new_arr[k][j] = "#"

            elif new_arr[k][j] == 6:
                break
        
        cctv(cnt + 1, new_arr)

    else:
        for k in range(j - 1, -1, -1):
            if new_arr[i][k] == 0:
                new_arr[i][k] = "#"
            
            elif new_arr[i][k] == 6:
                break

        for k in range(i + 1, n):
            if new_arr[k][j] == 0:
                new_arr[k][j] = "#"

            elif new_arr[k][j] == 6:
                break

        for k in range(j + 1, m):
            if new_arr[i][k] == 0:
                new_arr[i][k] = "#"
            
            elif new_arr[i][k] == 6:
                break

        for k in range(i - 1, -1, -1):
            if new_arr[k][j] == 0:
                new_arr[k][j] = "#"

            elif new_arr[k][j] == 6:
                break

        cctv(cnt + 1, new_arr)

cctv(0, map_array)
print(minimum)