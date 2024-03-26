def solution(number, k):
    answer = [] 
    for num in str(number):
        while answer and k > 0 and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)

    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)