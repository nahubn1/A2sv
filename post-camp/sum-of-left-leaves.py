# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        def dfs(node, d):
            nonlocal ans
            if not node.left and not node.right and d == 'left':
                ans += node.val
            
            if node.left: dfs(node.left, 'left')
            if node.right: dfs(node.right, 'right')
        
        dfs(root, "")
        return ans

