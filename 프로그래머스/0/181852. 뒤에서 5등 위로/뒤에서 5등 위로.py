import heapq

def heap(arr):
    result = []
    heapq.heapify(arr)
    
    for i in range(len(arr)):
        result.append(heapq.heappop(arr))
    
    return result
        
def solution(num_list):
    return heap(num_list)[5:]