from collections import deque

'''
Time Complexity is O(n)
'''


def maxSlidingWindow(nums, w):
    d = deque()
    out = []
    for i, n in enumerate(nums):
        # While there are elements in d and top (last) element is less than current element.
        while d and nums[d[-1]] < n:
            d.pop()
        d.append(i)
        # If the first element is equal to current index minus window size.
        if d[0] == i - w:
            d.popleft()

        # If the current index is greater than or equal to window size minus one, add that to output
        if i >= w - 1:
            out.append(nums[d[0]])
    return out

print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))