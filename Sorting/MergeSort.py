class Solution(object):

    def merge_sort(self, lst):
        """Sorts the input list using the merge sort algorithm.

        >>> lst = [4, 5, 1, 6, 3]
        >>> merge_sort(lst)
        [1, 3, 4, 5, 6]
        """
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = self.merge_sort(lst[:mid])
        right = self.merge_sort(lst[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        """Takes two sorted lists and returns a single sorted list by comparing the
        elements one at a time.

        >>> left = [1, 5, 6]
        >>> right = [2, 3, 4]
        >>> merge(left, right)
        [1, 2, 3, 4, 5, 6]
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