# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        t=0
        x=head
        pre=x
        a=x
        while head:
            t+=1
            if pre!=None:
                pre=pre.next
            if t==k:
                a=head
                pre=x
            head=head.next
        if pre!=a:
            pre.val,a.val=a.val,pre.val
        return x
