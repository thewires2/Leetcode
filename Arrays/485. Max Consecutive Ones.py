class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k=0
        t=0
        for i in nums:
            if i==1:
                k=k+1
                t=max(k,t)
            else:
                k=0
                
        return t
