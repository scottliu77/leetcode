'''

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.

'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # holds tuple where first value is time, second value is true if start, false if end
        times = []
        for interval in intervals:
            times.append((interval.start, True))
            times.append((interval.end, False))
        sorted_times = sorted(times, key = lambda time: (time[0], time[1]))
        max_count = count = 0
        for time in sorted_times:
            if time[1]:
                count += 1
            else:
                count -= 1
            max_count = max(max_count, count)
        return max_count