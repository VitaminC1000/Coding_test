def solution(my_strings, parts):
    return ''.join([my_strings[idx][s: e+1] for idx, (s, e) in enumerate(parts)])