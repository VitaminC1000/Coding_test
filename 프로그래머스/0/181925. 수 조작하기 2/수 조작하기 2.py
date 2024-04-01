def solution(numLog):
    wasd = dict(zip([1, -1, 10, -10], ['w', 's', 'd', 'a']))
    return ''.join([wasd[numLog[i] - numLog[i - 1]] for i in range(1, len(numLog))])