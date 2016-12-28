from unittest import TestCase
from Strings.BalancedParentheses import Solution
from Strings.PossibleStrings import Solution as S1
from Strings.FirstUniqueChar import Solution as S2
from Strings.KthUniqChar import Solution as S3
from Strings.FirstUniqueChar import Solution as S4
from Strings.LCS import Solution as S5
from Strings.NumOfPalindromes import Solution as S6

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

    def test_LCS(self):
        r = S5()
        self.assertEqual(r.lcs('abcdef', 'abc'), 'abc')
        self.assertEqual(r.lcs('abcdef', 'acf'), 'acf')
        self.assertEqual(r.lcs('anothertest', 'notatest'), 'nottest')
        self.assertEqual(r.lcs('132535365', '123456789'), '12356')

    def test_NumOfPalindromes(self):
        r = S6()
        s1 = 'racecarenterelephantmalayalam'
        s2 = 'murderforajarofredrum'
        s3 = 'oozyratinasanitaryzoo'
        self.assertListEqual(sorted(r.allPalindromes(s1)), sorted(['aceca', 'ele', 'ala', 'aya', 'cec', 'malayalam', 'ere', 'layal', 'alayala', 'racecar']))
        self.assertListEqual(sorted(r.allPalindromes(s2)), sorted(['murderforajarofredrum', 'rajar', 'urderforajarofredru', 'forajarof', 'aja', 'rderforajarofredr', 'erforajarofre', 'derforajarofred', 'rforajarofr', 'orajaro']))
        self.assertListEqual(sorted(r.allPalindromes(s3)), sorted(['zyratinasanitaryz', 'yratinasanitary', 'ozyratinasanitaryzo', 'oozyratinasanitaryzoo', 'inasani', 'ratinasanitar', 'atinasanita', 'oo', 'asa', 'tinasanit', 'nasan']))
