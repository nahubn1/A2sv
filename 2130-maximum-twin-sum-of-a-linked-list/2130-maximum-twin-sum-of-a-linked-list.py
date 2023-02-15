# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # counting n
        curr = head
        n = 0
        while curr:
            n += 1
            curr = curr.next

        # reversing half of the list
        ptr1 = head
        ptr2 = head.next
        i = 0
        while i < (n//2)-1:
            forward = ptr2.next
            ptr2.next = ptr1

            ptr1 = ptr2
            ptr2 = forward

            i += 1

        # calculating max twin sum
        max_sum = 0
        while ptr2:
            max_sum = max(max_sum, ptr1.val + ptr2.val)
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            

        return max_sum



        