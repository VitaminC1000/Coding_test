def solution(num_list):
    even = sum([val for idx, val in enumerate(num_list) if (idx + 1) % 2 == 0])
    odd = sum([val for idx, val in enumerate(num_list) if (idx + 1) % 2 == 1])
    return even if even > odd else odd