class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff=float('inf')
        for i in range(len(nums)):
            lo,hi=i+1,len(nums)-1
            while lo<hi:
                sum=nums[i]+nums[lo]+nums[hi]
                if abs(diff)>abs(target-sum):
                    k=sum
                    diff=abs(target-sum)
                if sum<target:
                    lo+=1
                else:
                    hi-=1
                if diff==0:
                    break
        return k
            
