class Solution:
    def customSortString(self, order: str, s: str) -> str:
        x={}
        f=""
        t=""
        for i in s:
            if i not in order:
                t+=i
            else:
                if i not in x:
                    x[i]=1
                else:
                    x[i]+=1
        for i in order:
            if i in x:
                f+=i*x[i]
        return f+t
