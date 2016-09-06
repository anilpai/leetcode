# Definition for singly-linked list.
import random


class ListNode(object):
    """
    Singly Linked List Node with a value and next pointer
    """
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
    """
    Solution to the problem or reordering list
    """
    def ReorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        # to find the central node using fast-slow method
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # to reverse the second half of list in-place
        prev, curr = None, slow
        while curr:
            prev, curr.next, curr = curr, prev, curr.next

        # Merge in-place;
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        return head

    def LinkedListToList(self, head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

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
    #ll = [1, 2, 3, 4]
    ll = random.sample(range(300), 8)
    s = Solution()
    head = s.createLinkedList(ll)
    print("Before reordering: ")
    s.printLinkedList(head)
    head = s.ReorderList(head)
    print("After reordering: ")
    s.printLinkedList(head)
