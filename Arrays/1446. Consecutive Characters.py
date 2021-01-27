class Solution:
    def maxPower(self, s: str) -> int:
        a=s[0]
        k=t=0
        for i in s:
            if i==a:
                k=k+1
                t=max(t,k)
            else:
                k=1
                a=i
        return t
