class RandomizedSet:

    def __init__(self):
        self.x={}
        self.s=[]
        

    def insert(self, val: int) -> bool:
        if val in self.x:
            return False
        else:
            self.x[val]=len(self.s)
            self.s.append(val)
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.x:
            a,b=self.s[-1],self.x[val]
            self.s[b],self.x[a]=a,b
            self.s.pop()
            del self.x[val]
            return True

    def getRandom(self) -> int:
        return choice(self.s)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
