class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        flat_list = [item for sublist in grid for item in sublist]
        for x in flat_list:
            if x<0:
                count=count+1
        return count
