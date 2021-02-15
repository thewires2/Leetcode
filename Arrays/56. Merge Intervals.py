class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda a:a[0])
        x=[]
        for i in intervals:
            if x==[] or x[-1][1]<i[0]:
                x.append(i)
            else:
                x[-1][1]=max(i[1],x[-1][1])
        return x
            
