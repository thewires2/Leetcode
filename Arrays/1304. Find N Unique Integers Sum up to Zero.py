class Solution:
    def sumZero(self, n: int) -> List[int]:
        s=-1
        x=[]
        if n%2==0:
            for i in range(n//2):
                x.append(s)
                x.append(abs(s))
                s=s-1
        else:
            x.append(0)
            for i in range(n//2):
                x.append(s)
                x.append(abs(s))
                s=s-1
        return x
