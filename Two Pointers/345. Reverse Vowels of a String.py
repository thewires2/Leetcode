class Solution:
    def reverseVowels(self, s: str) -> str:
        x=""
        a=""
        for i in s:
            if i in "aeiouAEIOU":
                x=x+i
        x=x[::-1]
        k=0
        for i in s:
            if i in "aeiouAEIOU":
                a=a+x[k]
                k=k+1
            else:
                a=a+i
        return a
                
