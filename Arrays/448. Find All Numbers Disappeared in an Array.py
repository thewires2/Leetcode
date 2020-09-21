class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x=[i for i in range(1,len(nums)+1)]
        y=list(set(x).difference(set(nums)))
        return y
