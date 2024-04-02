import heapq

def heap(arr):
    result = []
    heapq.heapify(arr)
    
    for i in range(len(arr)):
        result.append(heapq.heappop(arr))
        
    return result

def solution(numbers):
    answer = heap(numbers)
    
    return answer[-1] * answer[-2]