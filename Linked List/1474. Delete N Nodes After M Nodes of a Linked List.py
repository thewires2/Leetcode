# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        curNode = ListNode(0)
        curNode.next = head

        while curNode and curNode.next:
            for i in range(m):
                if curNode:
                    curNode=curNode.next
                else:
                    break
                
            for i in range(n):
                if curNode and curNode.next:
                    curNode.next=curNode.next.next
                else:
                    break
        return head
