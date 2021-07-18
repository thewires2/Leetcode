class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        x={}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] not in x:
                    x[mat[i][j]]=1
                else:
                    x[mat[i][j]]+=1
                if x[mat[i][j]]==len(mat):
                    return mat[i][j]
        return -1
            
