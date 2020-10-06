class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        k=nums[0]
        for i in range(1,len(nums)+1):
            if i in nums:
                continue
            k=i
        z=[]
        z.append(sum(nums)-sum(set(nums)))
        z.append(k)
        return z
