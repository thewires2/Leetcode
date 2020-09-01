class Solution:
       def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)-1
        g, ug = arr[-1], arr[-1]
        while l>=0:
            if arr[l]>g:
                g = arr[l]
            arr[l] = ug
            l-=1
            ug = g
        arr[-1] = -1
        return arr
