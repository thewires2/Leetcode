class Solution:
    def sortSentence(self, s: str) -> str:
        t=""
        x=[]
        for i in s:
            if i.isnumeric()==False and i!=" ":
                t+=i
            elif i.isnumeric():
                x.append([t,int(i)])
                t=""
            elif i==" ":
                continue 
        x.sort(key=lambda a:a[1])
        return " ".join(a[0] for a in x).strip()
