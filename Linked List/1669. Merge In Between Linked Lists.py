# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        k=-1
        pre=ListNode(-1000,list1)
        x=ListNode()
        y=ListNode()
        while pre:
            if pre.next and k==a-1:
                x=pre
                while k!=b:
                    pre=pre.next
                    k+=1
                y=pre.next
            k+=1
            pre=pre.next
        x.next=list2
        print(x.val,y.val)
        while list2:
            if list2.next:
                list2=list2.next
            else:
                list2.next=y
                break
        return list1
