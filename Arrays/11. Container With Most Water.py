class Solution:
    def maxArea(self, arr: List[int]) -> int:
        max_area = 0
        l=0
        r=len(arr)-1
        while l<r:
            max_area = max(max_area,(min(arr[l],arr[r])*(r-l)))
            if arr[l]<arr[r]:
                l=l+1
            else:
                r=r-1
        return max_area
