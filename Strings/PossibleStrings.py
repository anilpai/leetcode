class Solution(object):

    def printAllStringsK(self, s, prefix, n, k):
        if k == 0:
            print(prefix)
            return

        for i in range(n):
            self.printAllStringsK(s, prefix + s[i], n, k-1)

if __name__=='__main__':
    solution = Solution()
    s = ['a', 'b', 'c', 'd']
    k = 3
    solution.printAllStringsK(s, '', len(s), k)
