class Solution:
    def nthUglyNumber(self, n: int) -> int:
        x=[1]
        i1=i2=i3=0
        a=2
        b=3
        c=5
        for i in range(1,n):
            x.append(min(a,min(b,c)))
            if x[-1]==a:
                i1+=1
                a=x[i1]*2
            if x[-1]==b:
                i2+=1
                b=x[i2]*3
            if x[-1]==c:
                i3+=1
                c=x[i3]*5
        return x[n-1]
            
            
