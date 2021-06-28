class Solution:
    def minOperations(self, logs: List[str]) -> int:
        k=0
        for i in logs:
            if i=="../":
                if k!=0:
                    k=k-1
            elif i=="./":
                k=k
            else:
                k+=1
        return k
