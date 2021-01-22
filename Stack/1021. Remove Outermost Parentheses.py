class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        k=[]
        s=""
        l=0
        r=0
        for i in S:
            s+=i
            if i =="(":
                l=l+1
            if i==")":
                r=r+1
            if l==r:
                k.append(s)
                s=""
        s=""
        for i in k:
            s+=str(i[1:len(i)-1])
        print(s)
        return s
