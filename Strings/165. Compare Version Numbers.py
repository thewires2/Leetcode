class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        x=list(map(int,version1.split(".")))
        y=list(map(int,version2.split(".")))
        if len(x)>len(y):
            a=[0 for _ in range(len(x)-len(y))]
            y+=a
        elif len(x)<len(y):
            a=[0 for _ in range(len(y)-len(x))]
            x=x+a
        for i,j in zip(x,y):
            if i>j:
                return 1
            elif i<j:
                return -1
        return 0
            
        
