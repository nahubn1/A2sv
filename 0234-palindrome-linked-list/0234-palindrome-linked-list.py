# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def copy_list(self, head):
        org_head = ListNode(head.val)
        node = head.next
        temp = org_head
        
        while node:
            temp.next = ListNode(node.val)
            node = node.next
            temp = temp.next
            
        return org_head
    
    def reverseList(self, head):
                
        prev = None
        node = head
        
        while node:
            front = node.next
            node.next = prev
            
            prev = node   
            node = front
        
        return prev
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        new_head = self.copy_list(head)
        # print('$', new_head)
        rev_head = self.reverseList(new_head)
        # print('[]', rev_head)
        node = head
        rev_node = rev_head
        # print('%', head)
        
        
        while node:
            if node.val != rev_node.val:
                return False
            
            node = node.next
            rev_node = rev_node.next
        else:
            return True
                