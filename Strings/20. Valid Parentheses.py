class Solution:
    def isValid(self, s: str) -> bool:
        d=["()","[]","{}"]
        while True:
            k=False
            for i in d:
                if s=="":
                    return True
                if i in s:
                    k=True
                    s=s.replace(i,"")
            if k==False and s!="":
                return False
