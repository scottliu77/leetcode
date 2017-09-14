'''

Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.

Example 1:

Input: ["23:59","00:00"]
Output: 1

Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.

'''


class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        
        times = []
        
        for tp in timePoints:
            splitted = tp.split(":")
            time = 60 * int(splitted[0]) + int(splitted[1])
            if time == 0:
                time = 1440
            times.append(time)
        
        
        times.sort()
        
        minDiff = 1440;
        if(len(times) > 2):
            for i in range(len(times) - 1):
                if times[i+1] - times[i] < minDiff:
                    minDiff = times[i+1] - times[i];
                
        edge = min(times[len(times) - 1] - times[0], 24*60 - times[len(times) - 1] + times[0])

        if edge < minDiff:
            minDiff = edge
        
        return minDiff
        