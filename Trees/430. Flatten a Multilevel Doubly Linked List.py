class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return None
        stack=[head]
        pseudo=Node(0,None,head,None)
        prev=pseudo
        
        while stack:
            curr=stack.pop()
            
            prev.next=curr
            curr.prev=prev
            
            if curr.next:
                stack.append(curr.next)
                
            if curr.child:
                stack.append(curr.child)
                
                curr.child=None
            
            prev=curr
            
        pseudo.next.prev = None
        return pseudo.next
