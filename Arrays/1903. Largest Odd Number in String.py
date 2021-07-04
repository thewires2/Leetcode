class Solution:
    def largestOddNumber(self, num: str) -> str:
        x="97531"
        for i in range(len(num)-1,-1,-1):
            if num[i] in x:
                return num[:i+1]
        return ""
