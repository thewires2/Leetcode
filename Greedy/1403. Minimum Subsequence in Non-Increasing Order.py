class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        x=[]
        for i in range(len(nums)):
            x.append(max(nums))
            nums.remove(max(nums))
            if sum(x)>sum(nums):
                break
        x.sort(reverse=True)
        return x
