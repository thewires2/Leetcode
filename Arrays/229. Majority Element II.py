class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        x=set(nums)
        y=[a for a in x if nums.count(a)>(len(nums)//3)]
        return y
