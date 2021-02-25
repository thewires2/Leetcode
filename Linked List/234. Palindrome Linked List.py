# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        x=[]
        while head:
            x.append(head.val)
            head=head.next
        if x==x[::-1]:
            return True
