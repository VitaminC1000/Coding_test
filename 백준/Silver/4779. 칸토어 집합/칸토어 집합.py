import sys

def remove(a, n):
    if n == 1:
        return
    
    for i in range(a + n // 3, a + (n // 3) * 2):
        result[i] = ' '

    remove(a, n // 3)
    remove(a + n // 3 * 2, n // 3) 

while True:
    try:
        N = int(sys.stdin.readline())
        result = ['-'] * (3 ** N)
        remove(0, 3 ** N)
        print(''.join(result))

    except:
        break