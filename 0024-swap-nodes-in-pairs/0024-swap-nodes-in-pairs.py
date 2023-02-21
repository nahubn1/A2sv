# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        curr = head
        prev = dummy
        last = dummy
        even = False
        
        while curr:
            if even:
                last.next = curr
                
                forward = curr.next
                curr.next = prev
                
                last = prev
                prev = curr
                curr = forward
                
                even = not even
    
            else:
                prev = curr
                curr = curr.next
                
                
                even = not even
                
        if not even:
            last.next = None
        else:
            last.next = prev
                
        return dummy.next