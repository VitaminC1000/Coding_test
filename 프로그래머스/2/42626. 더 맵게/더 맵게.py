import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        try:
            answer += 1
            heapq.heappush(scoville, heapq.heappop(scoville)+2*heapq.heappop(scoville))
        except IndexError:
            return -1
    
    return answer