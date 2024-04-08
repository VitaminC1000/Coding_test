from copy import deepcopy
import sys

input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def up(board):
    global n

    for j in range(n):
        idx = 0
        for i in range(1, n):
            if board[i][j] != 0:
                temp = board[i][j]
                board[i][j] = 0

                if board[idx][j] == 0:
                    board[idx][j] = temp

                elif board[idx][j] == temp:
                    board[idx][j] = temp * 2
                    idx += 1

                else:
                    idx += 1
                    board[idx][j] = temp

    return board
                    

def down(board):
    global n

    for j in range(n):
        idx = n - 1
        for i in range(n - 2, -1, -1):
            if board[i][j] != 0:
                temp = board[i][j]
                board[i][j] = 0

                if board[idx][j] == 0:
                    board[idx][j] = temp

                elif board[idx][j] == temp:
                    board[idx][j] = temp * 2
                    idx -= 1

                else:
                    idx -= 1
                    board[idx][j] = temp

    return board
                    

def left(board):
    global n
    
    for i in range(n):
        idx = 0
        for j in range(1, n):
            if board[i][j] != 0:
                temp = board[i][j]
                board[i][j] = 0

                if board[i][idx] == 0:
                    board[i][idx] = temp

                elif board[i][idx] == temp:
                    board[i][idx] = temp * 2
                    idx += 1

                else:
                    idx += 1
                    board[i][idx] = temp

    return board
                    

def right(board):
    global n

    for i in range(n):
        idx = n - 1
        for j in range(n - 2, -1, -1):
            if board[i][j] != 0:
                temp = board[i][j]
                board[i][j] = 0

                if board[i][idx] == 0:
                    board[i][idx] = temp

                elif board[i][idx] == temp:
                    board[i][idx] = temp * 2
                    idx -= 1

                else:
                    idx -= 1
                    board[i][idx] = temp

    return board


def dfs(board, depth):
    global answer

    if depth == 5:
        for i in range(n):
            for j in range(n):
                answer = max(answer, board[i][j])
        return

    dfs(up(deepcopy(board)), depth + 1)
    dfs(down(deepcopy(board)), depth + 1)
    dfs(left(deepcopy(board)), depth + 1)                                     
    dfs(right(deepcopy(board)), depth + 1)

dfs(board, 0)
print(answer)