class Solution:
    def simplifyPath(self, path: str) -> str:
        path=path.replace("//","/")
        x=path.split("/")
        t=[]
        x=[i for i in x if i!=""]
        print(x)
        for i in x:
            if i==".":
                continue
            elif i=="..":
                if t!=[]:
                    t.pop()
            else:
                t.append("/"+i)
        if t==[]:
            return "/"
        return "".join(i for i in t)
