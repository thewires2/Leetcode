class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        x="".join(i for i in sorted(str(N)))
        for i in range(30):
            s="".join(i for i in sorted(str(2**i)))
            if s==x:
                print(s)
                return True
        return False
