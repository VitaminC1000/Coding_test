import sys

def maximum(n, numbers):
    pos = []  
    neg = [] 
    one = []  
    zero = 0  

    for num in numbers:
        if num > 1:
            pos.append(num)
        elif num == 1:
            one.append(num)
        elif num == 0:
            zero += 1
        else:
            neg.append(num)

    pos.sort(reverse=True)
    neg.sort()

    sum_ = sum(one)
    for i in range(0, len(pos)-1, 2):
        sum_ += pos[i] * pos[i+1]
    if len(pos) % 2 == 1:
        sum_ += pos[-1]

    for i in range(0, len(neg)-1, 2):
        sum_ += neg[i] * neg[i+1]
    if len(neg) % 2 == 1 and zero == 0:
        sum_ += neg[-1]

    return sum_

n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(n)]

print(maximum(n, numbers))
