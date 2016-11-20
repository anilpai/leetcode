from collections import defaultdict
from itertools import combinations


class Point(object):
    """
    A Point on a 2D space has x and y co-ordinates.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)


class Solution(object):
    def collinear(self, points):
        d = defaultdict(set)
        for p, q, r in combinations(points, 3):
            # To check if the area is zero.
            area = (p.x * (q.y - r.y) + q.x * (r.y - p.y) + r.x * (p.y - q.y)) / 2
            if area == 0:
                print(p, q, r)

if __name__=='__main__':
    # List of Points
    l = [Point(0, 2), Point(2, 0), Point(4, 1), Point(1, 3), Point(2, 2), Point(5, 3), Point(10, 8)]
    s = Solution()
    s.collinear(l)
    l = [Point(0, 0), Point(1, 1), Point(3, 4), Point(2, 2)]
    s.collinear(l)
