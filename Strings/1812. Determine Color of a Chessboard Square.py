class Solution:
    def squareIsWhite(self, s: str) -> bool:
        if (ord(s[0])+int(s[1]))%2==0:
            return False
        return True
