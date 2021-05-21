class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        x={}
        l=0
        r=0
        max_len=1
        if len(s)*k==0:
            return 0
        while r<len(s):
            x[s[r]]=r
            r+=1
            if len(set(x))>k:
                del_idx = min(x.values())
                del x[s[del_idx]]
                l = del_idx + 1
            max_len = max(max_len, r - l)

        return max_len
