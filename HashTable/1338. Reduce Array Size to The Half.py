class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        x={}
        y=[]
        k=len(arr)
        for i in arr:
            if i not in x:
                x[i]=1
            else:
                x[i]+=1
        y=sorted(list(x.values()))
        print(y)
        c=0
        while True:
            c+=1
            k-=y.pop()
            if k<=len(arr)//2:
                break
        return c
                
        
        
