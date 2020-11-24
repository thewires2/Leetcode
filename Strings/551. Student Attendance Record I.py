class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A')<=1:
            if 'LLL' in s:
               return False
            else:
                return True

