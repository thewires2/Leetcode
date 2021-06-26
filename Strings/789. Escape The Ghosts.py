class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        float_pac = abs(target[0])+abs(target[1])
        for i in ghosts:
            x=abs(target[0]-i[0])+abs(target[1]-i[1])
            if float_pac>=x:
                return False
        return True
