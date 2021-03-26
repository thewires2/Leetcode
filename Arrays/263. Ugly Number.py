class Solution:
    def isUgly(self, n: int) -> bool:
        while True:
            k=n
            if n%2==0:
                n=n//2
            if n%3==0:
                n=n//3
            if n%5==0:
                n=n//5
            if k==n:
                break
        if n==1:
            return True
