class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle=[]
        
        for i in range(rowIndex+1):
            row=[None for _ in range(i+1)]
            row[0],row[-1]=1,1
            
            for j in range(1,len(row)-1):
                row[j]=triangle[i-1][j]+triangle[i-1][j-1]
                
            triangle.append(row)
            
        return triangle[-1]
