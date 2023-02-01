# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        curr = head
        n = 0
        while curr:
            curr = curr.next
            n += 1
            
        k %= n
        i = 0
        dummy_head = ListNode(None)
        dummy_head.next = head
        ptr = dummy_head
        while i < n-k:
            ptr = ptr.next
            i += 1
        
        rot_dummy_head = ListNode()
        curr = rot_dummy_head
        while ptr and ptr.next:
            curr.next = ListNode(ptr.next.val)
            curr = curr.next
            ptr.next = ptr.next.next
        
        curr.next = head
        
        return rot_dummy_head.next
        
        
        
            
        
        