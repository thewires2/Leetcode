# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small=[]
        eq=[]
        a=head
        y=head
        while head:
            if int(head.val) >= x:
                eq.append(head.val)
            else:
                small.append(head.val)
            head=head.next
        result=small+eq
        for i in result:
            a.val=i
            a=a.next
        return y
