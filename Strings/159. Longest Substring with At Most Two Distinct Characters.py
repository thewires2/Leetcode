from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n= len(s)
        if n<3:
            return n
    
        left=0
        right=0

        hashmap=defaultdict()
        max_len=2

        while right<n:
            if len(hashmap)<3:
                hashmap[s[right]]=right
                right+=1
                print(hashmap)

            if len(hashmap)==3:
                del_idx=min(hashmap.values())
                del hashmap[s[del_idx]]
                left=del_idx+1
            max_len = max(max_len, right - left)

        return max_len  
            
