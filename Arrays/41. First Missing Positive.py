class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if nums==[]:
            return 1
        elif max(nums)>=0:
            x=max(nums)+2
            for i in range(1,x):
                if i not in nums:
                    return i
        else:
            return 1
