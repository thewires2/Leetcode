class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        x={}
        for i in knowledge:
            x[i[0]]=i[1]
        r=0
        s=s.replace("()","")
        t=""
        p=""
        while r<len(s):
            if s[r]=="(":
                r+=1
                while s[r]!=")":
                    t+=s[r]
                    r+=1
                try:
                    p+=x[t]
                except:
                    p+="?"
                t=""
                r+=1
            else:
                p+=s[r]
                r+=1
        return p
                
