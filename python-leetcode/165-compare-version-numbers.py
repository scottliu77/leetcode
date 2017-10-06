'''

Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37



'''



class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        arr1, arr2 = version1.split("."), version2.split(".")
        i = 0
        while i < len(arr1) and i < len(arr2):
            if int(arr1[i]) > int(arr2[i]):
                return 1
            if int(arr1[i]) < int(arr2[i]):
                return -1
            i += 1
        if len(arr1) == len(arr2):
            return 0
        elif len(arr1) > len(arr2):
            while i < len(arr1):
                if int(arr1[i]) != 0:
                    return 1
                i += 1
            return 0
        else:
            while i < len(arr2):
                if int(arr2[i]) != 0:
                    return -1
                i += 1
            return 0