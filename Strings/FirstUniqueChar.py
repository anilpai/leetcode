'''
Index of first unique character occured in a string.

Tip : Better way to implement using Ordered Dict
'''


class Solution(object):

    def firstUniqueChar(self, s):
        a = [0] * 26

        for i in s:
            a[ord(i)-ord('a')]+=1

        for i in s:
            if a[ord(i)- ord('a')] == 1:
                return s.index(i)
        return -1


if __name__=='__main__':
    sol = Solution()
    s = 'xyzxyzdfeghda'
    print(sol.firstUniqueChar(s))
