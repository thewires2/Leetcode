class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        positions = { k: i for i, k in enumerate(keyboard) }
        total_time = positions[word[0]] 
        for i in range(1, len(word)):
            total_time += abs(positions[word[i - 1]] - positions[word[i]]) 
        return total_time
