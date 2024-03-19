def solution(s):
    cnt = 0
    
    for i in s:
        if i == "(":
            cnt += 1
            
        else:
            if cnt > 0:
                cnt -= 1
            else:
                return False
                
    if cnt > 0:
        return False
                
    return True