class Solution:
    def decodeString(self, s: str) -> str:
        x=[]
        t=""
        k=""
        j="0123456789"
        for i in s:
            f=True
            if i!="]":
                x.append(i)
            else:
                while True:
                    if x[-1]!="[" and x[-1].isnumeric()==False:
                        a=x.pop()
                        t+=a
                    elif x[-1]=="[":
                        x.pop()
                        while len(x)!=0 and x[-1].isnumeric():
                            a=x.pop()
                            k=a+k
                        x.append("".join(t for _ in range(int(k))))
                        k=""
                        t=""
                        break
        return "".join(d[::-1] for d in x)
