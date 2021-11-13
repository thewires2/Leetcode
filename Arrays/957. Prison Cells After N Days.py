class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        
        visited = {}
        fast_forward = False
        
        while n>0:
            if not fast_forward:
                state_key = tuple(cells)
                if state_key in visited:
                    print(n)
                    n%=visited[state_key]-n
                    print(visited[state_key])
                    print(n)
                    fast_forward = True
                else:
                    visited[state_key]=n
                    
            if n>0:
                n-=1
                cells = self.nextday(cells)
        return cells
                
    def nextday(self,cells):
        ret = [0]
        for i in range(1,len(cells)-1):
            ret.append(int(cells[i-1]==cells[i+1]))
        ret.append(0)
        return ret
