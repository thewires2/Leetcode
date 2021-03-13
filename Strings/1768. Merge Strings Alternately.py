class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x=""
        k=0
        while k<(min(len(word1),len(word2))):
            x+=word1[k]+word2[k]
            k+=1
        if word1:
            x+=word1[len(word2):]
        if word2:
            x+=word2[len(word1):]
        return x
