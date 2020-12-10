class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        z={}
        d=[]
        for i in cpdomains:
            s=[]
            x,y=i.split(" ")
            if y.count(".")==1:
                s.append(y)
                a,b=y.split(".")
                s.append(b)
            if y.count(".")==2:
                s.append(y)
                a,b,c=y.split(".")
                s.append(b+"."+c)
                s.append(c)
            for i in s:
                if i not in z:
                    z[i]=int(x)
                else:
                    z[i]=z[i]+int(x)
        for i,j in z.items():
            d.append(str(j)+" "+i)
        return d
