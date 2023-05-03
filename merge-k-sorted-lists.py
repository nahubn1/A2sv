# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        hashmap = defaultdict(list)

        for node in lists:
            if node:
                heap.append(node.val)
                hashmap[node.val].append(node)
        heapify(heap)

        dummy = head = ListNode()
        while heap:
            node = hashmap[heappop(heap)].pop()
            head.next = ListNode(node.val)
            head = head.next

            if node.next:
                heappush(heap, node.next.val)
                hashmap[node.next.val].append(node.next)
        
        return dummy.next