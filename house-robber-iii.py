# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def dp(node, state):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val
            
            if state in memo:
                return memo[state]

            op1  = node.val
            if node.left: 
                op1 += dp(node.left.left, 4*state)
                op1 += dp(node.left.right, 4*state + 1 )
            if node.right:
                op1 += dp(node.right.left, 4*state + 2)
                op1 += dp(node.right.right, 4*state + 3)
            
            op2 = dp(node.left, 2*state) + dp(node.right, 2*state+1)
        
            memo[state] = max(op1, op2)
            return memo[state]
        
        return dp(root, 1)