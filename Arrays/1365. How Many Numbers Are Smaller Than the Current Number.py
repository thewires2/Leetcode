class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        x=[]
        for i in nums:
            x.append(sum([1 for y in nums if y<i]))
        return x
