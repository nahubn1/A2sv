# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def search(self, node):
        if not node:
            return

        self.search(node.left)
        if self.idx < self.k:
            self.idx += 1
            self.value = node.val

            self.search(node.right)


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.idx = 0
        self.value = None
        self.search(root)
        return self.value