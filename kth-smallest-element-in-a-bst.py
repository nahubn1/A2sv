# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = -1

        def dfs(start, node):
            nonlocal ans

            if not node:
                return 0
            
            left = dfs(start, node.left)
            i  = start + left
            if i == k: ans = node.val
            right = dfs(i+1, node.right)

            return left+right+1
        
        dfs(1, root)
        return ans