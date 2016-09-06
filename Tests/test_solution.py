from unittest import TestCase

from ReorderList.ReorderList import Solution

class TestSolution(TestCase):
    def test_ReorderList(self):
        r = Solution()
        head = r.createLinkedList([1, 2, 3, 4])
        head = r.ReorderList(head)
        result = r.LinkedListToList(head)
        expected = [1, 4, 2, 3]
        self.assertListEqual(result, expected, "Both lists are equal")

    def test_createLinkedList(self):
        self.fail()

    def test_printLinkedList(self):
        self.fail()
