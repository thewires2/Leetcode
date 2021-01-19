class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        r=k
        t=0
        z=sum(arr[l:r])
        while r<len(arr)+1:
            if (z//k)>=threshold:
                t=t+1
            #print(arr[l:r])
            if r<len(arr):
                z=z+(arr[r]-arr[l])
            r=r+1
            l=l+1
            #print(z)
            
        return t
