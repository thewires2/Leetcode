class Solution:
    def isArmstrong(self, N: int) -> bool:
        x=list(map(int,str(N)))
        b=list(map(lambda s:s**len(x),x))
        if N==sum(b):
            return True
        else:
            return False
        
