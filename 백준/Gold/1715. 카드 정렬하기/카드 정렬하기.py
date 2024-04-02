import heapq

def min_comparison(n, cards):
    heapq.heapify(cards)
    answer = 0

    while len(cards) > 1:
        first_smallest = heapq.heappop(cards)
        second_smallest = heapq.heappop(cards)

        combined = first_smallest + second_smallest
        answer += combined

        heapq.heappush(cards, combined)

    return answer

n = int(input())
cards = [int(input()) for i in range(n)]

print(min_comparison(n, cards))