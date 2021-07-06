class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s)==1:
            return 1
        i=0
        j=len(s)-1
        while i<j:
            if s[i]!=s[j]:
                break
            temp = s[i]
            while i<=j and s[i]==temp:
                i+=1
            while j>=i and s[j]==temp:
                j-=1
        return j-i+1
