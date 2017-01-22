class Solution(object):

    def printAllStringsK(self, s, prefix, n, k):
        '''
        Permutation of a String : print all possible combinations.
        '''
        if k == 0:
            print(prefix)
            return

        for i in range(n):
            self.printAllStringsK(s, prefix + s[i], n, k-1)

    def printUniqueCombinations(self, s, partial=[]):
        '''
        Print unique combinations.
        '''

        print(''.join(partial))

        for i in range(len(s)):
            left = s[i]
            right = s[i + 1:]
            self.printUniqueCombinations(right, partial + [left])

    def permute(self, a, l, r):
        if l == r:
            print(''.join(a))
        else:
            for i in range(l, r+1):
                a[l], a[i] = a[i], a[l]
                self.permute(a, l+1, r)
                a[l], a[i] = a[i], a[l]


if __name__=='__main__':
    solution = Solution()
    s = 'abcd'
    k = 3
    solution.printAllStringsK(s, '', len(s), k)
    solution.printUniqueCombinations(s)
    a = list(s)
    solution.permute(a, 0, len(a)-1)