class Solution:
    def longestCommomSubsequence(self, arrays: List[List[int]]) -> List[int]:
        final=[]
        for i in range(len(arrays[0])):
            x=True
            for j in range(1,len(arrays)):
                if arrays[0][i] not in arrays[j]:
                    x=False
                    break
            if x:
                final.append(arrays[0][i])
        return final
