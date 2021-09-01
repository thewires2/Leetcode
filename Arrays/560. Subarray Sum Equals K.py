class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum = 0
        x = defaultdict(int)
        nums = [0] + nums
        for i in range(len(nums)):
            sum+=nums[i]
            count+=x[sum-k]
            x[sum]+=1
        return count
            
