from heapq import merge
import itertools


'''

NEEDS more understanding !!

'''

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):

        uglies = [1]
        merged = merge(*map(lambda p: (u * p for u in uglies), primes))
        uniqed = (u for u, _ in itertools.groupby(merged))
        map(uglies.append, itertools.islice(uniqed, n - 1))
        return uglies[-1]

if __name__=='__main__':
    s= Solution()
    print(s.nthSuperUglyNumber(12, [2, 7, 13, 19]))