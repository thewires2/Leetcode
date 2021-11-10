# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        
        sum_poly = dummy = PolyNode()
        
        while poly1 or poly2:
            power1=poly1.power if poly1 else -1
            power2=poly2.power if poly2 else -1
            
            if power1==power2:
                coeff = poly1.coefficient + poly2.coefficient
                if coeff!=0:
                    dummy.next = PolyNode(coeff,poly1.power)
                    dummy , poly1 , poly2 = dummy.next , poly1.next , poly2.next
                else:
                    poly1 , poly2 =poly1.next , poly2.next
                
            elif power1>power2:
                dummy.next=PolyNode(poly1.coefficient,poly1.power)
                dummy , poly1 = dummy.next , poly1.next
                
            elif power2>power1:
                dummy.next=PolyNode(poly2.coefficient,poly2.power)
                dummy , poly2 = dummy.next , poly2.next
        return sum_poly.next
                
