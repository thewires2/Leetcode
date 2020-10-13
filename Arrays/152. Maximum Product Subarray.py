class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        a=nums[0]
        b=nums[0]
        result=a
        for i in range(1,len(nums)):
            curr=nums[i]
            temp_max=max(curr,a*curr,b*curr)
            b=min(curr,a*curr,b*curr)
            
            a=temp_max
            result=max(a,result)
        return result
        
