class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        def binary_search(arr, x):
            low = 0
            high = len(arr) - 1
            mid = 0
            while low <= high:
                mid = (high + low) // 2
                if arr[mid] < x:
                    low = mid + 1
                elif arr[mid] > x:
                    high = mid - 1
                else:
                    return mid
            return -1
        for i in mat[0]:
            k=1
            for j in range(1,len(mat)):
                if binary_search(mat[j],i)!=-1:
                    k+=1
            if k==len(mat):
                return i
        return -1
