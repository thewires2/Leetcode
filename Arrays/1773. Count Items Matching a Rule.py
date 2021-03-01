class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        k=0
        if ruleKey=="type":
            x=0
        elif ruleKey=="color":
            x=1
        else:
            x=2
        
        for i in items:
            if i[x]==ruleValue:
                k+=1
        return k
