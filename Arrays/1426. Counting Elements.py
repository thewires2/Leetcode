class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        k=0
        for i in nums:
            if i+1 in nums:
                k=k+1
        return k
