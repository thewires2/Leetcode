class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        for i,j in enumerate(A):
            if i==j:
                return i
        return -1
