from unittest import TestCase
from Strings.BalancedParentheses import Solution
from Strings.PossibleStrings import Solution as S1

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
        self.assertEqual(r.printAllStringsK(s, '', len(s), k), None ,'Printed all string' )
