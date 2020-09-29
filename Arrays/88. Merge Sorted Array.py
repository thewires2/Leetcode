class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(len(nums2)):
            nums1[-i-1]=nums2[i]
        nums1.sort()
