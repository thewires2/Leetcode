class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        x=int(((len(arr)+1)/2)*(arr[0]+arr[-1]))
        return x-sum(arr)
