from functools import reduce

def solution(num_list):
    if len(num_list) >= 11:
        answer = sum(num_list)
    else:
        answer = reduce(lambda x, y: x * y, num_list)
    return answer