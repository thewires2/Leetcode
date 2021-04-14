class Solution:
    def reverseWords(self, s: List[str]) -> None:
        string="".join(i for i in s)
        x=[i for i in string.split(" ")]
        string=" ".join(i for i in x[::-1])
        string=string.lstrip()
        x=[i for i in string]
        s[:]=x
        
