def min_operation(a, b):
    cnt = 0

    b_list = [s for s in str(b)]

    while a != b:
        if int(b_list[-1]) == 1:
            b_list.pop()
            b = int(''.join(b_list))
            b_list = [s for s in str(b)]
            cnt += 1
        
        else:
            if b % 2 == 0:
                b //= 2
                b_list = [s for s in str(b)]
                cnt += 1

            else:
                return -1

        if a > b:
            return -1
    
    return cnt + 1

a, b = map(int, input().split(' '))

print(min_operation(a, b))