class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        x=[]
        x.append(start)
        for i in range(1,n):
            x.append(start + 2*i)
        z=x[0]
        for i in range(1,len(x)):
            z=z^x[i]
        return z
