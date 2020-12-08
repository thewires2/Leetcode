class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        f=False
        k=0
        if digits[0]==0:
            f=True
            for i in range(len(digits)):
                if digits[i]==0:
                    k=k+1
                else:
                    break
                
        x=[]
        a="".join(str(x) for x in digits)
        a=int(a)
        a=a+1
        a=str(a)
        for i in a:
            x.append(int(i))
        if f==False:
            return x
        else:
            y=[0 for _ in range(k-1)]
            y=y+x
            return y
    
