class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x=[]
        t=[]
        for i in strs:
            if sorted(i) not in t:
                t.append(sorted(i))
                x.append([i])
            else:
                x[t.index(sorted(i))].append(i)
        return x
