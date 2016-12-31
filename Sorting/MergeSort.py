class Solution(object):

    def merge_sort(self, l):
        """
        Sorts the input list using the merge sort algorithm.
        """
        if len(l) <= 1:
            return l
        mid = len(l) // 2
        left = self.merge_sort(l[:mid])
        right = self.merge_sort(l[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        """
        Takes two sorted lists and returns a single sorted list by comparing the
        elements one at a time.
        """
        if not left:
            return right
        if not right:
            return left
        if left[0] < right[0]:
            return [left[0]] + self.merge(left[1:], right)
        return [right[0]] + self.merge(left, right[1:])


if __name__=='__main__':
    s = Solution()
    a = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2]
    print(s.merge_sort(a))