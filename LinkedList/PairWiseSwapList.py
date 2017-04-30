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
    Solution to the problem of pairwise swap singly linked list
    """

    def swapPairs(self, head):
        '''
        Solution provided by leetcode.
        Source: https://leetcode.com/problems/swap-nodes-in-pairs/#/solutions
        '''
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next

    def PairWiseSwap(self, prev):
        '''
        My solution.
        '''
        if prev is None:
            return None
        else:
            if prev.next is None:
                return prev

        curr = prev.next
        if curr is not None:
            tmp = curr.next
            curr.next = prev
            prev.next = self.PairWiseSwap(tmp)
        return curr

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
    print("Before swapping: ")
    s.printLinkedList(head)
    print("After swapping: ")
    if head is None or head.next is None:
        new_head = head
    else:
        new_head = head.next
        s.PairWiseSwap(head)
    s.printLinkedList(new_head)
    print("Using Swap Pairs function to test:")
    s.printLinkedList(s.swapPairs(new_head))