class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        x={}
        seen=[]
        z=[]
        for i in orders:
            if i[2] not in seen:
                seen.append(i[2])
            if int(i[1]) not in x:
                x[int(i[1])]=[i[2]]
            else:
                x[int(i[1])].append(i[2])
        seen.sort()
        z.append(["Table"]+seen)
        for i in sorted(list(x.keys())):
            a=[str(i)]
            for t in seen:
                a.append(str(x[i].count(t)))
            z.append(a)
        return z
