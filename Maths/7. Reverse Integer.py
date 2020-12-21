class Solution:
    def reverse(self, x: int) -> int:
        f=False
        if x<0:
            f=True
        y=str(abs(x))
        y=y[::-1]
        x=int(y)
        if -2147483648<=x and x<=2147483647:
            if f==False:
                return x
            return -x
        return 0
