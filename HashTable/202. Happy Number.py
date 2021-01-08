class Solution:
    def isHappy(self, n: int) -> bool:
        x=[]
        def Happy(n,x):
            t,k=0,0
            while n>0:
                t=n%10
                n=n//10
                k=k+t*t
            if k==1:
                return True
            else:
                if k in x:
                    return False
                else:
                    x.append(k)
                    return Happy(k,x)
        return Happy(n,x)
