class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s)==0:
            return t
        x=list(s)
        y=list(t) 
        for i in x:
            if i in y:
                y.remove(i)
        return y[0]
