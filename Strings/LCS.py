class Solution(object):
    '''
    Longest Common Subsequence. : DP problem found in CodeWars.
    Explanation : https://www.youtube.com/watch?v=NnD96abizww
    '''
    def lcs(self, x, y):
        if len(x) == 0 or len(y) == 0:
            return ''
        if x[0] == y[0]:
            return x[0] + self.lcs(x[1:], y[1:])
        else:
            return max(self.lcs(x, y[1:]), self.lcs(x[1:], y), key=len)

if __name__=='__main__':
    s = Solution()
    print(s.lcs('a', 'b'))
    print(s.lcs('abcdef', 'abc'))
    print(s.lcs('a', 'a'))
    print(s.lcs('abc', 'ac'))
    print(s.lcs('abcdef', 'abc'))
    print(s.lcs('abcdef', 'acf'))
    print(s.lcs('anothertest', 'notatest'))
    print(s.lcs('132535365', '123456789'))
    print(s.lcs('finaltest', 'zzzfinallyzzz'))

