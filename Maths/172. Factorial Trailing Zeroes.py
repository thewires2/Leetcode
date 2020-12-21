class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n==0 or n==1: return 0
        def fact(x):
            if x==1:
                return 1
            else:
                return x * fact(x-1)
        s=0
        f=fact(n)
        if f%10==0:
            k=0
            while f%10==0:
                f=f//10
                k=k+1
            return k
        else:
            return 0
