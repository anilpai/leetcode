'''
Knuth Morris Pratt Algorithm
Video : https://www.youtube.com/watch?v=GTJr8OvyEVQ
'''


class Solution(object):
    def KMPSearch(self, pat, txt):
        M = len(pat)
        N = len(txt)

        lps = [0] * M
        j = 0

        self.computeLPSArray(pat, M, lps)

        i = 0

        while i < N:
            if pat[j] == txt[i]:
                i += 1
                j += 1

            if j == M:
                print("Found pattern at index : " + str(i-j))
                j = lps[j-1]

            elif i < N and pat[j] != txt[i]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1

    def computeLPSArray(self, pat, M, lps):
        '''
        LPS : Longest prefix suffix value.
        '''
        length = 0
        i = 1

        while i < M:
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length-1]
                else:
                    lps[i] = 0
                    i += 1


if __name__=='__main__':
    txt = 'ABABDABACDABABCABAB'
    pat = 'ABABCABAB'
    s =Solution()
    s.KMPSearch(pat, txt)