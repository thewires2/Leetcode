class Solution:
    def longestOnes(self, nums: List[int], K: int) -> int:
        left = 0
        for right in range(len(nums)):
            K -= 1 - nums[right]
            if K < 0:
                K += 1 - nums[left]
                left += 1
        return right - left + 1
        
