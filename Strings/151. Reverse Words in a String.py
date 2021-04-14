class Solution:
    def reverseWords(self, s: str) -> str:
        x=[i.strip() for i in s.split()][::-1]
        s=" ".join(i for i in x)
        s=s.strip()
        return s
