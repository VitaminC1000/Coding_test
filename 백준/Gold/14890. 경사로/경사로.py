import sys

input = sys.stdin.readline
n, l = map(int, input().split())
map_array = [list(map(int, input().split())) for _ in range(n)]

road = 0

def hor_count(map_array, x, y, cnt, length, stepper):
    global n, l, road

    if 0 <= y < n - 1:
        if map_array[x][y] == map_array[x][y + 1]:
            hor_count(map_array, x, y + 1, cnt + 1, length + 1, stepper)

        elif map_array[x][y] - map_array[x][y + 1] == -1:
            if length >= l and (x, y - (l - 1)) not in stepper:
                hor_count(map_array, x, y + 1, cnt + 1, 1, stepper)
            
            else:
                return
            
        elif map_array[x][y] - map_array[x][y + 1] == 1:
            if l + y + 1 <= n and sum(map_array[x][y + 1: l + y + 1]) / l == map_array[x][y + 1]:
                for i in range(y + 1, l + y + 1):
                    stepper.append((x, i))
                hor_count(map_array, x, y + 1, cnt + 1, 1, stepper)

            else:
                return
            
        else:
            return
        
    else:
        if cnt == n:
            road += 1
            return

for i in range(n):
    hor_count(map_array, i, 0, 1, 1, [])
    hor_count([list(j) for j in zip(*map_array)], i, 0, 1, 1, [])

print(road)