class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1=num1.replace("i","")
        num2=num2.replace("i","")
        x1,y1=num1.split("+")
        x2,y2=num2.split("+")
        x=int(x1)*int(x2)-(int(y1)*int(y2))
        y=int(x1)*int(y2)+int(x2)*int(y1)
        return str(x)+"+"+str(y)+"i"
