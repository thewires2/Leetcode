class Solution:
    def countLetters(self, S: str) -> int:
        x=""
        a=[]
        for i in S:
            if x=="":
                x=x+i
            elif i in x:
                x=x+i
            else:
                if len(x)!=1:
                    a.append((len(x)*(len(x)+1))//2)
                else:
                    a.append(1)
                x=""
                x=x+i
        if len(x)!=1:
            a.append((len(x)*(len(x)+1))//2)
        else:
            a.append(1)
        return sum(a)
