
class Solution(object):

    def compress(self, s):
        res = []
        count = 0

        for i,val in enumerate(s):
            count+=1
            if i+1 >= len(s) or s[i] != s[i+1]:
                res.append(val+str(count))
                count = 0
        return ''.join(res)

if __name__=='__main__':
    s = Solution()
    strings = ['aabcccccaaa', 'aaaaaaa']
    for string in strings:
        print(s.compress(string))
