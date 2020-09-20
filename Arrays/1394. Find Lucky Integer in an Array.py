class Solution:
    def findLucky(self, arr: List[int]) -> int:
        x=[i for i in arr if arr.count(i)==i]
        if not x:
            return -1
        else:
            return max(x)

        
