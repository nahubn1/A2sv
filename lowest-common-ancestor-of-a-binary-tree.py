# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        ans = None

        def dfs(node):
            if not node:
                return 0
            

            curr = ((node == p) + (node == q))
            left = dfs(node.left)
            right = dfs(node.right)

            if curr + left + right == 2:
                nonlocal ans
                ans = node

            return max(curr, left, right)
        
        dfs(root)
        return ans