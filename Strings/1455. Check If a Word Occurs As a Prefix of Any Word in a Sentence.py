class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        k=0
        x=list(map(str,sentence.split(" ")))
        print(x)
        for i in x:
            k=k+1
            print(i[:len(searchWord)])
            if i[:len(searchWord)]==searchWord:
                return k
        return -1
                
