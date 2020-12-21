class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        for i in s:
            if i.isalnum()==False:
                continue
            else:
                a=a+i
        a=a.lower()
        print(a)
        if a==a[::-1]:
            return True
