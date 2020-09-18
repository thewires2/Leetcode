class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        studentRecord = {}
        returnList = []
        for i in items:
            if i[0] not in studentRecord.keys():
                studentRecord[i[0]] = [i[1]]
            else:
                studentRecord[i[0]].append(i[1])

        for i, j in studentRecord.items():
            print(i,j)
            j = sorted(j)
            j = j[len(j)-5:len(j)]
            studentRecord[i] = int(sum(j)/5)
            returnList.append([i,studentRecord[i]])

        return returnList
