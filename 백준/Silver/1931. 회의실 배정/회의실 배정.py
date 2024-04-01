def max_meeting(n, arr):
    arr.sort(key = lambda x: (x[1], x[0]))
    st = [arr[0]]
    
    for i in range(1, len(arr)):
        if st[-1][1] <= arr[i][0]:
            st.append(arr[i])

    return len(st)

n = int(input())
arr = [list(map(int, input().split(" "))) for i in range(n)]

print(max_meeting(n, arr))