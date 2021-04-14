class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k>len(nums):
            k=k%len(nums)
        n = len(nums)
        z = [0] * n
        for i in range(len(nums)):
            z[(i + k) % n] = nums[i]
        nums[:] = z
