class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums))<3:
            return max(nums)
        for i in range(2):
            for i in range(nums.count(max(nums))):
                nums.remove(max(nums))
        return max(nums)
