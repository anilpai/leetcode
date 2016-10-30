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
    def MergeLists(self, headA, headB):
        head = Node(0)
        curr = head
        while headA is not None and headB is not None:
            if headA.val < headB.val:
                curr.next = headA
                headA = headA.next
            else:
                curr.next = headB
                headB = headB.next
            curr = curr.next
        if headA is None:
            curr.next = headB
        if headB is None:
            curr.next = headA
        return head.next

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
        :return: null
        '''
        while head:
            print(str(head.val))
            head = head.next
        return


if __name__ == '__main__':

    ll1 = random.sample(range(300), 6)
    ll2 = random.sample(range(300), 6)
    # ll1 = ll1.sort()
    # ll2 = ll2.sort()
    s = Solution()
    headA = s.createLinkedList(sorted(ll1))
    headB = s.createLinkedList(sorted(ll2))
    print("Sorted List A ")
    s.printLinkedList(headA)
    print("Sorted List B ")
    s.printLinkedList(headB)
    head = s.MergeLists(headA, headB)
    print("Merging A and B ")
    s.printLinkedList(head)