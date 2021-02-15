class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda a:a[0])
        x=[]
        for i in intervals:
            if x==[] or x[-1][1]<=i[0]:
                x.append(i)
            else:
                return False
        return True
