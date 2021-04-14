# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        x=head
        y=[]
        while x:
            if x:
                y.append(x.val)
            x=x.next
        if y==[]:
            return head
        if k>len(y):
            k=k%len(y)
        y=y[-k:]+y[:-k]
        node=head
        for i in y:
            node.val=i
            node=node.next
        return head
