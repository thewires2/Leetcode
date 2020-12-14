class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        k=0
        for i in words:
            if set(i).issubset(set(allowed))==True:
                k=k+1
        return k
