class Solution:
    def findLonelyPixel(self, k: List[List[str]]) -> int:
        x=[]
        a=0
        y=[]
        for i in k:
            if i.count("B")==0:
                continue
            if i.count("B")>1:
                y+=[i for i, n in enumerate(i) if n == 'B']
                continue
            x.append(i.index("B"))
        #print(x)
        for i in x:
            if x.count(i)==1 and y.count(i)==0:
                a=a+1
        return a
                
