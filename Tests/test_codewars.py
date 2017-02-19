from unittest import TestCase
from Codewars.Molecule2Atoms import Solution as S1
from Codewars.SortColumnsCSV import Solution as S2


class TestSolution(TestCase):
    def test_molecule2atoms(self):
        r = S1()
        water = 'H2O'
        self.assertDictEqual(r.parse_molecule(water), {'H': 2, 'O': 1})
        magnesium_hydroxide = 'Mg(OH)2'
        self.assertDictEqual(r.parse_molecule(magnesium_hydroxide), {'Mg': 1, 'O': 2, 'H': 2})
        fremySalt = 'K4[ON(SO3)2]2'
        self.assertDictEqual(r.parse_molecule(fremySalt), {'K': 4, 'O': 14, 'N': 2, 'S': 4})
        unknown = 'S{O3{PO}2}2'
        self.assertDictEqual(r.parse_molecule(unknown), {'O': 10, 'P': 4, 'S': 1})

    def test_sortColumnCSV(self):
        r = S2()
        pre_sorting = (
            "myjinxin2015;raulbc777;smile67;Dentzil;SteffenVogel_79\n"
            "17945;10091;10088;3907;10132\n"
            "2;12;13;48;11"
        )

        post_sorting = (
            "Dentzil;myjinxin2015;raulbc777;smile67;SteffenVogel_79\n"
            "3907;17945;10091;10088;10132\n"
            "48;2;12;13;11"
        )

        self.assertEqual(r.sort_csv_columns(pre_sorting), post_sorting)