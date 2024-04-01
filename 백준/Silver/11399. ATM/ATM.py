import heapq

def heap(arr):
    result = []
    heapq.heapify(arr)

    for i in range(len(arr)):
        result.append(heapq.heappop(arr))

    return result

def atm(n, arr):
    arr = heap(arr)

    sum_list = [sum(arr[: i + 1]) for i in range(n)]

    return sum(sum_list)

n = int(input())
arr = list(map(int, input().split(" ")))

print(atm(n, arr))