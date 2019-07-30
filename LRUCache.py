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

if __name__ == "__main__":


    cache = LRUCache(2);

    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))      
    # returns 1
    cache.put(3, 3)  
    # delete key 2
    cache.get(2)       
    # returns -1 (not found)
    cache.put(4, 4)    
    # evicts key 1
    print(cache.get(1))       
    # returns -1 (not found)
    cache.get(3)       
    # returns 3
    cache.get(4)       
    # returns 4