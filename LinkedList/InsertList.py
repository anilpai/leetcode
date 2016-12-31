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
    Insert a node at a particular position of a singly linked list
    """
    def InsertList(self, head, val, position):

        d = ListNode(val)
        # if the head is NULL
        if head is None:
            head = d
            return head

        # if the position is ZERO
        if position == 0:
            d.next = head
            head = d
            return head

        curr = head
        while position - 1:
            curr = curr.next
            position -= 1

        d.next = curr.next
        curr.next = d
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
        '''
        Prints the Linked List
        :return: null
        '''
        while head:
            print(str(head.val))
            head = head.next
        return


if __name__ == '__main__':

    ll = random.sample(range(300), 6)
    s = Solution()
    head = s.createLinkedList(ll)
    print("Before inserting: ")
    s.printLinkedList(head)
    head = s.InsertList(head, 20, 4)
    print("After inserting: ")
    s.printLinkedList(head)