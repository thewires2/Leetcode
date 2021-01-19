class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        x=0
        l=0
        r=l+1
        while r<len(nums) and l<len(nums):
            if nums[r]-nums[l]<k or l==r:
                r=r+1
            elif nums[r]-nums[l]==k:
                x=x+1
                #print(nums[r],nums[l])
                l=l+1
                while (l < len(nums) and nums[l] == nums[l - 1]):
                    l += 1
            elif nums[r]-nums[l]>k:
                l=l+1
        return x
