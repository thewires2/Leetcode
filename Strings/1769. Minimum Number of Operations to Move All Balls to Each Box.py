class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        x=[]
        for i in range(len(boxes)):
            k=0
            for j in range(len(boxes)):
                if i==j:
                    continue
                elif boxes[j]=="0":
                    continue
                else:
                    k+=abs(j-i)
            x.append(k)
        return x
