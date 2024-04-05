import sys

def factorial(n):
    
    if n == 1 or n == 0:
        return 1
    
    elif n >= 2:
        return n * factorial(n - 1)

n = int(sys.stdin.readline())

print(factorial(n))