def solution(my_string, is_prefix):
    return 1 if is_prefix in [my_string[:i] for i in range(len(my_string))] else 0