from unittest import TestCase
from Sorting.QuickSort import Solution as a
from Sorting.MergeSort import Solution as b


class TestSolution(TestCase):
    def test_quicksort(self):
        r = a()
        array = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2]
        self.assertListEqual(r.quicksort(array, 0, len(array) - 1), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],' Sorted using Merge Sort')

    def test_mergesort(self):
        r = b()
        array = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2]
        self.assertListEqual(r.merge_sort(array), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 'Sorted using Merge Sort')