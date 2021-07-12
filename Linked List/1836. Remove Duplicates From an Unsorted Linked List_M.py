# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        x={}
        dummy_head=final=ListNode()
        tail=head
        while head:
            if head.val not in x:
                x[head.val]=1
            else:
                x[head.val]+=1
            head=head.next
        while tail:
            if x[tail.val]!=1:
                while tail and (x.get(tail.val)!=1):
                    dummy_head.next=tail.next
                    tail=tail.next 
            else:
                dummy_head.next=tail
                dummy_head=dummy_head.next   
                tail=tail.next
        return final.next
                
