class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        p1, p2 = 0, 0 
        while p1 < len(name) and p2 < len(typed):
            if name[p1] == typed[p2]:
                p1 += 1
                p2 += 1
            elif p2 >= 1 and typed[p2] == typed[p2-1]:
                p2 += 1
            else:
                return False
        if p1 != len(name):
            return False
        else:
            while p2 < len(typed):
                if typed[p2] != typed[p2-1]:
                    return False
                p2 += 1
        return True
