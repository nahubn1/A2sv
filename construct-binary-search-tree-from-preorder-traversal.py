# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        def construct(start, end):
            if start > end:
                return

            node = TreeNode(preorder[start])

            i = start+1
            while i <= end and preorder[i] < preorder[start]:
                i += 1
            
            node.left = construct(start+1, i-1)
            node.right = construct(i, end)

            return node
        
        return construct(0, len(preorder)-1)