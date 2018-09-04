# Time:  O(n)
# Space: O(1)
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"


class Solution(object):
    def convert(self,s, numRows):
        """
        :param s: str
        :param numRows: int
        :return: str
        """
        if numRows ==1:
            return s
        step, zigzag = 2*numRows -2, ""
        for i in range(numRows):
            for j in range(i, len(s), step):
                zigzag += s[j]
                if 0 < i < numRows - 1 and j+step-2*i < len(s):
                    """
                    P   A   H   N
                    A P L S I I G
                    Y   I   R
                    to fill the gap letters P, S & I
                    """
                    print(j, step, 2*i, s[j+step-2*i])
                    zigzag += s[j+step-2*i]
        return zigzag


if __name__=='__main__':
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))
    print(s.convert("PAYPALISHIRING", 4))
