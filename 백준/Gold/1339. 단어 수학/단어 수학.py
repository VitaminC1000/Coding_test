import sys

def maximum(str_list):
    str_dict = {}

    for str_ in str_list:
        n_square = len(str_) - 1

        for s in str_:
            if s in str_dict:
                str_dict[s] += 10 ** n_square
            else:
                str_dict[s] = 10 ** n_square

            n_square -= 1

    max_num = 9
    answer = 0
    
    for i in sorted(str_dict.values(), reverse = True):
        answer += i * max_num
        max_num -= 1

    return answer

n = int(sys.stdin.readline())

str_list = [sys.stdin.readline()[: -1] for _ in range(n)]

print(maximum(str_list))