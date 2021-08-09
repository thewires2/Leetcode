class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        def recurse(amount,arr,memo={}):
            if amount in memo: return memo[amount]
            if amount == 0: return []
            if amount<0: return None
            shortestCombination=None
            for num in arr:
                remainder = amount-num
                result= recurse(remainder,arr,memo)
                if result!=None:
                    combination=result+[num]
                    if shortestCombination==None or len(combination)<len(shortestCombination):
                        shortestCombination=combination
            memo[amount]=shortestCombination
            return shortestCombination
        k=recurse(amount,coins)
        if k==None:
            return -1
        return len(k)
