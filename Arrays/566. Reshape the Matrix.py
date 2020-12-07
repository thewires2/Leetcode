class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c!=len(nums)*len(nums[0]):
            return nums
        s=[]
        nums = [item for sublist in nums for item in sublist]
        k=0
        for i in range(r):
            x=[]
            for j in range(c):
                x.append(nums[k+j])
            k=k+c
            s.append(x)
        return s
