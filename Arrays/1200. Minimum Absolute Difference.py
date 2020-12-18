class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        y=[]
        arr.sort()
        x=arr[1]-arr[0]
        for i in range(1,len(arr)):
            x=min(x,abs(arr[i]-arr[i-1]))
        for i in range(1,len(arr)):
            if abs(arr[i]-arr[i-1])==x:
                y.append([arr[i-1],arr[i]])
        return y
        
