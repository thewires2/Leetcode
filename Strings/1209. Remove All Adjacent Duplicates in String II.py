class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        t=0
        while True:
            a=len(s)
            for j in range(len(s)):
                if j==0 or s[j-1]!=s[j]:
                    t=1
                else:
                    t=t+1
                if t==k:
                    s=s.replace(s[j]*k,"")
                    j=0
                    break
            if a==len(s):
                break
        return s
                
                
                
                
