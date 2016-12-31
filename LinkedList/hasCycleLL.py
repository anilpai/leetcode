"""
 Merge two linked lists

"""
import random


class Node(object):
    def __init__(self, x):
        """
        :param x: int
        """
        number_types = (int, float)
        if isinstance(x, number_types):
            self.val = x
        else:
            raise ValueError
        self.next = None


class Solution(object):
    def hasCycle(self, head):

        if head is None:
            return 0
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return 1
        return 0

    def createCyclicLinkedList(self, ll):

        if len(ll) == 0:
            return None

        l = [Node(item) for item in ll]

        head = l[0]
        if len(l) == 1:
            return head

        prev = head

        for item in l[1:]:
            curr = item
            prev.next, prev = curr, curr

        tmp = head
        while tmp.next:
            tmp = tmp.next

        tmp.next = head.next.next

        return head

    def printLinkedList(self, head):
        '''
        Prints the Linked List
        '''
        while head:
            print(str(head.val))
            head = head.next
        return

if __name__ == '__main__':

    ll = [1, 2, 3, 4, 5, 6]
    s = Solution()
    head = s.createCyclicLinkedList(ll)
    print(bool(s.hasCycle(head)))

