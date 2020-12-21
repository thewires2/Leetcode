class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0:
            return False
        y=str(bin(n))[2:]
        if y.count("1")==1:
            return True
        return False
