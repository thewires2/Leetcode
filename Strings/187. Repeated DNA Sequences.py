class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        x={}
        t=[]
        for i in range(len(s)-9):
            if s[i:i+10] not in x:
                x[s[i:i+10]]=1
            else:
                x[s[i:i+10]]+=1
        for i in x:
            if x[i]>1:
                t.append(i)
        return t
                
            
            
