class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        x="".join(str(i) for i in A)
        x=str(int(x)+K)
        a=[int(i) for i in x]
        return a
