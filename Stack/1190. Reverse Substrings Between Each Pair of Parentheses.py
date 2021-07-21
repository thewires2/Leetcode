class Solution:
    def reverseParentheses(self, s: str) -> str:
        if not s:
            return ""
        x = []
        for i in s:
            if i!=")":
                x.append(i)
            else:
                t=[]
                while x[-1]!="(":
                    t.append(x.pop())
                x.pop()
                x+=t
        return "".join(i for i in x)
