class Solution:
    def countVowelStrings(self, n: int) -> int:
        arr=['a','e','i','o','u']
        k=0
        def recurse(n,arr,i):
            if n==0: return 1
            result=0
            for j in arr:
                if j>=i:
                    result+=recurse(n-1,arr,j)
            return result
        for i in arr:
            k+=recurse(n-1,arr,i)
        return k
                    
                
