class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg=(sum(nums[:k]))/k
        print(*nums[:k])
        if len(nums)==k:
            return avg
        l=1
        r=k+1
        z=avg
        while r<len(nums)+1:
            s=(avg*k - nums[l-1] + nums[r-1])/k
            print(s)
            z=max(z,s)
            avg=s
            l=l+1
            r=r+1
        return z
