# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.sum = 0
        addedLevels = set()
        def dfs(node, level):
            if not node:
                return

            if level in addedLevels:
                self.sum += node.val

            if node.val % 2 == 0:
                addedLevels.add(level+2)
            
            dfs(node.left, level+1)
            dfs(node.right, level+1)

            if level+2 in addedLevels:
                addedLevels.remove(level+2)
        dfs(root, 0)
        return self.sum