# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cycle = False
        
        # Phase I
        slow = head
        fast = head        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                cycle = True
                meet_node = slow
                break
        
        # Phase II
        if cycle:
            curr = head

            while curr != meet_node:
                curr = curr.next
                meet_node = meet_node.next

            return curr
        