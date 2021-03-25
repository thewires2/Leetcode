# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists==[] or lists==[[]]:
            return None
        print(lists)
        x=[]
        for i in lists:
            if i==None:
                continue
            while True:
                x.append(i.val)
                i=i.next
                if i==None:
                    break
        if x==[]:
            return None
        x.sort()
        z=ListNode(x[0])
        y=z
        for i in range(1,len(x)):
            z.next=ListNode(x[i])
            z=z.next
        return y
