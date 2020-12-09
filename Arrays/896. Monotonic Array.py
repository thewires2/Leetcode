class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(set(A))==1:
            return True
        if A[-1]-A[0]>0:
            for i in range(1,len(A)):
                if A[i-1]<=A[i]:
                    continue
                else:
                    return False
            return True
        else:
            for i in range(1,len(A)):
                if A[i-1]>=A[i]:
                    continue
                else:
                    return False
            return True
        
