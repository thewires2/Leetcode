class Solution:
    def removeVowels(self, S: str) -> str:
        Z=''
        for i in S:
            if i in 'aeiou':
                continue
            else:
                Z=Z+i
        return Z
