def min_cost(n, length, cost):
    current_cost = cost[0]
    answer = length[0] * current_cost

    for i in range(1, n - 1):
        if length[i] * current_cost > length[i] * cost[i]:
            current_cost = cost[i]
            answer += length[i] * current_cost
        else:
            answer += length[i] * current_cost

    return answer

n = int(input())
length = list(map(int, input().split(" ")))
cost = list(map(int, input().split(" ")))

print(min_cost(n, length, cost))