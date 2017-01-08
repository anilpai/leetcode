# Definition for singly-linked list.
import random


class ListNode(object):
    """
    Singly Linked List Node with a value and next pointer
    """
    def __init__(self, x=None, next=None):
        """
        :param x: int, float
        """
        self.val = x
        self.next = next


class Solution(object):
    """
    Solution to the problem of reversing singly linked list
    """

    def RotateListKnodes(self, head, k):

        position = 0

        if k == position:
            return head

        prev, curr = None, head
        while position < k:
            prev, curr = curr, curr.next
            position += 1

        prev.next, prev = None, curr

        while curr.next is not None:
            curr = curr.next

        curr.next = head
        head = prev

        return head

    def createLinkedList(self, ll):

        if len(ll) == 0:
            return None

        l = [ListNode(item) for item in ll]

        head = l[0]
        if len(l) == 1:
            return head

        prev = head

        for item in l[1:]:
            curr = item
            prev.next, prev = curr, curr

        return head

    def printLinkedList(self, head):

        while head:
            print(str(head.val))
            head = head.next
        return


if __name__ == '__main__':

    ll = random.sample(range(300), 6)
    s = Solution()
    head = s.createLinkedList(ll)
    print("Before rotating: ")
    s.printLinkedList(head)
    k = 3
    head = s.RotateListKnodes(head, k)
    print("After rotating: ")
    s.printLinkedList(head)
    k = 2
    head = s.RotateListKnodes(head, k)
    print("After rotating: ")
    s.printLinkedList(head)