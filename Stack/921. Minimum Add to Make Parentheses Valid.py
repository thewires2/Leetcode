class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        x=[]
        
        for i in s:
            if i=="(":
                x.append("(")
            else:
                if x:
                    if x[-1]=="(":
                        x.pop()
                    else:
                        x.append(")")
                else:
                    x.append(")")
        return len(x)
