class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        k1,k2=[],[]
        z=-inf
        for i in range(len(arrays)):
            k1.append([arrays[i][0],i])    
            k2.append([arrays[i][-1],i])
        k1.sort(key=lambda a:a[0])
        k2.sort(key=lambda a:a[0],reverse=True)
        print(k1)
        print(k2)
        if k1[0][1]==k2[0][1]:
            return max(abs(k2[1][0]-k1[0][0]),abs(k1[1][0]-k2[0][0]))
        return abs(k1[0][0]-k2[0][0])
