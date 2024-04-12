import sys
from collections import deque

input = sys.stdin.readline
status = [deque(list(map(str, input().strip()))) for _ in  range(4)]
k = int(input())
NandD = [list(map(int, input().split())) for _ in range(k)]

def left_direction(gear, direction):
    if gear < 0:
        return
    
    if status[gear + 1][6] != status[gear][2]:
        left_direction(gear - 1, -direction)
        status[gear].rotate(direction)

def right_direction(gear, direction):
    if gear > 3:
        return
    
    if status[gear - 1][2] != status[gear][6]:
        right_direction(gear + 1, -direction)
        status[gear].rotate(direction)

for gear, direction in NandD:
    left_direction(gear - 2, -direction)
    right_direction(gear, -direction)
    status[gear - 1].rotate(direction)

answer = 0
answer += 1 if status[0][0] == "1" else 0
answer += 2 if status[1][0] == "1" else 0
answer += 4 if status[2][0] == "1" else 0
answer += 8 if status[3][0] == "1" else 0

print(answer)