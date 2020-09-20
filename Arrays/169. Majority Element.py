from collections import Counter
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:      
        data = Counter(nums)
        print(data.most_common())   # Returns all unique items and their counts
        print(data.most_common(1))  # Returns most common element and count
        if data.most_common(1)[0][0]==target and data.most_common(1)[0][1]>(len(nums)//2):
            return True
        else:
            return False
