class Solution:
    def freqAlphabets(self, s: str) -> str:
        res=''
        i=len(s)-1
        while i>=0:
            if s[i]=='#':
                b=int(s[i-2]+s[i-1])
                res+=chr(b+96)
                i-=3
            else:
                res+=chr(int(s[i])+96)
                i-=1
        return res[::-1]
