class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        i=0
        k=0
        while len(sticks)>1:
            sticks.sort()
            x=sticks.pop(0)
            y=sticks.pop(0)
            k+=x+y
            sticks.append(x+y)
        return k
        
