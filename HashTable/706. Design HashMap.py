class MyHashMap:

    def __init__(self):
        self.x={}
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.x[key]=value
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.x:
            return self.x[key]
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.x:
            del self.x[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
