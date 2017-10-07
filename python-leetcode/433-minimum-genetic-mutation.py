import sys
from collections import deque

class Solution(object):

    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        chars = ['A', 'C', 'G', 'T']
        visited = set()
        bankSet = set(bank)
        dist = {}
        bank.append(start)
        if end not in bankSet:
            return -1
        for word in bank:
            dist[word] = sys.maxint
        dist[start] = 0
        queue = deque()        
        queue.append(start)
        while queue:
            curr = queue.popleft()
            visited.add(curr)
            s = list(curr)
            for i in xrange(len(s)):
                curr_char = s[i];
                for char in chars:
                    if curr_char != char:
                        s[i] = char
                        temp = ''.join(s)
                        if temp in bankSet and temp not in visited:
                            dist[temp] = min(dist[temp], dist[curr] + 1)
                            queue.append(temp)
                s[i] = curr_char
        return dist[end] if dist[end] != sys.maxint else -1