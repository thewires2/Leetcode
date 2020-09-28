if not l1:
            return l2
        if not l2:
            return l1
        
        
        pointer1=l1
        pointer2=l2
        
        if l1.val<=l2.val:
            head=l1
        else:
            head=l2
            
        while pointer1 and pointer2:
            
            if pointer1.val <= pointer2.val:
                while  pointer1 and pointer1.val <= pointer2.val:
                    temp1=pointer1
                    pointer1=pointer1.next
                temp1.next=pointer2
            
            else:
                while pointer2 and pointer2.val < pointer1.val:
                    temp2=pointer2
                    pointer2=pointer2.next
                temp2.next=pointer1
                
        return head
