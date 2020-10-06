class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if s=="":
            return t
        x=list(s)
        y=list(t)
        for i in x:
            if i in y:
                y.remove(i)
                
        return y[0]
