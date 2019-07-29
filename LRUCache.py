class LRUCache(object):
    def __init__(self, capacity):
        from collections import OrderedDict 
        """
        :type capacity: int
        """
        self.limit = capacity
        self.cache = OrderedDict()
        self.size = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            val = self.cache.pop(key)
            self.cache[key] = val
            return self.cache[key]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.cache.pop(key)
            self.size -= 1
        elif self.size == self.limit:
            self.cache.popitem(last=False)
            self.size -= 1
        self.cache[key] = value
        self.size += 1
"""
explanation: 

Effciency:
All operations are of O(1) since the cache is implemented by OrderedDict

Design Choice:
I use OrderedDict to make the code look more compact and elegant. The put method might be a 
little different from the requirement but I believe it is more reasonable to perform an 
"use operation" when the key is already in the cache and we update its value


"""