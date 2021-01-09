class Solution:
    def calPoints(self, ops: List[str]) -> int:
        t=[]
        for i in ops:
            if i.isnumeric():
                t.append(int(i))
            elif i=="+":
                t.append((t[-1]+t[-2]))
            elif i=="C":
                t.pop()
            elif i=="D":
                t.append(t[-1]*2)
            else:
                t.append(int(i))
        print(t)
        return sum(t)
