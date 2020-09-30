from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c=dict(Counter(nums))
        for i,j in c.items():
            if j==1:
                return i
