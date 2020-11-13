class Solution:
    def generateTheString(self, n: int) -> str:
        if n%2!=0:
            a='a'*n
            return a
        else:
            return 'a'*(n-1)+'b'
        
