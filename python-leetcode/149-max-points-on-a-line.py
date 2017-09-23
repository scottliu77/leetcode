'''


Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.


'''

# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b



import numpy as np

class Solution(object):

	'''
	O(n^2) time

	'''
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        max_value = 0
        if len(points) <= 2:
            return len(points)
        for i in xrange(len(points) - 1):
            undef = 1
            same_point = 1
            d = {}
            for j in xrange(i+1, len(points)):
                if points[j].x == points[i].x and points[j].y == points[i].y:
                    same_point += 1
                elif points[j].x == points[i].x:
                    undef += 1
                else:
                	# Need to use longdouble to preserve precision
                    slope = (float(points[j].y - points[i].y) * np.longdouble(1))/(points[j].x - points[i].x)
                    if slope in d:
                        d[slope] = d[slope] + 1
                    else:
                        d[slope] = 1
                max_value = max(max_value, same_point)
                for value in d.values():
                    max_value = max(max_value, value + same_point)
                max_value = max(max_value, undef)
            
        return max_value
