class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        t = 0
        sum = 0
        for x in range(k):
            sum+=calories[x]
        if sum<lower:
            t-=1
        elif sum>upper:
            t+=1
        for i in range(k,len(calories)):
            sum+=calories[i]-calories[i-(k)]
            if sum<lower:
                t-=1
            elif sum>upper:
                t+=1
        return t
