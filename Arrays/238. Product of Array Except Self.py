import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        b=[]
        x=np.prod(nums)
        if nums.count(0)>1 or nums.count(0)==0:
            for i in nums:
                b.append(x//i)
            return b
        else:
            b=[0]*len(nums)
            a=nums.index(0)
            nums.remove(0)
            x=np.prod(nums)
            b[a]=x
            return b
            
