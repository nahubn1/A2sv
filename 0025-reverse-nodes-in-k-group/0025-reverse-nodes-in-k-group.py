# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # counting length
        cr = head
        n = 0
        while cr:
            n += 1
            cr = cr.next

        dummy_node = ListNode()
        dummy_node.next = head

        # tail1 is a candidate tail it will get full entiltlment to tail after orginal tail has finished his service 
        tail = dummy_node
        tail1 = head
        
        prev = dummy_node
        curr = head 


        for i in range(n//k): # to iterate k chunks at a time 
            for j in range(k): # to reverse each chunks
                forward = curr.next
                curr.next = prev

                prev = curr
                curr = forward

            # connecting two cunks 
            tail.next = prev
            tail = tail1
            tail1 = curr
        
        # considering the left out chunk
        tail.next = curr

        return dummy_node.next




                
