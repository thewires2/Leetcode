class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x=[]
        for i,j in enumerate(nums):
            a=target-j
            if a in nums[i+1:]:
                x.append(nums.index(j))
                x.append(nums.index(target-j,i+1))
                break
        return x
