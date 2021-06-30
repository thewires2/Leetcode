class Solution:
    def maxDepth(self, s: str) -> int:
        z=0
        m=0
        for i in s:
            if i=="(":
                z+=1
            elif i==")":
                z-=1
            m=max(m,z)
        return m
