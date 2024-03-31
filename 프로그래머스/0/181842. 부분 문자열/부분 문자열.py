def solution(str1, str2):
    sub_str = [str2[i: i + len(str1)] for i in range(len(str2)) if i + len(str1) <= len(str2)]
    
    if str1 in sub_str:
        answer = 1
    else:
        answer = 0
    return answer