import sys

input = sys.stdin.readline
n, k = map(int, input().split())
unsorted_array = list(map(int, input().split()))

def merge(arr, low, high):
    global cnt, k, answer

    temp = []
    mid = (low + high) // 2
    i, j = low, mid + 1

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= high:
        temp.append(arr[j])
        j += 1

    for i in range(low, high + 1):
        cnt += 1
        arr[i] = temp[i - low]

        if cnt == k:
            answer = arr[i]

    return arr


def merge_sort(arr, low, high):
    if low >= high:
        return 

    mid = (low + high) // 2

    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)

    sorted_array = merge(arr, low, high)

    return sorted_array

cnt = 0
answer = 0

merge_sort(unsorted_array, 0, n - 1)

print(answer if cnt >= k else -1)