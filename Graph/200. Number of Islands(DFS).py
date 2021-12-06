class Solution:  
    def numIslands(self, matrix: List[List[str]]) -> int:
        posX = [1,0,-1,0]
        posY = [0,1,0,-1]
        
        def check(j,i):
            if i<0 or j<0 or j==len(matrix) or i==len(matrix[0]) or matrix[j][i]!="1":
                return 
            else:
                matrix[j][i]="0"
                for m,n in zip(posX,posY):
                    check(m+j,n+i)
                
        k = 0
        
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                if matrix[j][i]=="1" :
                    k+=1
                    check(j,i)
        return k
                    
