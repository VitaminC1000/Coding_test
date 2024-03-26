def solution(answers):
    answer = []
    
    poor1 = [1, 2, 3, 4, 5]
    poor2 = [2, 1, 2, 3, 2, 4, 2, 5]
    poor3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    victory_poor = [0, 0, 0]
    
    for idx, val in enumerate(answers):
        
        if val == poor1[idx % 5]:
            victory_poor[0] += 1
            
        if val == poor2[idx % 8]:
            victory_poor[1] += 1
            
        if val == poor3[idx % 10]:
            victory_poor[2] += 1
    
    for idx, vic in enumerate(victory_poor):
        if vic == max(victory_poor):
            answer.append(idx+1)
    
    return answer
