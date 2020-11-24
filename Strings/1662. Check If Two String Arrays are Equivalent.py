class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        x="".join(word for word in word1)
        y="".join(word for word in word2)
        if x==y:
            return True
        return False
