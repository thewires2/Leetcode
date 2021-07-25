class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        x={}
        for i in logs:
            if i[0] not in x:
                x[i[0]]={i[1]}
            else:
                x[i[0]].add(i[1])
        res = [0]*k
        for i in x.values():
            res[len(i)-1] += 1
        return res
