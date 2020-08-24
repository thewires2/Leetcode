class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(1,len(nums),2):
            x=nums[i-1]
            while x>0:
                a.append(nums[i])
                x=x-1
        return a
