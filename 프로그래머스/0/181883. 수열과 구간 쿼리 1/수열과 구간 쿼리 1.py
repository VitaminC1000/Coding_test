def solution(arr, queries):
    for i in range(len(arr)):
        for s, e in queries:
            if s <= i <= e:
                arr[i] += 1
    
    return arr