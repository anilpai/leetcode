class Solution(object):
    def KthUniqChar(self, s, k):
        if k < 1:
            return None

        n = len(s)
        count = [0] * 256
        index = [n] * 256

        for x,i in enumerate(s):
            count[ord(i)] += 1

            if count[ord(i)] == 1:
                index[ord(i)] = x

            if count[ord(i)] == 2:
                index[ord(i)] = n

        result = [i for i in sorted(index) if i < n]
        if k > len(result):
            return None
        return s[result[k-1]]


if __name__=='__main__':
    s = Solution()
    string = 'geeksforgeeks'
    print(s.KthUniqChar(string, 1)) # f
    print(s.KthUniqChar(string, 2)) # o
    print(s.KthUniqChar(string, 0)) # r