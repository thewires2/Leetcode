class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        x=int("".join(str(ord(i)-97) for i in firstWord))
        y=int("".join(str(ord(i)-97) for i in secondWord))
        z=int("".join(str(ord(i)-97) for i in targetWord))
        return (x+y)==z
        
