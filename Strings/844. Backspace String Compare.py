class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=""
        t1=""
        for i in s:
            if i!="#":
                s1+=i
            elif i=="#":
                s1=s1[:-1]
        for j in t:
            if j!="#":
                t1+=j
            else:
                t1=t1[:-1]
        if s1==t1:
            return True
