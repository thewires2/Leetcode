class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        if target==[]:
            return []
        k=0
        s=[]
        for i in range(1,target[-1]+1):
            if i==target[k]:
                s.append("Push")
                k+=1
            else:
                s.append("Push")
                s.append("Pop")
        return s
                
