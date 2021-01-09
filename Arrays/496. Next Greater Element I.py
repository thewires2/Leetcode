class Solution:
    def nextGreaterElement(self, num1: List[int], num2: List[int]) -> List[int]:
        t=[]
        for i in num1:
            f=True
            for j in num2[num2.index(i):]:
                if j>i:
                    f=False
                    t.append(j)
                    break
            if f==True:
                t.append(-1)
        return t
                
