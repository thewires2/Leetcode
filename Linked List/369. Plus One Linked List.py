# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, l1: ListNode) -> ListNode:
        x=""
        while l1:
            x=x+str(l1.val)
            l1=l1.next
        y=str(int(x)+1)
        head=ListNode()
        node=head
        for i in range(len(y)):
            head.val=int(y[i])
            if i==len(y)-1:
                break
            head.next=ListNode()
            head=head.next
        return node
