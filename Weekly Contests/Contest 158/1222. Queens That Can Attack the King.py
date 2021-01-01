class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        x=[-1,0,1]
        res=[]
        for i in x:
            for j in x:
                if i==0 and j==0:
                    continue
                nx=king[0]
                ny=king[1]
                while nx<8 and ny<8 and nx>-1 and ny>-1:
                    if [nx,ny] in queens:
                        print(nx,ny)
                        res.append([nx,ny])
                        break
                    nx=nx+i
                    ny=ny+j
                    
        return res 
