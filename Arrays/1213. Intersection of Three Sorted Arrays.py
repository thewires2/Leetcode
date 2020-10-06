class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x=[]
        for i in nums1:
            if i in nums2:
                x.append(i)
                nums2.remove(i)
        return x
