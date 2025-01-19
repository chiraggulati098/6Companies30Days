# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return 
        
        resHead = ListNode(val = -1)
        cur = resHead
        
        idx = -1 * float('inf')
        while idx != -1:
            minVal = float("inf")
            idx = -1

            for i, x in enumerate(lists):
                if x and x.val < minVal:
                    minVal = x.val
                    idx = i
            
            if idx == -1 * float('inf'):
                return

            if idx == -1:
                return resHead.next
                
            cur.next = ListNode(minVal)
            lists[idx] = lists[idx].next
            cur = cur.next