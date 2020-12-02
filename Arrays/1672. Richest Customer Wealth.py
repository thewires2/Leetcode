class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        k=0
        for x in accounts:
            k=max(k,sum(x))
        return k
