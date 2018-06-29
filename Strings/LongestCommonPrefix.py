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

        prefix = ''
        for c in zip(*strs):
            if len(set(c)) == 1:
                prefix += c[0]
            else:
                break
        return prefix


if __name__=='__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))

