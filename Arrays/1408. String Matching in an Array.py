class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        x=[]
        for i in words:
            for j in words:
                if i==j:
                    continue
                if i in j:
                    x.append(i)
        x=list(set(x))
        return x
