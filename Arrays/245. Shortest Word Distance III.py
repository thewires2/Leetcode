class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        x=[]
        y=[]
        k=inf
        for i in range(len(words)):
            if words[i]==word1:
                x.append(i)
            if words[i]==word2:
                y.append(i)
        print(x,y)
        for i in x:
            for j in y:
                if i!=j:
                    k=min(k,abs(i-j))
        return k
