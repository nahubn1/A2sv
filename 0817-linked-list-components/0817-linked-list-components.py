# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        
        flag = False
        curr = head
        count = 0
        while curr:
            if flag and curr.val not in nums:
                count += 1
                                
            if curr.val in nums:
                flag = True
            else:
                flag = False
            
            curr = curr.next
        
        if flag:
            count += 1
        
        return count