class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        x=[]
        for i in range(len(startTime)):
            if startTime[i]<=queryTime and endTime[i]>=queryTime:
                print(startTime[i],endTime[i])
                x.append(1)
        return sum(x)
