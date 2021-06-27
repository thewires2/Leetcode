class Solution:
    def countSegments(self, s: str) -> int:
        s=s.strip()
        if not s:
            return 0
        k=0
        t=""
        for i in s:
            if i!=" ":
                t+=i
            else:
                if t!="":
                    k+=1
                    t=""
        return k+1
