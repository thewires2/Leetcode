class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        x={}
        for i in s:
            if i not in x:
                x[i]=1
            else:
                x[i]+=1
                
        l=0 
        r=0
        count=[]
        y={}
        while r<len(s):
            if s[r] not in y:
                y[s[r]]=1
            else:
                y[s[r]]+=1
                
            if y[s[l]]==x[s[l]]:
                f=True
                k=0
                for i in y:
                    k+=y[i]
                    if y[i]!=x[i]:
                        f=False
                        break
                if f==False:
                    l+=1
                    r+=1
                else:
                    count.append(k)
                    l=r+1
                    r=r+1
                    y={}
            else:
                r+=1
                
        return count
