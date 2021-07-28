class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        x={}
        d=[]
        for i in range(k):
            if nums[i] not in x:
                x[nums[i]]=1
            else:
                x[nums[i]]+=1
        s=len(list(x.keys()))
        d.append(s)
        for i in range(k,len(nums)):
            if nums[i] not in x:
                x[nums[i]]=1
                s+=1
            else:
                x[nums[i]]+=1
                
            if x[nums[i-k]]==1:
                del x[nums[i-k]]
                s-=1
            else:
                x[nums[i-k]]-=1
            d.append(s)
        return d
