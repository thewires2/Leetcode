class Solution:
    def thousandSeparator(self, n: int) -> str:
        if len(str(n))<=3:
            return str(n)
        x=len(str(n))//3
        y=str(n)
        y=y[::-1]
        a=""
        for i in range(len(y)):
            a=a+y[i]
            if (i+1)%3==0 and (i+1)!=len(y):
                a=a+"."
            
        return a[::-1]
