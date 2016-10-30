from unittest import TestCase

from LinkedList.ReorderList import Solution

class TestSolution(TestCase):
    def test_ReorderList(self):
        r = Solution()
        head = r.createLinkedList([1, 2, 3, 4])
        head = r.ReorderList(head)
        result = r.LinkedListToList(head)
        expected = [1, 4, 2, 3]
        self.assertListEqual(result, expected, "Both lists are equal")

    def test_createLinkedList(self):
        r = Solution()
        head = r.createLinkedList([1, 2, 3, 4])
        self.assertEqual(head.next.next.val, 3, "Node 3 in linked list equals 3")

    def test_printLinkedList(self):
        r = Solution()
        head = r.printLinkedList(r.createLinkedList([1, 2, 3, 4]))
        self.assertEqual(head, None, "Complete Linked List was printed")
