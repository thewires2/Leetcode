class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        x=[]
        for i,j in enumerate(mat):
            x.append(j[i])
            x.append(j[len(mat)-(i+1)])
        if len(mat)%2==0:
            return sum(x)
        else:
            y=mat[len(mat)//2]
            z=y[len(mat)//2]
            return sum(x)-z
        
            
