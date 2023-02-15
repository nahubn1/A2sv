# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        ptr1 = head
        prev = head
        ptr2 = head.next
        odd = False
        while ptr2:
            if odd:
                forward = ptr1.next
                ptr1.next = ListNode(ptr2.val)
                ptr1.next.next = forward
                
                prev.next = ptr2.next
                
                ptr1 = ptr1.next
                ptr2 = ptr2.next
                
            else:
                ptr2 = ptr2.next
                prev = prev.next
                
            
            odd = not odd
        
        return head
    