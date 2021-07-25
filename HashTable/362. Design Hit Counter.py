class HitCounter:

    def __init__(self):
        self.x={}
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if timestamp not in self.x:
            self.x[timestamp]=0
        self.x[timestamp]+=1 
        
        

    def getHits(self, timestamp: int) -> int:
        initial=timestamp-300
        hits=0
        for i in range(initial+1,timestamp+1):
            if i in self.x:
                hits+=self.x[i]
        return hits


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
