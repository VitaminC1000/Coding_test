cnt = 0

def solution(numbers, target):
    global cnt

    if len(numbers) == 0 and target == 0:
        cnt += 1
    
    if len(numbers) > 1:
        solution(numbers[1: ], target + numbers[0])

        solution(numbers[1: ], target - numbers[0])
    
    elif len(numbers) == 1:
        solution([], target + numbers[0])

        solution([], target - numbers[0])
    
    return max(0, cnt)