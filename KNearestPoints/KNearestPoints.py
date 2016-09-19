import math
import heapq


class Point(object):
    """
    A Point on a 2D space has x and y co-ordinates.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Solution(object):
    '''
    Find the distance between a given point and k nearest points from that point.
    '''
    def distance(self, p0, p1):
        '''
        distance between two points using Distance Formulae.
        '''
        return math.sqrt((p0.x - p1.x)**2 + (p0.y - p1.y)**2)

    def KNearestPoints(self, p0, k=1, lst=None):
        '''
        K neighbouring points from a given point p0
        :param p0: Given 2D Point
        :param k: number of 2D points
        :return: list of K nearest points
        '''
        given = p0
        if len(lst) == 0:
            return None

        heap = [(self.distance(given, item), item) for item in lst]

        heapq.heapify(heap)

        # Get the K nearest points.
        final_list = []
        for i in range(k):
            value, key = heapq.heappop(heap)
            final_list.append((key.x, key.y))

        return final_list

if __name__ == '__main__':
    # Given Point
    p0 = Point(0, 0)
    # List of Points
    l = [Point(0, 2), Point(2, 0), Point(4, 1), Point(1, 3), Point(2, 2), Point(5, 3), Point(10, 8)]
    s = Solution()
    print(s.KNearestPoints(p0, 2, l))
