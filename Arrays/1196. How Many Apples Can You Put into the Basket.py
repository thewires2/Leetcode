class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        x=[]
        if sum(arr)<=5000:
            return len(arr)
        arr.sort()
        print(arr)
        for i in arr:
            if sum(x)<=5000:
                x.append(i)
            else:
                break
        return len(x)-1
            
