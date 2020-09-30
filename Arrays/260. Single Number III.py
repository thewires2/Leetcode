from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x=[]
        c=dict(Counter(nums))
        for i,j in c.items():
            if j==1:
                x.append(i)
                
        return x
