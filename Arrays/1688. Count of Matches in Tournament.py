class Solution:
    def numberOfMatches(self, n: int) -> int:
        k=0
        if n==1:
            return 0
        while n>0:
            if n==2:
                k=k+1
                break
            if n%2==0:
                n=n//2
                k=k+n
            else:
                k=k+(n//2)
                n=(n//2)+1
        return k
