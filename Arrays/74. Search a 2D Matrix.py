class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if i==[]:
                return False
            if target>max(i):
                continue
            elif target in i:
                return True
            else:
                print("c") 
                return False
