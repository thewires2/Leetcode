class Solution:
    def longestWord(self, words: List[str]) -> str:
        def checkPrefixes(word):
            for i in range(len(word)-1, 0, -1):
                if not word[:i] in wordSet:
                    return False
            return True
        
        wordSet = set(words)
        words.sort()
        words.sort(key= lambda x: len(x), reverse=True) 
        for word in words:
            if checkPrefixes(word):
                return word
        
        return ""
