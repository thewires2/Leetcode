class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        a_sum = sum(A)
        b_sum = sum(B)
        b_set=list(set(B))
        for i in range(len(A)):
            if (b_sum - a_sum)//2 + A[i] in b_set:
                return([A[i], (b_sum - a_sum)//2 + A[i]])
