class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        for i in range(1,n):
            if ((i*(i+1))//2)<=n and (((i+1)*((i+2))//2))>n:
                return i
            else:
                continue
        
