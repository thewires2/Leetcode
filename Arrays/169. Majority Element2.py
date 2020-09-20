from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        data=Counter(nums)
        return data.most_common(1)[0][0]
