import math

def solution(board, k):
    i = len(board)
    j = len(board[0])
    
    answer = 0
    
    for n in range(i):
        for m in range(j):
            if n + m <= k:
                answer += board[n][m]
    
    return answer