# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = defaultdict(lambda:-1)

        prev1 = -1
        prev2 = -1

        curr1 = l1
        curr2 = l2

        while curr1 or curr2:
            if curr1:
                prev[curr1] = prev1
                prev1 = curr1
                curr1 = curr1.next

            if curr2:
                prev[curr2] = prev2
                prev2 = curr2
                curr2 = curr2.next
        
        lsn1 = prev1 
        lsn2 = prev2

        front = None
        carryP = 0
        curr = None
        while True:
            tot, carry = (lsn1.val+lsn2.val+carryP )%10, (lsn1.val+lsn2.val+carryP)//10

            curr = ListNode(tot)
            curr.next = front
            front = curr

            carryP = carry
            
            flag1 = False if  prev[lsn1] != -1 else True
            flag2 = False if  prev[lsn2] != -1 else True
            lsn1 = prev[lsn1] if prev[lsn1] != -1 else ListNode(0)
            lsn2 = prev[lsn2] if prev[lsn2] != -1 else ListNode(0)

            if not carryP and flag1 and flag2:
                break

        
        return curr