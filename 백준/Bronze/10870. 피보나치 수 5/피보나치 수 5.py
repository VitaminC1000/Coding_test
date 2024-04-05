import sys

def fibonacci(n):

    if n == 1:
        return 1
    
    elif n == 0:
        return 0
    
    elif n >=2:
        return fibonacci(n - 1) + fibonacci(n - 2)

    return

n = int(sys.stdin.readline())

print(fibonacci(n))