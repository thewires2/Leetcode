class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        counter=0
        nums.sort()
        for i in range(len(nums)):
            lo,hi=i+1,len(nums)-1
            while lo<hi:
                k=nums[i]+nums[lo]+nums[hi]
                #print(nums[i],nums[lo],nums[hi])
                if target-k>0:
                    counter+=hi-lo
                    lo+=1
                else:
                    hi-=1                       
        return counter
