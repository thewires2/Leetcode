class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        x=[i for i in A if i%2==0]
        y=[i for i in A if i%2!=0]
        return x+y
