class Solution:
    def maximum69Number (self, num: int) -> int:
        num=str(num)
        x=num.find('6')
        if x!=-1:
            num=num.replace('6','9',1)
        return int(num)
