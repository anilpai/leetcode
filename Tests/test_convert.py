from unittest import TestCase
from Convert.Number2Roman import Solution as S1
from Convert.Number2Word import Solution as S2


class TestSolution(TestCase):
    def test_intToRoman(self):
        r = S1()
        integer = 5764
        integer2 = 12978
        self.assertTrue(r.intToRoman(integer), 'MMMMMDCCLXIV')
        self.assertTrue(r.intToRoman2(integer2), 'MMMMMMMMMMMMCMLXXVIII')

    def test_romanToInt(self):
        r = S1()
        roman = 'MDCCLXIV'
        self.assertTrue(r.romanToInt(roman), 1764)

    def test_convert2word(self):
        r = S2()
        n = 5129038237764
        self.assertEqual(r.convert2word(n), 'five trillion one hundred twenty nine billion thirty eight million two hundred thirty seven thousand seven hundred and sixty four')