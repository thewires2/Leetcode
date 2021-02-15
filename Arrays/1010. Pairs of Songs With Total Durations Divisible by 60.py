class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        x=collections.defaultdict(int)
        ret=0
        for t in time:
            if t%60==0:
                ret+=x[0]
            else:
                ret+=x[60-t%60]
            x[t%60]+=1
        return ret
