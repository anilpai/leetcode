'''
Python program for Memoized version of nth Fibonacci number.

Video : http://www.geeksforgeeks.org/dynamic-programming-set-1/

'''


'''
MEMOIZATION version.  (Top Down)
'''


def fib(n, lookup):

    # Base Case
    if n == 0 or n == 1:
        lookup[n] = n

    if lookup[n] is None:
        lookup[n] = fib(n-1, lookup) + fib(n-2, lookup)

    return lookup[n]


'''
Tabulated version. (Bottom Up)
'''


def fib2(n):
    f = [0] * (n+1)

    f[1] = 1

    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]


if __name__=='__main__':
    n = 34
    lookup = [None] * 101
    print(fib(n, lookup))
    n = 9
    print(fib2(n))
