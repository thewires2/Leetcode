class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        k=0
        points=0
        max_points=0
        for _ in range(len(tokens)):
            while k<len(tokens) and tokens[k]<=power :
                power-=tokens[k]
                points+=1
                max_points=max(max_points,points)
                k+=1
            if points>=1:
                points-=1
                power+=tokens[-1]
                tokens.pop()
        return max_points
                
                
            
