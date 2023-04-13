"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}
        i = 0

        originalHead = head
        dummyNode = Node(0)
        prev = dummyNode 
        while head:
            curr = Node(head.val)
            hashmap[head] = curr

            prev.next = curr
            prev = curr

            head = head.next

            i += 1
        
        head = originalHead
        curr = dummyNode.next
        while curr:
            if head.random:
                curr.random = hashmap[head.random]
            else:
                curr.random = None
            curr = curr.next
            head = head.next
        
        return dummyNode.next