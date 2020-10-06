class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        y=sum(A)-sum(set(A))
        z=len(A)//2
        z=z-1
        return y//z
