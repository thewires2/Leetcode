class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
    
        def getPower(n):
            if n==1:
                return 0
            k=0
            while n!=1:
                if n%2==0:
                    n=n//2
                    k+=1
                else:
                    n=(n*3)+1
                    k+=1
            return k
        y=[]
        for x in range(lo,hi+1):
            y.append([x,getPower(x)])
        y.sort(key=lambda a:a[1])
        return y[k-1][0]
