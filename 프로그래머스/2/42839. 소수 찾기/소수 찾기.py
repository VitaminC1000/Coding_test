from itertools import permutations

def is_prime_number(x) :
    if x < 2 :
        return False
    
    for i in range(2, x) :
        if x % i == 0:
            return False
            
    return True


def solution(numbers):
    answer = 0
    per = []
    
    numbers_list = [i for i in numbers]
    
    for i in range(1, len(numbers)+1):
        per.extend(int(''.join(j)) for j in list(permutations(numbers_list, i)))
    
    for i in set(per):
        if is_prime_number(int(i)):
            answer += 1
    
    return answer