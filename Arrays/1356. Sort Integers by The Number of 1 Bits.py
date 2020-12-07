class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        x={}
        f=[]
        if len(set(arr))==1 and len(arr)!=1:
            return arr
        for i in arr:
            x[i]=str(bin(i)[2:]).count('1')
        for i in set(x.values()):
            d=[]
            for m,n in x.items():
                if n==i:
                    for _ in range(arr.count(m)):
                        d.append(m)
            d.sort()
            f.append(d)
        flat_list = [item for sublist in f for item in sublist]
        return flat_list
