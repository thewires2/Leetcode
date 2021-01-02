# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        x=[]
        z=False
        if head==None:
            return False
        while head:
            if head not in x:
                x.append(head)
                head=head.next
            else:
                z=True
                break
        return z
        
