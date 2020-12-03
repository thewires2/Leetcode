class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        while len(stones)!=1:
            x=stones[0]
            y=stones[1]
            if x==y:
                if len(stones)==2:
                    stones=[]
                    return 0
                stones=stones[2:]
            else:
                stones=stones[2:]
                stones.append(abs(x-y))
            stones.sort(reverse=True)
        return stones[0]
