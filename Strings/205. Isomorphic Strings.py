class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        x={}
        seen = []
        for i,j in zip(s,t):
            if i not in x:
                if j not in seen:
                    x[i]=j
                    seen.append(j)
                else:
                    return False
            else:
                if x[i]!=j:
                    return False
        print(x)
        return True
