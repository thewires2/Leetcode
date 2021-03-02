class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        x=[""]*len(strs[0])
        t=0
        for i in strs:
            k=0
            for j in i:
                x[k]+=j
                k+=1
        print(x)
        for i in x:
            a=("".join(x for x in sorted(i)))
            if i!=a:
                print(i,a)
                t+=1
        return t
