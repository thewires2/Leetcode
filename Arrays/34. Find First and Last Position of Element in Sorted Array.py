class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        x=[]
        if target not in nums:
            return [-1,-1]
        for i,j in enumerate(nums):
            if j==target:
                x.append(i)
        return [min(x),max(x)]
