class Solution(object):
    """
    1 . Word by Word Matching -> O(MN) , O(M)
    2 . Character by Character Matching -> O(MN), O(M)
    3 . Divide and Conquer (same as 1) -> O(MN), O(M .log N)
    4 . Binary Search -> O(M log M. N), O(N)
    5 . Using Trie -> O(MN) , O(MN)
    """

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]

        mins = min(strs, key=len)
        n, i = len(mins), 0
        while i < len(strs):
            if mins[:n] != strs[i][:n]:
                n -= 1
                i = 0
            else:
                i += 1
        return mins[:n]

    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        short_word = min(strs, key=len)
        answer = ""
        i = 0
        for letter in short_word:
            for word in strs:
                if word[i] != letter:
                    return answer
            answer = answer + letter
            i = i+1
        return answer


if __name__=='__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))

