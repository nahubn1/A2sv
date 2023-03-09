# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def register(self, node, n, level):
        if not node:
            return 
        
        self.levels[level].append(n)
        self.register(node.left, 2*n, level+1)
        self.register(node.right, 2*n+1, level+1)
        
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.levels = defaultdict(list)
        self.register(root, 1, 0)
        
        max_width = 0
        
        for level in self.levels.values():
            max_width = max(max_width, max(level)-min(level)+1)
        
        return int(max_width)