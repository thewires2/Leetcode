class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        x="abcdefghijklmnopqrstuvwxyz"
        
        for i in x:
            if i not in sentence:
                return False
        return True
