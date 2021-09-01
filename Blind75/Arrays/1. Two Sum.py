class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}
        for i in range(len(nums)):
            if target-nums[i] in x:
                return [x[target-nums[i]],i]
            x[nums[i]]=i
        print(x)
