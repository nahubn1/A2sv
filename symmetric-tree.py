# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @staticmethod
    def split(root):
        root1 = TreeNode(root.val)
        root1.left = root.left

        root2 = TreeNode(root.val)
        root2.right = root.right

        return root1, root2

    def reflect(self, root):
        if not root.left and not root.right:
            root.left, root.right = root.right, root.left
        elif root.left and not root.right: 
            root.left, root.right = root.right, self.reflect(root.left)
        elif not root.left and root.right:
            root.left, root.right = self.reflect(root.right), root.left
        else:
            root.left, root.right = self.reflect(root.right), self.reflect(root.left)
        
        return root


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p and not q) or (not p and q):
            return False
        elif not p and not q:
            return True

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        root1, root2 = self.split(root)
        root2 = self.reflect(root2)

        return self.isSameTree(root1, root2)