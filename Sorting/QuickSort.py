import random


class Solution(object):
    def quicksort(self, a, first, last):
        if first < last:
            pivot = self.partition(a, first, last)
            self.quicksort(a, first, pivot-1)
            self.quicksort(a, pivot+1, last)
        return a

    def partition(self, a, first, last):
        pivot = first + random.randrange(last - first + 1)
        a[pivot], a[last] = a[last], a[pivot]
        for i in range(first, last):
            if a[i] <= a[last]:
                a[i], a[first] = a[first], a[i]
                first += 1
        a[first], a[last] = a[last], a[first]
        return first


if __name__=='__main__':
    s = Solution()
    a = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2]
    print(s.quicksort(a, 0, len(a)-1))