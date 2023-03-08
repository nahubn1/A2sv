# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root, maximum):
        if not root:
            return True, maximum
        
        flag, maximum = self.check(root.left, maximum)

        if not flag or root.val <= maximum:
            return False, maximum

        maximum = root.val
        flag, maximum = self.check(root.right, maximum)

        return flag, maximum

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, -inf)[0]