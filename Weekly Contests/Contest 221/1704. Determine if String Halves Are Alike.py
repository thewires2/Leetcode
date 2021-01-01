class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s.lower
        print(s[:len(s)//2],s[len(s)//2:])
        if sum([1 for i in s[:len(s)//2] if i in "aeiouAEIOU"]) == sum([1 for i in s[len(s)//2:] if i in "aeiouAEIOU"]):
            return True
        return False
