class Solution:
    def validIPAddress(self, IP: str) -> str:
        x=IP.split('.')
        if len(x)==4:
            for i in x:
                if i.isnumeric() == True:
                    if int(i)>=0 and int(i)<=255:
                        if i[0]=="0" and len(i)!=1:
                            return "Neither"
                        else:
                            continue
                    else:
                            return "Neither"
                else:
                    return "Neither"
            return "IPv4"
        y=IP.split(':')
        s="".join(i for i in y)
        try:
            if int(s, 16):
                if len(y)==8:
                    for i in range(8):
                        if len(y[i])>=1 and len(y[i])<=4:
                                continue
                        else:
                            return "Neither"
                    return "IPv6"
        except:
            return "Neither"
        return "Neither"
