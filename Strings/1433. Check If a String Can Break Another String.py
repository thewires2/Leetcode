class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1=sorted(s1)
        s2=sorted(s2)
        t=0
        k=0
        print(s1,s2)
        for i,j in zip(s1,s2):
            if i==j:
                k+=1
            else:
                if i>j:
                    t+=1
                else:
                    t-=1
        print(t,k)
        if abs(t)+k==len(s1):
            return True
            
