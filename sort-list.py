# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
            
        if not head.next:
            return head
        
        head1, head2 = self.split(head)
       
        return self.merge(self.sortList(head1), self.sortList(head2))


    def split(self, head):
        n = 0 
        fast = head.next
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None

        return head, head2
    
    def merge(self, head1, head2):
        if (head1 and not head2) or (head1 and head2 and head1.val <= head2.val):
            node = ListNode(head1.val)
            node.next =  self.merge(head1.next, head2)
        elif (not head1 and head2) or (head1 and head2 and head2.val <= head1.val):
            node = ListNode(head2.val)
            node.next =  self.merge(head1, head2.next)
        else:
            node = None
        
        return node