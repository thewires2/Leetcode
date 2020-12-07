class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        s=[]
        odd = [x for x in A if x%2!=0]
        even = [x for x in A if x%2==0]
        for i in range(len(A)//2):
            s.append(even[i])
            s.append(odd[i])
        return s
