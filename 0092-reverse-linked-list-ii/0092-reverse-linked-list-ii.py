# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_node(self, index, node, start=0):
        i = start
        curr_node = node

        while i < index:
            curr_node = curr_node.next     
            i += 1
                
        return curr_node
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_node = ListNode()
        dummy_node.next = head
        left_end = self.get_node(left-1, dummy_node)
        middle_start = left_end.next
        right_start = self.get_node(right+1, middle_start, left)
        

        i = left+1
        prev = middle_start
        node = middle_start.next
        
        while i <= right:
            forward = node.next
            node.next = prev

                
            prev = node
            node = forward
            
            i += 1
        
        left_end.next = prev
        middle_start.next = right_start
        
        return dummy_node.next