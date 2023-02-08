# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = ListNode()
        dummy.next = curr
        rem = 0
        while l1 or l2:
            tot = l1.val + l2.val + rem
            if tot > 9:
                curr.next = ListNode(tot-10)
                rem = 1
            else:
                curr.next = ListNode(tot)
                rem = 0
            
            if l2.next and not l1.next:
                l1.next = ListNode(0)
            if l1.next and not l2.next:
                l2.next = ListNode(0)
            
            l1 = l1.next
            l2 = l2.next
            curr = curr.next

        if rem:
            curr.next = ListNode(rem)

        return dummy.next.next

