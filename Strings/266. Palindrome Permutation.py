class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        x={}
        k=0
        for i in set(s):
            x[i]=s.count(i)
        for i,j in x.items():
            if j%2!=0:
                k=k+1
            if k>1:
                return False
        return True
