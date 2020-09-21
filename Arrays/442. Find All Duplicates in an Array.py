from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        x=[]
        z=dict(Counter(nums))
        z={k: v for k, v in sorted(z.items(), key=lambda item: item[1])}
        for k,v in z.items():
            if v==2:
                x.append(k)
        return x
    
