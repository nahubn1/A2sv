# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, node):
        if not node:
            return 0, 0

        left_n, left_total = self.check(node.left)
        right_n, right_total = self.check(node.right)
        
        n = left_n + right_n + 1
        total = left_total + right_total + node.val

        if total//n == node.val:
            print('yey')
            self.count += 1

        return n, total

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.check(root)
        return self.count