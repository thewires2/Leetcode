# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        tmp = head
        k=0
        while tmp:
            tmp=tmp.next
            k=k+1
        k=k//2
        for i in range(k):
            head=head.next
        return head
