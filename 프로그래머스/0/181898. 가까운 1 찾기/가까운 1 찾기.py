def solution(arr, idx):
    for i, val in enumerate(arr):
        if val == 1 and i >= idx:
            answer = i
            break
        else:
            answer = -1
    return answer