class Solution:
    def balancedStringSplit(self, s: str) -> int:
        counter = {'L': 0, 'R': 0}
        count = 0
        for i in range(len(s)):
            counter[s[i]] += 1
            if counter['L'] == counter['R']:
                count += 1
                counter['L'] = 0
                counter['R'] = 0
        return count
