class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        x={}
        f=[]
        z=[]
        for i in pieces:
            x[i[0]]=i
        l=0
        while l<len(arr):
            if arr[l] in x:
                f.append(x[arr[l]])
                print(f)
            else:
                return False
            print(len(x[arr[l]]))
            l=l+len(x[arr[l]])
        
        for i in f:
            for x in i:
                z.append(x)
                
        if z==arr:
            return True 
        return False
