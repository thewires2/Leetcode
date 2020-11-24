class Solution:
    def maxScore(self, s: str) -> int:
        score=0
        for i in range(1,len(s)):
            x=s[:i].count("0")
            y=s[i:].count("1")
            score=max(score,x+y)
        return score
