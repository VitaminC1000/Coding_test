def solution(num_list):
    even = [str(i) for i in num_list if i % 2 == 0]
    odd = [str(i) for i in num_list if i % 2 == 1]
    return int(''.join(even)) + int(''.join(odd))