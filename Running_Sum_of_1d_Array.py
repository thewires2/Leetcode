class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        for i in range(len(nums)):
            sum = nums[i] + sum
            nums[i] = sum
        return nums
