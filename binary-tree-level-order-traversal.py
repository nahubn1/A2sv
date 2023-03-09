# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def register(self, node, level):
        if not node:
            return 
        
        self.levels[level].append(node.val)

        self.register(node.left, level+1)
        self.register(node.right, level+1)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.levels = defaultdict(list)
        self.register(root, 0)
        return self.levels.values()