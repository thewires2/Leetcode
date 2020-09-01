class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        s=nums
        x=(max(nums))
        nums.remove(max(nums))
        a=(max(nums))
        pro=(a-1)*(x-1)
        return pro
