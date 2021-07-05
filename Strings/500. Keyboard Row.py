class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        x={
            0:"qwertyuiop",
            1:"asdfghjkl",
            2:"zxcvbnm"
        }
        k=[]
        for i in words:
            t=i.lower()
            for z in x:
                if set(t).issubset(set(x[z])):
                    k.append(i)
        return k
