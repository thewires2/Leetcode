class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        while part in s:
            for i in range(len(s)-len(part)+1):
                if s[i:i+len(part)]==part:
                    s=s[:i]+s[i+len(part):]
                    break
        return s
