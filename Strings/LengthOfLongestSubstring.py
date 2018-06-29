class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        Given a string, find the length of the longest substring without repeating characters.
        :param s: string.
        :return: max length of the string.
        """
        start = max_length = 0
        d = {}

        for i in range(len(s)):
            if s[i] in d and start <= d[s[i]]:
                start = d[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)

            d[s[i]] = i

        return max_length
