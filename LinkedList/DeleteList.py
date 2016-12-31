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
    Delete a node at a particular position (RECURSIVELY) of a singly linked list
    """
    def DeleteList(self, head, position):
        if position == 0:
            return head.next
        head.next = self.DeleteList(head.next, position - 1)
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
    print("Before deleting: ")
    s.printLinkedList(head)
    head = s.DeleteList(head, 4)
    print("After deleting: ")
    s.printLinkedList(head)