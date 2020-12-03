class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        e=0
        o=0
        for i in position:
            if i%2==0:
                e=e+1
            else:
                o=o+1
        
        return min(e,o)
