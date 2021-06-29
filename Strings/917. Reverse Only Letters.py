class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        t=""
        r=""
        f=""
        for i in s:
            if i.isalpha()==True:
                r+=i
            else:
                t+=i
        r=r[::-1]
        m=0
        n=0
        for i in range(len(s)):
            if s[i].isalpha()==True:
                f+=r[m]
                m+=1
            else:
                f+=t[n]
                n+=1
        return f
