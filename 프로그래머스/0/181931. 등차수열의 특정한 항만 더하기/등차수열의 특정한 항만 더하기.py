def solution(a, d, included):
    return sum([a + idx * d for idx, val in enumerate(included) if val])