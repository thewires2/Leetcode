class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.x={}
        

    def insert(self, key: str, val: int) -> None:
        if key in self.x:
            self.x[key]=val
        self.x[key]=val

    def sum(self, prefix: str) -> int:
        y = 0
        for i,j in self.x.items():
            if prefix==i[:len(prefix)]:
                y+=j
        return y


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
