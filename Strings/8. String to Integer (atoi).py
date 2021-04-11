class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        upper_bound = 2 ** 31
        lower_bound = upper_bound * -1
        read = ""
        is_negative = False
        
        s = s.lstrip()
        
        if not s:
            return 0
        
        if s[0] == "-":
            is_negative = True
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        
        for i in s:
            if i.isdigit():
                read += i
            else:
                break
                
        if read:
            read = read.lstrip("0")
            if read.isdigit():
                read = int(read)
            else:
                return 0
        else:
            return 0
        
        if is_negative:
            read *= -1
        
        if read < lower_bound:
            read = lower_bound
        elif read > (upper_bound - 1):
            read = (upper_bound - 1)
            
        return read
