class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        submax=0
        c=nums[0]
        for i in nums:
            submax=submax+i
            if submax > c:
                c=submax
            if submax<0:
                submax=0
        return c
