from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        t=[]
        for i in range(k):
             t.append(Counter(nums).most_common()[i][0])
        return t
