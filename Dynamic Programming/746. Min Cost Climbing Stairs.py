class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)
        
        cost_at_i = 0
        cost_at_i_minus_1 = 0
        cost_at_i_minus_2 = 0
        
        for i in range(len(cost)):
            cost_at_i_minus_2 = cost_at_i_minus_1
            cost_at_i_minus_1 = cost_at_i
            cost_at_i = cost[i] + min(cost_at_i_minus_1, cost_at_i_minus_2)
        
        return min(cost_at_i, cost_at_i_minus_1)
