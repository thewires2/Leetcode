class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        x=m
        y=n
        for i in ops:
            x=min(x,i[0])
            y=min(y,i[1])
        return x*y
