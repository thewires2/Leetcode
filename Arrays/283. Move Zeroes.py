class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        x=nums.count(0)
        for _ in range(x):
            nums.remove(0)
        for _ in range(x):
            nums.append(0)
        
