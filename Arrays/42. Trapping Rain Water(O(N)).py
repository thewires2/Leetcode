class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = height[0]
        max_l = [0]
        max_right = height[-1]
        max_r = []
        
        for i in range(1,len(height)):
            max_left = max(height[i-1],max_left)
            max_l.append(max_left)
            
        for i in range(len(height)-2,-1,-1):
            max_right = max(height[i+1],max_right)
            max_r.append(max_right)
        
        max_r.reverse()
        max_r.append(0)
        min_lr = []
        for i,j in zip(max_l,max_r):
            min_lr.append(min(i,j))
            
        count = 0
        for i in range(len(height)):
            k=min_lr[i]-height[i]
            if k>=0:
                count+=k
        return count
