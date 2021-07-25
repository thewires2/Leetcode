class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        x={}
        y=[]
        for i in range(len(groupSizes)):
            if groupSizes[i] not in x:
                x[groupSizes[i]]=[i]
            else:
                if len(x[groupSizes[i]])==groupSizes[i]:
                    y.append(x[groupSizes[i]])
                    x[groupSizes[i]]=[i]
                else:
                    x[groupSizes[i]].append(i)
                    
        for i in x:
            y.append(x[i])
        return y
