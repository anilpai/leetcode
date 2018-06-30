"""
Add two numbers stored as linked list.
"""

# Definition for singly-linked list.

from LinkedList.ReorderList import Solution as LL


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


""""
 two non-empty linked lists representing two non-negative integers. 
 The digits are stored in reverse order and each of their nodes contain a single digit. 
 Add the two numbers and return it as a linked list.
"""


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        carry, curr = 0, head

        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = divmod(val, 10)
            curr.next = ListNode(val)
            curr = curr.next

        if carry == 1:
            curr.next = ListNode(1)

        return head.next


if __name__=='__main__':
    s = LL()
    s1 = Solution()
    head = s1.addTwoNumbers(s.createLinkedList([2, 4, 3]), s.createLinkedList([5, 6, 4]))
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)
