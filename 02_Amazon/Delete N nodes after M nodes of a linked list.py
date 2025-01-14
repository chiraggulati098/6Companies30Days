class Solution:
    def linkdelete(self, head, n, m):
        # Code here
        cur = head  

        while cur:
            for _ in range(1, m):
                if cur is None:         
                    return head
                cur = cur.next
    
            if cur is None:             
                return head
    
            t = cur.next
            for _ in range(1, n + 1):
                if t is None:           
                    break
                temp = t
                t = t.next
                del temp  
    
            cur.next = t
            cur = t
    
        return head