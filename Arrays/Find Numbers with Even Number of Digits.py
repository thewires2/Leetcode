class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            s=0
            while i>0:
                i=i//10
                s=s+1
            if s%2==0:
                count=count+1
        return count
