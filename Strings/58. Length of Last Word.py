class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        try:
            x=list(map(str,s.split()))
            return len(x[-1])
        except:
            return 0
