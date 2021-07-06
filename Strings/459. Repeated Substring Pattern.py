class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        ans=""
        temp=""
        
        for i in range(0,len(s)-1):
            temp+=s[i]
            if  len(s)%len(temp)==0 and temp*int((len(s)/len(temp)))==s:
                print(temp)
                return 1
        
        return 0
