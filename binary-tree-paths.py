# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def connect(self, root, arr):
        arr.append(str(root.val))

        if not root.left and not root.right:
            self.ans.append('->'.join(arr)) 

        if root.left:
            self.connect(root.left, arr)
        if root.right:
            self.connect(root.right, arr)
        arr.pop()
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ans = []
        self.connect(root, [])
        return self.ans