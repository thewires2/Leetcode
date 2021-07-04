class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        x=len(nums)-k
        t=nums.index(max(nums[:x+1]))
        return nums[t:t+k]
