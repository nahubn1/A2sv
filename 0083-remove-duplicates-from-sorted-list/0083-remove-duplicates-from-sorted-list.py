# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        dummy_node = ListNode()
        dummy_node.next = head
        prev = dummy_node
        curr = head
        
        while curr:
            if curr.val in visited:
                prev.next = curr.next
                curr = curr.next
            else:
                visited.add(curr.val)
                curr = curr.next
                prev = prev.next
        
        return dummy_node.next