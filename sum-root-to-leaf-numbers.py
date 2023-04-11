# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        def backtrack(node, num):

            num.append(str(node.val))

            if not node.left and not node.right:
                ans.append(int(''.join(num)))

            if node.left:
                backtrack(node.left, num)
            if node.right:
                backtrack(node.right, num)

            num.pop()
        
        backtrack(root, [])
        
        return sum(ans)