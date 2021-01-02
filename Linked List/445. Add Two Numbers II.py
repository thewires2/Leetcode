# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x,y="",""
        while l1:
            x=x+str(l1.val)
            l1=l1.next
        while l2:
            y=y+str(l2.val)
            l2=l2.next
        y=str(int(x)+int(y))
        head=ListNode()
        node=head
        for i in range(len(y)):
            head.val=int(y[i])
            if i==len(y)-1:
                break
            head.next=ListNode()
            head=head.next
        return node
