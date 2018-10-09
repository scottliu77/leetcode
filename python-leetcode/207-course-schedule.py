'''
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.

'''

from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        d = {}
        in_degrees = [0] * numCourses
        for pair in prerequisites:
            second, first = pair
            in_degrees[second] += 1
            if first in d:
                d[first].append(second)
            else:
                d[first] = [second]
        q = deque()
        for i in xrange(len(in_degrees)):
            if not in_degrees[i]:
                q.append(i)
        count = 0
        while q:
            curr = q.popleft()
            count += 1
            adj = d.get(curr, [])
            for vertex in adj:
                in_degrees[vertex] -= 1
                if in_degrees[vertex] == 0:
                    q.append(vertex)
        return count == numCourses