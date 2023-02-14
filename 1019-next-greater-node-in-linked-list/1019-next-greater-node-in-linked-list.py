from collections import defaultdict
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        idx = defaultdict(list)
        res = []
        curr = head
        stack = []
        i = 0
        while curr:
            res.append(0)
            idx[curr.val].append(i)
            
            while stack and curr.val > stack[-1]:
                res[idx[stack.pop()].pop()] = curr.val
            else:
                stack.append(curr.val)
                
            i += 1
            curr = curr.next
    
        return res
            
        
        
        
        