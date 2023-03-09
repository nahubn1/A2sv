# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def register(self, node, c, r):
        if not node:
            return
        
        self.positions[(c, r)].append(node.val)
        self.register(node.left, c-1, r+1)
        self.register(node.right, c+1, r+1)

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.positions = defaultdict(list)

        self.register(root, 0, 0)

        columns = defaultdict(list)
        for c, r in sorted(self.positions.keys()):
            columns[c].extend(sorted(self.positions[(c, r)]))

        return columns.values()