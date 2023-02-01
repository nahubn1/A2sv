# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_dummy_head = ListNode()
        less_curr = less_dummy_head 
        geater_dummy_head = ListNode()
        greater_curr = geater_dummy_head
        
        curr = head
        
        while curr:
            if curr.val < x:
                less_curr.next = ListNode(curr.val)
                less_curr = less_curr.next
            else:
                greater_curr.next = ListNode(curr.val)
                greater_curr = greater_curr.next
            curr = curr.next
            
        less_curr.next = geater_dummy_head.next
        
        return less_dummy_head.next
            
                
                
                
                
            