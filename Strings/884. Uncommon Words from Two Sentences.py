class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        x=[]
        x1=s1.split(" ")
        x2=s2.split(" ")
        for i in x1:
            if i not in x2 and x1.count(i)==1:
                x.append(i)
        for j in x2:
            if j not in x1 and x2.count(j)==1:
                x.append(j)
        return x
                
