class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        counter=0
        nums.sort()
        for i in range(len(nums)-1,1,-1):
            lo,hi=0,i-1
            while lo<hi:
                if nums[lo]+nums[hi]>nums[i]:
                    counter+=hi-lo
                    hi-=1
                elif nums[lo]+nums[hi]<=nums[i]:
                    lo+=1
        return counter
