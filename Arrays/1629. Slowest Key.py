class Solution:
    def slowestKey(self, nums: List[int], keysPressed: str) -> str:
        x=[]
        x.append(nums[0])
        for i in range(1,len(nums)):
            x.append(nums[i]-nums[i-1])
        print(x)
        if x.count(max(x))==1:
            return keysPressed[x.index(max(x))]
        else:
            y=[]
            print(keysPressed)
            for i,j in enumerate(x):
                if j==max(x):
                    y.append(keysPressed[i])
            y.sort()
            return y[-1]
