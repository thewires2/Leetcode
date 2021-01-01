class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        k=0
        for i in set(s):
            if s.count(i)%2==0:
                k=k+1
        print(k,len(set(s)))
        if len(set(s))==k or len(set(s))==k+1:
            return True
        return False
