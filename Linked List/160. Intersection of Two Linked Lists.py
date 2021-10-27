# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        p1 = headA
        p2 = headB
        
        while p1 or p2:
            if p1 == p2:
                return p1
            if p1==None and p2!=None:
                p1=headB
                p2=p2.next
            elif p1!=None and p2==None:
                p2=headA
                p1=p1.next
            else:
                p1=p1.next
                p2=p2.next
            
