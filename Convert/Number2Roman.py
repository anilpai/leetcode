import sys


class Solution(object):

    def intToRoman2(self, n):
        n_map = zip(
            (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
            ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'))

        if n == 0:
            return ''
        return next(c + self.intToRoman2(n - v) for v, c in n_map if v <= n)

    def intToRoman(self, n):
        numeral_map = zip(
            (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
            ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'))

        r = []
        for integer, numeral in numeral_map:
            cnt = int(n / integer)
            r.append(numeral * cnt)
            n -= integer * cnt
        return ''.join(r)

    def romanToInt(self, n):
        numeral_map = zip(
            (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
            ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'))

        i = result = 0
        for integer, numeral in numeral_map:
            while n[i: i+len(numeral)] == numeral:
                result += integer
                i += len(numeral)
        return result


if __name__ == '__main__':
    s = Solution()
    n = 5764
    print(s.intToRoman(n))
    print(s.intToRoman2(n))
    r = 'MDCCLXIV'
    print(s.romanToInt(r))