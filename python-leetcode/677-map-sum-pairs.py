'''

Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5


'''

class MapSum(object):
    class Node(object):
        def __init__(self, key):
            self.key = key
            self.val = 0
            self.children = {}
        
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = self.Node("")
        self.total = {}
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        update = val
        if key in self.total:
            update -= self.total[key]
        temp = self.head
        for s in key:
            if s in temp.children:
                temp = temp.children[s]
                temp.val += update
            else:
                (temp.children)[s] = self.Node(s)
                temp = temp.children[s]
                temp.val += update
        self.total[key] = val
                
    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        temp = self.head
        for s in prefix:
            if s not in temp.children:
                return 0
            temp = temp.children[s]
        return temp.val
            
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)