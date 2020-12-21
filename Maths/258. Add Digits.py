class Solution:
    def addDigits(self, num: int) -> int:
        while num>9:
            s=[]
            x=num
            while x>0:
                s.append(x%10)
                x=x//10
            num=sum(s)
        return num
