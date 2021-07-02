class Solution:
    def numSplits(self, s: str) -> int:
        c = Counter(s)
        d = set()
        ans = 0
        for i in range(len(s)):
            d.add(s[i])
            c[s[i]]-=1
            if  c[s[i]] == 0:
                del c[s[i]] 
            if len(d) == len(c):
                ans+=1
        return ans
