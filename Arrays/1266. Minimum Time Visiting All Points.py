class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x=points[0][0]
        y=points[0][1]
        k=0
        for i in range(len(points)-1):
            k+=max(abs(points[i][0]-points[i+1][0]),abs(points[i][1]-points[i+1][1]))
        return k
            
            
