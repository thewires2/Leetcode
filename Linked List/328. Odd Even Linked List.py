# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd=[]
        even=[]
        k=1
        x=head
        y=head
        while head:
            if k%2!=0:
                odd.append(head.val)
            else:
                even.append(head.val)    
            head=head.next
            k+=1
        result=odd+even
        for i in range(len(result)):
            x.val=result[i]
            x=x.next
        return y
            
        
                
                
