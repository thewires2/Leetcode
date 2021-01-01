class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l=0
        r=1
        k=0
        while r<len(s)+1:
            print(s[l:r])
            if s[l:r].count("L") == s[l:r].count("R"):
                k=k+1
                l=r
                r=r+1
            r=r+1
        return k
