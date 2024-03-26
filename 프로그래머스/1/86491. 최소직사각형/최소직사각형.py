def solution(sizes):
    answer = 0
    w = 0
    h = 0
    
    for i in sizes:
        if i[0] > i[1]:
            cw = i[0]
            ch = i[1]
        else:
            cw = i[1]
            ch = i[0]
            
        if w < cw:
            w = cw
        if h < ch:
            h = ch
            
    answer = w * h
    
    return answer