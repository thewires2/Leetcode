class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        def nCr(n):
            import math
            f = math.factorial
            return f(n) / f(2) / f(n-2)
        s=set(nums)
        b=0
        for i in s:
            x=nums.count(i)
            if x>=2:
                b=b+nCr(x)
        
        return int(b)
