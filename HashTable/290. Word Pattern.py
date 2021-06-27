class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        x=s.split(" ")
        if len(x)!=len(pattern):
            return False
        a={}
        z={}
        for i,j in zip(pattern,x):
            if i not in a:
                if j in z:
                    return False
                else:
                    a[i]=j
                    z[j]=i
            else:
                if a[i]!=j:
                    return False
        return True
