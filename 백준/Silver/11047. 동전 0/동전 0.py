def coin(n, k, arr):
    answer = 0

    for i in range(n - 1, -1, -1):
        if arr[i] <= k:
            answer += k // arr[i]
            k -= k // arr[i] * arr[i]
        
        if k <= 0:
            break

    return answer

n, k = map(int, input().split(" "))
arr = [int(input()) for i in range(n)]

print(coin(n, k, arr))