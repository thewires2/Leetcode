class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        s=min(A)
        a=0
        while s>0:
            a=a+(s%10)
            s=s//10
        if a%2==0:
            return 1
        else:
            return 0
            
