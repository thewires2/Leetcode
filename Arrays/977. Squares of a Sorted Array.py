class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        a=[i*i for i in A]
        a.sort()
        return a
    
