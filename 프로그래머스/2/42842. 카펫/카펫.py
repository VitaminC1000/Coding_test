def factorization(n):
    factors = []
    
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
            
    return factors


def solution(brown, yellow):
    answer = []
    
    size = brown + yellow

    factors = factorization(size)
    left = 0
    right = len(factors) - 1
    
    while True:
        if left > right:
            break

        if brown == 2 * (factors[right] + factors[left] - 2):
            answer.extend([factors[right], factors[left]])
        
        left += 1
        right -= 1
    
    return answer