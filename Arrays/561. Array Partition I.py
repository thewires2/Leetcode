class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        k=0
        for i in range(0,len(nums),2):
            k+=nums[i]
        return k
