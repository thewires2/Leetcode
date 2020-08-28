import collections
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if len(text)<7:
            return 0
        count=collections.Counter(text)
        z=count['b']
        while z>0:
            if count['a']>=1*z and count['l']>=2*z and count['o']>=2*z and count['n']>=1*z:
                return z
            z=z-1
        else:
            return 0
        
