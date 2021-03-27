class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        a=[]
        x={}
        for i in set(words):
            x[i]=words.count(i)
        a = sorted(x, key=lambda i: (-x[i], i))
        return a[:k]
