lass Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        k=
        z=set(A)
        for i in z:
            if A.count(i)==1:
                if i>k:
                    k=i
        if k==0:
            return -1
        else:
            return k
        
