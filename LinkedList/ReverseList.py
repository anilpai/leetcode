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
    def ReverseList(self, head):
        prev, curr = None, head

        while curr:
            prev, curr.next, curr = curr, prev, curr.next

        return prev

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
    # print(head.val)
    print("Before reordering: ")
    s.printLinkedList(head)
    head = s.ReverseList(head)
    print("After reversing: ")
    s.printLinkedList(head)