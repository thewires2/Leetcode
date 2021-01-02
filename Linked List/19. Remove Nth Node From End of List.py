# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node=head
        z=head
        k=0
        while head:
            k=k+1
            head=head.next
        if n==k:
            node=node.next
            return node
        if n==0:
            while node:
                if node.next.next==None:
                    node.next=None
                    break
                node=node.next
            return z
        k=k-n
        while True:
            if k==1:
                node.next=node.next.next
                break
            k=k-1
            node=node.next
        return z
            
