class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        k=0
        for i in words:
            s=True
            for x in set(i):
                if i.count(x)<=chars.count(x):
                    continue
                else:
                    s=False
            if s==True:
                k=k+len(i)
        return k
