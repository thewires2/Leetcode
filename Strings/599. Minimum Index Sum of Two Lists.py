class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        k=[]
        x=[]
        d1=dict()
        for i in list1:
            if i in list2:
                d1[i]=list1.index(i)+list2.index(i)
                k.append(list1.index(i)+list2.index(i))
        for i,j in d1.items():
            if j==min(k):
                x.append(i)
        return x
        
                
