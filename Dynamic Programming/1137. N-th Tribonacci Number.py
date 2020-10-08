class Solution:
    def tribonacci(self, n: int) -> int:
        initial = [0,1,1]
        while len(initial)<=n:
            initial.append(sum(initial[-3:]))
        return initial[n]
