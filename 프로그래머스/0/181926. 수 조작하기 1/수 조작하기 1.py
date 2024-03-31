def solution(n, control):
    answer = []
    
    for i in control:
        if i == "w":
            answer.append(1)
        
        elif i == "s":
            answer.append(-1)
            
        elif i == "d":
            answer.append(10)
            
        elif i == "a":
            answer.append(-10)
    return sum(answer) + n