# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root, left, right):
        if not root:
            return True
        
        if root.val <= left or root.val >= right:
            return False

        return self.check(root.left, left, root.val) and self.check(root.right, root.val, right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, -inf, inf)