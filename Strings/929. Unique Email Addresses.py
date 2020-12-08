class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        d=[]
        for i in emails:
            x,y=i.split("@")
            if "+" in x:
                x=x[:x.index("+")]
            x=x.replace(".","")
            d.append(x+"@"+y)
        return len(set(d))
