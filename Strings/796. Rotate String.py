class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s=s.strip()
        goal=goal.strip()
        if s==goal:
            return True
        for i in range(len(s)):
            if s[i:]+s[:i]==goal:
                return True
