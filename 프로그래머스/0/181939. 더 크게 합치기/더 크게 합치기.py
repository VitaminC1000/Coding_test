def solution(a, b):
    x = int(''.join(list(map(str, [a, b]))))
    y = int(''.join(list(map(str, [b, a]))))
    
    if x >= y:
        answer = x
        
    else:
        answer = y
    return answer