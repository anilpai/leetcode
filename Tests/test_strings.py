from unittest import TestCase
from Strings.BalancedParentheses import Solution
from Strings.PossibleStrings import Solution as S1
from Strings.FirstUniqueChar import Solution as S2
from Strings.KthUniqChar import Solution as S3
from Strings.FirstUniqueChar import Solution as S4


class TestSolution(TestCase):
    def test_paranthesisChecker(self):
        r = Solution()
        strings = ['{{([][])}()}', '[{()]']
        self.assertTrue(r.paranthesisChecker(strings[0]), "Parenthesis has matched.")
        self.assertFalse(r.paranthesisChecker(strings[1]), "Parenthesis has not matched.")

    def test_printAllStringsK(self):
        r = S1()
        s = ['a', 'b', 'c', 'd']
        k = 3
        self.assertEqual(r.printAllStringsK(s, '', len(s), k), None,'Printed all string')

    def test_firstUniqueChar(self):
        r = S2()
        s = 'abcac'
        self.assertEqual(r.firstUniqueChar(s),1, 'First Unique char')

    def test_KthUniqChar(self):
        r = S3()
        s = 'geeksforgeeks'
        self.assertEqual(r.KthUniqChar(s, 1), 'f', 'Kth Uniq')
        self.assertEqual(r.KthUniqChar(s, 2), 'o', 'Kth Uniq')
        self.assertEqual(r.KthUniqChar(s, 3), 'r', 'Kth Uniq')
        self.assertEqual(r.KthUniqChar(s, 0), None, 'Kth Uniq')
        self.assertEqual(r.KthUniqChar(s, 4), None, 'Kth Uniq')

    def test_firstUniqueChar(self):
        r = S4()
        s = 'xyzxyzdfeghda'
        self.assertEqual(r.firstUniqueChar(s), 7, 'First Unique Char')