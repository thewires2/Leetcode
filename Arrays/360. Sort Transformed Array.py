class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        return sorted([(a*(i*i)+b*i+c) for i in nums])
        
