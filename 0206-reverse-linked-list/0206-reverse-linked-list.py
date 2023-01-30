# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        prev = None
        node = head
        
        while True:
            front = node.next
            node.next = prev
            prev = node
            
            if not front:
                break
                
            node = front
        
        return node
                