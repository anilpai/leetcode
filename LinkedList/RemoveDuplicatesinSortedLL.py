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
    def removeDuplicates(self, head):
        node = head
        while node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head

    def createLinkedList(self, ll):

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

    ll = [1, 2, 2, 3, 3, 4]
    s = Solution()
    head = s.createLinkedList(ll)
    print("Sorted List")
    s.printLinkedList(head)
    h = s.removeDuplicates(head)
    print("After removing duplicates")
    s.printLinkedList(h)