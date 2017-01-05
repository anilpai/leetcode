# Definition for singly-linked list.
import random


class ListNode(object):

    def __init__(self, x=None, next=None):
        self.val = x
        self.next = next


class Solution(object):
    """
    Find the merging node.
    """

    def MergingNode(self, headA, headB):
        currA = headA
        currB = headB
        while currA != currB:

            # If you reach end of one list , start from beginning of another.
            if currA.next is not None:
                currA = currA.next
            else:
                currA = headB

            if currB.next is not None:
                currB = currB.next
            else:
                currB = headA

        return currA.val

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

    ll1 = random.sample(range(300), 6)
    ll2 = random.sample(range(1000), 3)
    s = Solution()
    head1 = s.createLinkedList(ll1)
    head2 = s.createLinkedList(ll2)
    curr = head2
    while curr.next:
        curr = curr.next
    curr.next = head1.next.next
    print("Linked List A ")
    s.printLinkedList(head1)
    print("Linked List B ")
    s.printLinkedList(head2)
    print("Merging Node :")
    print(s.MergingNode(head1, head2))
