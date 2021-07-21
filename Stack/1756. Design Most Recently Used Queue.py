class MRUQueue:

    def __init__(self, n: int):
        self.x=[i for i in range(1,n+1)]

    def fetch(self, k: int) -> int:        
        z=self.x[k-1]
        self.x.remove(z)
        self.x.append(z)
        return self.x[-1]


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
