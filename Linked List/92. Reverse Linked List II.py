# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy_head = sublist_head = ListNode(0,head)
        for _ in range(1,left):
            sublist_head=sublist_head.next
            
        #Reversal
        sublist_iter = sublist_head.next
        for _ in range(right-left):
            temp=sublist_iter.next
            print(sublist_head)
            sublist_iter.next , temp.next , sublist_head.next = temp.next , sublist_head.next , temp
        print(sublist_head)
            
        
        return dummy_head.next
            
