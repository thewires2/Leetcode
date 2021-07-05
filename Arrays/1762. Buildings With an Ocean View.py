class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        if len(heights)==1:
            return [0]
        else:
            last_idx = len(heights)-1
            stack = [last_idx]
            for idx in reversed(range(len(heights)-1)):
                if heights[idx]>heights[stack[-1]]:
                    stack.append(idx)
            return stack[::-1]
