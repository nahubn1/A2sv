# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        ptr1 = dummy

        while ptr1.next:
            min_prev = ptr1
            min_node = min_prev.next
            

            prev2 = ptr1
            ptr2 = prev2.next
        
            while ptr2:
                if ptr2.val < min_node.val:
                    min_node = ptr2
                    min_prev = prev2
                else:
                    ptr2 = ptr2.next
                    prev2 = prev2.next
                
            min_prev.next = min_node.next

            forward = ptr1.next
            ptr1.next = ListNode(min_node.val)
            ptr1.next.next = forward

            ptr1 = ptr1.next

        return dummy.next
                

            
