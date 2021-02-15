class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        k=0
        x={}
        for i in nums:
            if i not in x:
                x[i]=1
            else:
                x[i]+=1
        for i,j in x.items():
            if j==1:
                k+=i
        return k
        
