class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        x=[0]
        k=0
        for i in gain:
            k=k+i
            x.append(k)
        return max(x)
