# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, minn, maxx):
    
            if not node:
                return True
            
            if minn < node.val < maxx:
                return dfs(node.left, minn, node.val) and dfs(node.right, node.val, maxx)
            else:
                return False
        
        return dfs(root, -inf, inf)