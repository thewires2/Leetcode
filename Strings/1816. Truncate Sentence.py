class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(i for i in s.split(" ")[:k]).strip()
