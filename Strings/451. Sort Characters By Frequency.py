class Solution:
    def frequencySort(self, s: str) -> str:
        x={}
        z=""
        for i in set(s):
            x[i]=s.count(i)
        d={k:v for k,v in sorted(x.items(), key=lambda a:a[1],reverse=True)}
        for i,j in d.items():
            for _ in range(j):
                z=z+i
        return z
