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
        self.swap(a, pivot, last)
        for i in range(first, last):
            if a[i] <= a[last]:
                self.swap(a, i, first)
                first += 1
        self.swap(a, first, last)
        return first

    def swap(self, a, x, y):
        a[x], a[y] = a[y], a[x]


if __name__=='__main__':
    s = Solution()
    a = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2]
    print(s.quicksort(a, 0, len(a)-1))