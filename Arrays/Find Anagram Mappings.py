class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        x=[]
        for i in A:
            x.append(B.index(i))
        return x
