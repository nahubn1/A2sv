# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ans = list()

        count = Counter()
        def dfs(node):
            if not node:
                return ''
            
            subTree = f'<{dfs(node.left)}{node.val}{dfs(node.right)}>'
            if count[subTree] == 1:
                ans.append(node)
            
            count[subTree] += 1
 
            return subTree
        
        dfs(root)
        return ans