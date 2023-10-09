# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def check(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
        
            if node1.val == node2.val:
                return (check(node1.left, node2.left) and check(node1.right, node2.right)) or \
                       (check(node1.left, node2.right) and check(node1.right, node2.left))
            else:
                return False
        
        return check(root1, root2)