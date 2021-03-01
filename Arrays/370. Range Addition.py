class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        x=[0]*length
        for i in updates:
            
            x[i[0]]+=i[2]
            
            if i[1]<length-1:
                x[i[1]+1]-=i[2]
        for i in range(1,len(x)):
            x[i]+=x[i-1]
        print(len(x))
        return x
            
            
        
