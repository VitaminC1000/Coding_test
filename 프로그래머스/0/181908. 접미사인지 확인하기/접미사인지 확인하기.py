def solution(my_string, is_suffix):
    suffix = [my_string[i:] for i in range(len(my_string))]
    
    if is_suffix in suffix:
        answer = 1
        
    else:
        answer = 0
    return answer