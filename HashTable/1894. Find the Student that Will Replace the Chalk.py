class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s=sum(chalk)
        rounds=k//s
        k=k-s*rounds
        for i in range(len(chalk)):
            if chalk[i]>k:
                return i
            k-=chalk[i]
