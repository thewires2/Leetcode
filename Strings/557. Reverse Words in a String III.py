class Solution:
    def reverseWords(self, s: str) -> str:
        q=''
        x=list(map(str,s.split(" ")))
        for i in x:
            q=q+i[::-1]
            q=q+" "
        return q.strip()
