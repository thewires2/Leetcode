class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        ans=0
        arr=[]
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                arr.append(s[i:j])
        
        for w in arr:
            i=0
            j=len(w)
            while j<=len(t):
                wrd=t[i:j]
                k=1
                flag=True
                for m in range(len(wrd)):
                    if w[m]!=wrd[m]:
                        if k==1:
                            k=0
                        else:
                            flag=False
                            break
                if flag and k==0:
                    ans+=1
                i+=1
                j+=1
        return ans
