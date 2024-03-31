def solution(n):
    if n % 2 == 0:
        answer = sum([(n - 2 * i) ** 2 for i in range(n // 2)])
    else:
        answer = sum([(n - 2 * i) for i in range(n // 2 + 1)])
    return answer