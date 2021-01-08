class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x={}
        t=[]
        for i in set(nums):
            x[i]=nums.count(i)
        print(x.values())
        d={k: v for k, v in sorted(x.items(), key=lambda item: item[1],reverse=True)}
        for i,j in d.items():
            if k==0:
                break
            t.append(i)
            k=k-1
        return t
        
